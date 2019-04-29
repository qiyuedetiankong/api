# -*- coding:utf-8-*-
# @Time    :2019/4/17
# @Author  :武汉-七月
# @File    :contants.py
# @Software:PyCharm Community Edition
import os

# 获取当前contants的绝对路径
base_dir1 = os.path.abspath(__file__)

# os.path.dirname()的功能相当于os.path.split()[0]
# base_dir2 = os.path.dirname(base_dir1)
# base_dir3 = os.path.split(base_dir1)[0]
# print(base_dir1)
# print(base_dir2)
# print(base_dir3)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
# 获取该文件的绝对路径
# excel 数据存放路径
case_file = os.path.join(base_dir, "data", "cases.xlsx")
#配置文件存放路径
global_file = os.path.join(base_dir, "config", "global_switch.conf")
online_file = os.path.join(base_dir, "config", "online.conf")
test_file = os.path.join(base_dir, "config", "test.conf")
sql_file = os.path.join(base_dir, "config", "sql.conf")
#log日志存放路径
logs_file = os.path.join(base_dir, "log", "logs.text")
# 测试用例路径
test_file = os.path.join(base_dir, "test_case")
# 测试报告路径
html_file=os.path.join(base_dir,"report")


