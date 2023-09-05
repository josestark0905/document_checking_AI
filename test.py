import jieba
import snownlp

if __name__ == "__main__":
    f = open(R".\docProcParaData.txt", encoding='utf-8')
    text = f.read()
    f.close()
    # print(text)
    s = snownlp.SnowNLP(text)
    print(s.keywords(10))
    print(s.summary(10))
