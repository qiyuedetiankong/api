#-*- coding:utf-8-*-
# @Time    :2019/4/17
# @Author  :武汉-七月
# @File    :configparse.py
# @Software:PyCharm Community Edition
import configparser
from homework.API_0423.common.contants import *

class ReadConfig:
 """
 读取config中的配置文件

 """

 def __init__(self):

     # 打开配置文件global_file
     self.cfg=configparser.ConfigParser()
     self.cfg.read(global_file)

     # 读取global_file文件中的配置开关，通过配置开关的读取值来确定获取online.conf or test.conf
     switch = self.cfg.getboolean("switch","on")
     if switch:
         self.cfg.read(online_file,encoding="utf-8")
     else:
         self.cfg.read(test_file,encoding="utf-8")

 def get_cfg_value(self,section, option):
     return  self.cfg.get(section, option)

if __name__ == '__main__':
    print(ReadConfig().get_cfg_value("api", "pre_url"))
    print(ReadConfig().get_cfg_value("data", "normal_user"))
    print(ReadConfig().get_cfg_value("sql","host"))


