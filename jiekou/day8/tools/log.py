#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: log.py
# @Author: Bull
# ---
# *日志处理类，没有使用“单例模式”。所以使用这个类会重复输出日志

import logging.handlers

from day8.setting import DIR_NAME


class Getlog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.path = DIR_NAME + '/log/test.logger'

    def get_logger(self):
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
        fm = logging.Formatter(fmt)

        tf = logging.handlers.TimedRotatingFileHandler(
            filename = self.path,
            when = 'H',
            backupCount = 24,
            encoding = 'utf-8'
        )

        #tf处理器，用来写文件
        tf.setFormatter(fm)
        # 给“处理器”设置级别
        tf.setLevel(logging.DEBUG)
        self.logger.addHandler(tf)

        # ch处理器，用来把日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fm)
        self.logger.addHandler(ch)

        return  self.logger

logger = Getlog().get_logger()

if __name__ == '__main__':
    logger = Getlog().get_logger()
    logger.info('日志信息')