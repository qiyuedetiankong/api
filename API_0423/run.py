#-*- coding:utf-8-*-
# @Time    :2019/4/26
# @Author  :武汉-七月
# @File    :run.py
# @Software:PyCharm Community Edition
import unittest
import time
from homework.API_0423.common.contants import *
from HTMLTestRunnerNew import HTMLTestRunner


discover = unittest.defaultTestLoader.discover(test_file, 'test*.py')
now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
report_name = 'report' + '_' + now + '.html'
report_path = os.path.join(html_file, report_name)
with open(report_path, 'wb+') as file:
    runner = HTMLTestRunner(stream=file, title='测试报告', tester ="武汉-七月",description='api测试')
    runner.run(discover)