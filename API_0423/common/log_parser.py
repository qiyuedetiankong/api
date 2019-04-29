# -*- coding:utf-8-*-
# @Time    :2019/4/26
# @Author  :武汉-七月
# @File    :log_parser.py
# @Software:PyCharm Community Edition
import logging
from homework.API_0423.common.configparse import ReadConfig

from homework.API_0423.common import contants


class Catlogs:
    def __init__(self, encoding="utf-8"):
        '''初始化log日志log级别，log输出格式'''
        self.log_level = ReadConfig().get_cfg_value("log_info", "level")
        self.log_format = ReadConfig().get_cfg_value("log_info", "log_format")

    def cat_logs(self,msg):
        # 新建一个日志收集器，设置日志的收集格式，级别
        my_logger = logging.getLogger(contants.logs_file)
        my_logger.setLevel(self.log_level)
        fmt = logging.Formatter(self.log_format)
        # 新建一个日志输出渠道-文本渠道，设置输出格式，级别
        File_handler = logging.FileHandler(contants.logs_file,encoding="utf-8")
        File_handler.setFormatter(self.log_level)
        File_handler.setFormatter(fmt)

        # 日志收集器与渠道连接，日志输出到指定的渠道
        my_logger.addHandler(File_handler)

        if self.log_level == "CRITIAL":
            my_logger.critical(msg)
        elif self.log_level == "DEBUG":
            my_logger.debug(msg)
        elif self.log_level == "INFO":
            my_logger.info(msg)
        elif self.log_level == "WARNING":
            my_logger.warning(msg)
        elif self.log_level == "ERROR":
            my_logger.error(msg)
        my_logger.removeHandler(File_handler)


if __name__ == '__main__':
    Catlogs().cat_logs("nihao ")
    Catlogs().cat_logs("nihao ")
