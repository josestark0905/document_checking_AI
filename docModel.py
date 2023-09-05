import docProcData
import jiebaTest


def cut_sentences(content, end_flag):
    content_len = len(content)
    sentences = []
    tmp_char = ''
    for idx, char in enumerate(content):
        tmp_char += char

        # check whether it is the end of input
        if (idx + 1) == content_len:
            sentences.append(tmp_char)
            break

        # check end flag
        if char in end_flag:
            # cut sentence
            next_idx = idx + 1
            if not content[next_idx] in end_flag:
                sentences.append(tmp_char)
                tmp_char = ''

    return sentences


def merge_str(l):
    s = ""
    for i in l:
        s += i
    return s


def docVec_check_jieba(doc, keys, like_threshold):
    """
    doc - the input paragraph for key point comparing
        [sentence1, sentence2 ...]
        [[sentence1, sentence2 ...], [...] ...]
    keys - key points
        [(string)key point1, key point2 ...]
    k - threshold values for similarity
    return empty list if all key points are found, else return list of key points unfound
    """
    tmp = keys.copy()
    for sentence in doc:
        # find keys[i] with highest similarity max_sim, if the max_sim is bigger than k, tmp.remove(k)
        similar_key = None
        max_sim = float("-inf")
        for key in tmp:
            vec1, vec2 = jiebaTest.get_word_vector(sentence, key)
            sim_cur = jiebaTest.cos_dist(vec1, vec2)
            if sim_cur > max_sim:
                max_sim = sim_cur
                similar_key = key
        if similar_key != None and similar_key in tmp and max_sim > like_threshold:
            tmp.remove(similar_key)

    return tmp


def doc_proc(para, keys, like_threshold=0.2, summary_threshold=8):
    """
    para - paragraph to test, a long string of characters. 
    keys - keywords for that paragraph. exp: ['sdfgsh', 'yerhwe']
    """
    # cut paragraph to sentences
    doc = cut_sentences(para, ['?', '!', '.', ',', '？', '！', '。', '…', '，', '\n'])

    # doc vector
    docVec = docVec_check_jieba(doc, keys, like_threshold)

    return docVec


if __name__ == "__main__":
    para = merge_str(docProcData.para_data(0))  # input paragraph
    keys_sets = docProcData.keys_data()  # input data of keywords

    doc_result = []
    for keys in keys_sets:
        if keys[0] == '文明施工：\n':
            print("number of keys is", len(keys))
            doc_result = doc_proc(para, keys)
            break
    print("number of unfound keys is", len(doc_result))
    for re in doc_result:
        print(re)
