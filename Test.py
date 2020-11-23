# -*- coding: utf-8 -*-
import os
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller, SentenceSplitter
LTP_DATA_DIR = 'F:\\LTP\\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
print('\n'.join(sents))
segmentor = Segmentor()  # 初始化实例
segmentor.load("F:\\LTP\\ltp_data_v3.4.0\\cws.model")  # 加载模型
labeller = SementicRoleLabeller()
labeller.load("F:\\LTP\\ltp_data_v3.4.0\\pisrl_win.model")  # 加载模型
words = segmentor.segment('元芳你怎么看？我就趴窗口上看呗！')  # 分词
print('\t'.join(words))
segmentor.release()  # 释放模型
labeller.label()