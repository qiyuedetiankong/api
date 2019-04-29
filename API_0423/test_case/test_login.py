#-*- coding:utf-8-*-
# @Time    :2019/4/16
# @Author  :武汉-七月
# @File    :test_login.py
# @Software:PyCharm Community Edition

from ddt import ddt, data, unpack
import json
import unittest
from  homework.API_0423.common.excelparse import *
from  homework.API_0423.common.http_request import *
from  homework.API_0423.common.contants import  *
from  homework.API_0423.common.log_parser import Catlogs



@ddt
class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.HttpRequest = HttpRequest()

    @classmethod
    def tearDownClass(cls):
        print("用例执行完毕")

    @data (*(ExcelParse(case_file,"login").get_case()))
    @unpack
    def test_login(self,case_id,  method, url, data, expected,sql,title):

        resp=self.HttpRequest.httprequest(method, url, data).json()
        try:
             self.assertEqual(eval(expected), resp)
             row=case_id+1
             ExcelParse(case_file,"login").write_result(row, resp, "pass")
             Catlogs().cat_logs("case:{},请求数据data:{},测试通过".format(title, data))
        except Exception as e:
             row = case_id + 1
             ExcelParse(case_file, "login").write_result(row, resp, "failed")
             Catlogs().cat_logs("case:{},请求数据data:{},测试失败".format(title, data))
             raise e