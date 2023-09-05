from enum import Enum
import easyocr
from imageai.Prediction import ImagePrediction
import os
import cv2

ocr_reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
execution_path = os.getcwd()
imageai_model_path = "fig_process\\DenseNet-BC-121-32.h5"
imgai_model = ImagePrediction()
imgai_model.setModelTypeAsDenseNet121()
imgai_model.setModelPath(os.path.join(execution_path, imageai_model_path))
imgai_model.loadModel()


class fig_type(Enum):
    scenery = 1
    engin = 2
    paper = 3
    others = 4


def ocr_check(s, keywords):
    for word in keywords:
        if s.find(word) >= 0:
            return True
    return False


def imgai_check(predictions, probabilities, keywords):
    count = 0
    for i in range(len(predictions)):
        if predictions[i] in keywords:
            count += probabilities[i]
    if count > 0.5:
        return True
    return False


def color_check(fig_path):
    img = cv2.imread(fig_path)
    precision = 50
    color_percent = 0.8
    w = 0
    b = 0
    tot = img.shape[0] * img.shape[1]
    pixels = img.reshape(1, tot, 3)[0]
    div = tot // 500000 + 1
    tot = tot // div

    for i in range(0, len(pixels), div):
        color = pixels[i]
        if color[0] > 255 - precision and color[1] > 255 - precision and color[2] > 255 - precision:
            w += 1
        elif color[0] < precision and color[1] < precision and color[2] < precision:
            b += 1

    if float(w + b) / tot > color_percent:
        return True
    return False


def fig_proc(fig_path):
    '''
    fig_path - path to the figure. exp: './fig_process/1.1.png'
    '''
    label = 'other'

    # ocr keywords
    ocr_engin = ['导线', '钢绳', '力绳', '锚', '连接线', '光缆', '滑车', '扣', '跨越', '封网', '示意图']
    ocr_paper = ['复函', '批准', '证书', '方案', '意见', '委员会', '资格', '证书', '证件', '中心']

    # figure recognition keywords
    imgai_scenery = ['breakwater', 'dam', 'lakeside', 'seashore', 'freight_car', 'maze', 'worm_fence', 'lampshade',
                     'crane', 'water_tower', 'chainlink_fence', 'beacon', 'obelisk', 'pole', 'trimaran',
                     'drilling_platform', 'radio_telescope', 'space_shuttle']
    imgai_engin = ['rule', 'slide_rule', 'envelope', 'crossword_puzzle', 'menu', 'oscilloscope', 'safety_pin',
                   'paper_towel']
    imgai_paper = ['carton', 'envelope', 'bucket', 'book_jacket', 'web_site', 'menu']

    # ocr
    result = ocr_reader.readtext(fig_path, detail=0)
    s = "".join(result)
    s = s.replace(' ', '')

    if ocr_check(s, ocr_paper):
        return 'paper'

    # figure recognition
    predictions, probabilities = imgai_model.classifyImage(os.path.join(execution_path, fig_path), result_count=5)

    if not color_check(fig_path) and imgai_check(predictions, probabilities, imgai_scenery):
        return 'scenery'
    if ocr_check(s, ocr_engin) + imgai_check(predictions, probabilities, imgai_engin) + color_check(fig_path) >= 2:
        return 'engin'
    if imgai_check(predictions, probabilities, imgai_paper):
        return 'paper'

    return label


if __name__ == "__main__":
    prefix = './fig_process/'
    postfix = '.png'

    for i in range(11, 18):
        site = prefix + str(i) + postfix
        print(str(i), fig_proc(site))
