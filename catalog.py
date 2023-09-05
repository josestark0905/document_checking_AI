import xml.etree.ElementTree as ET
from jieba import analyse
from gensim import corpora
from gensim import models
from gensim import similarities
import jieba


def extract_words(text):
    # 引入TextRank关键词抽取接口
    textrank = analyse.textrank
    # 基于TextRank算法进行关键词抽取
    keywords = textrank(text)
    # 输出抽取出的关键词
    for keyword in keywords:
        print(keyword + "/")


def read_xml(path):
    root = ET.parse(path).getroot()
    all_content = []
    for node in root.iter():
        if "hlink" in node.tag:
            for content in node.iter():
                split_content = content.tag.split("}")
                end_split_content = split_content[len(split_content) - 1]
                if end_split_content == "t" and content.text != " " and "、" not in content.text:
                    if "1" not in content.text and "2" not in content.text and "3" not in content.text and "4" not in content.text and "5" not in content.text and "6" not in content.text and "7" not in content.text and "8" not in content.text and "9" not in content.text and "0" not in content.text:
                        all_content.append(content.text)
    return all_content


def similarity(standard, test):
    lose = []
    for doc_standard in standard:
        # 1 分词
        # 1.1 历史比较文档的分词
        all_location_list = []
        for doc in test:
            doc_list = [word for word in jieba.cut_for_search(doc)]
            # doc_list = [word for word in jieba.cut(doc)]
            all_location_list.append(doc_list)

        # 1.2 测试文档的分词
        doc_test_list = [word for word in jieba.cut_for_search(doc_standard)]

        # 2 制作语料库
        # 2.1 获取词袋
        dictionary = corpora.Dictionary(all_location_list)

        # 2.2 制作语料库
        # 历史文档的二元组向量转换
        corpus = [dictionary.doc2bow(doc) for doc in all_location_list]
        # 测试文档的二元组向量转换
        doc_test_vec = dictionary.doc2bow(doc_test_list)

        # 3 相似度分析
        # 3.1 使用TF-IDF模型对语料库建模
        tfidf = models.TfidfModel(corpus)

        # 3.2 对每个目标文档，分析测试文档的相似度
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
        sim = index[tfidf[doc_test_vec]]

        # 根3.3 据相似度排序
        result = sorted(enumerate(sim), key=lambda item: -item[1])
        if result[0][1] is None or result[0][1] < 0.6:
            lose.append(doc_standard)
        return lose


if __name__ == '__main__':
    Test = read_xml(R'C:\Users\Archillesheel\Desktop\样本\示例2\长青线路跨越大广高速专项施工方案.xml')
    Standard = ['施工步骤', '施工准备', '放线施工', '压线施工', '导地线展放', '紧挂线施工', '附件安装', '封顶网及架体拆除', '施工组织', '安全保障措施',
                '质量保证措施', '应急处置方案', '铁路应急抢险预案', '行车组织方案', '麻城', '工务段', '人身安全控制方案', '主要工器具表（按一个施工组配置）']
    print(similarity(Standard, Test))
