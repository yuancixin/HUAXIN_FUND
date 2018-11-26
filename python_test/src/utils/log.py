'''
Created on 2018年11月26日

@author: wanglx
'''
# -*- coding:UTF-8 -*-

# 官方
import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# own
LOG_DIR = "./__log"

# 创建一个logger,默认为root logger
logger = logging.getLogger()


def init_log(log_file_name="tmp"):
    """
    初始化log
    :param log_file_name: 文件名
    :return:
    """
    # 设置全局log级别为debug。注意全局的优先级最高

    logger.setLevel(logging.INFO)

    # 创建一个终端输出的handler,设置级别
    h_term = logging.StreamHandler(stream=sys.stdout)
    h_term.setLevel(logging.DEBUG)

    # log文件夹不存在 则创建
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # 创建一个文件记录日志的handler,设置级别为
    h_file = logging.handlers.RotatingFileHandler(os.path.join(LOG_DIR, log_file_name + ".log"),
                                                  maxBytes=10 * 1024 * 1024,
                                                  backupCount=5)
    h_file.setLevel(logging.INFO)

    # 创建一个全局的日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # 将日志格式应用到终端handler
    h_term.setFormatter(formatter)

    # 将日志格式应用到文件handler
    h_file.setFormatter(formatter)

    # 将终端handler添加到logger
    logger.addHandler(h_term)

    # 将文件handler添加到logger
    logger.addHandler(h_file)