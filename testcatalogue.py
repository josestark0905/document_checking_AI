import docx
from gensim import corpora
from gensim import models
from gensim import similarities
import jieba


def test_catalogue(word, location_list=None):
    try:
        # 获取相似度阈值标准
        f = open("相似度阈值.txt")
        standard = float(f.readline())
        f.close()
    except:
        standard = 0.5
    # 标准库的分词和建模
    all_location_list = []
    if location_list == None:
        location_list = []
    f = open("目录标准库.txt", "r", encoding='UTF-8')
    for line in f.readline():
        location_list.append(line)
    f.close()
    for location in location_list:
        doc_list = [word for word in jieba.cut_for_search(location)]
        all_location_list.append(doc_list)
    # 1 获取词袋
    dictionary = corpora.Dictionary(all_location_list)
    # 2 制作语料库
    # 标准库的二元组向量转换
    corpus = [dictionary.doc2bow(doc) for doc in all_location_list]
    # 3 使用TF-IDF模型对语料库建模
    tfidf = models.TfidfModel(corpus)
    #####################################################################################
    # 检测文档的分词
    file = docx.Document(word)
    doc_test = ""
    for paragraph in file.paragraphs:
        print(paragraph.text)
        if ".." in paragraph.text:
            doc_test += paragraph.text
    print(doc_test)
    doc_test_list = [word for word in jieba.cut_for_search(doc_test)]
    # doc_test_list = [word for word in jieba.cut(doc_test)]

    # 测试文档的二元组向量转换
    doc_test_vec = dictionary.doc2bow(doc_test_list)

    # 对每个目标文档，分析测试文档的相似度
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    sim = index[tfidf[doc_test_vec]]

    # 根3.3 据相似度排序
    sim = sorted(enumerate(sim), key=lambda item: -item[1])
    print(sim)


if __name__ == '__main__':
    test_catalogue(R"C:\Users\Archillesheel\Desktop\样本\方案模板\模板-钢格构跨越架跨越高速公路施工方案.docx")
