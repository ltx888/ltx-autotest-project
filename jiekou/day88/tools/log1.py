# coding:utf-8
# @File: log.py
# @author: Lvtiexin
import logging.handlers
import datetime

from day88.setting1 import DIR_NAME

class Getlog():
    def __init__(self):
        self.curr_time = datetime.datetime.now().date()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.path = DIR_NAME + '/log/'+ str( self.curr_time)+'.log'
        print(self.path)

    def get_logger(self):
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
        fm = logging.Formatter(fmt)

        tf = logging.handlers.TimedRotatingFileHandler(
            filename = self.path,
            when = 'H',
            backupCount = 24,
            encoding = 'utf-8',
        )
        # tf处理器，用于写文件
        tf.setFormatter(fm)
        # 给处理器设置级别
        tf.setLevel(logging.DEBUG)
        self.logger.addHandler(tf)

        # ch处理器，用来把日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fm)
        self.logger.addHandler(ch)

        return self.logger
logger = Getlog().get_logger()

if __name__ == '__main__':
    logger = Getlog().get_logger()
    logger.info('日志信息')