# -*- coding: utf-8 -*-
import os
from pyltp import Segmentor
import codecs
LTP_DATA_DIR = 'F:\\LTP\\ltp_data_v3.4.0'  # ltp模型目录的路径

#读取txt文件：
def read_txt(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines
if __name__ == '__main__':
    cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
    segmentor = Segmentor()  # 初始化实例
    segmentor.load("F:\\LTP\\ltp_data_v3.4.0\\cws.model")  # 加载模型
    with codecs.open('C:/Users/lenovo/Desktop/labels1.txt', 'w', 'utf-8') as fw:#labels
        doc = read_txt('C:/Users/lenovo/Desktop/垃圾.txt')
        for s in doc:
            #words = segmentor.segment(s)  # 分词
            fw.write('垃圾' + '\n')
            #print(' '.join(words))
    segmentor.release()  # 释放模型


