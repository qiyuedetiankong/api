#-*- coding:utf-8-*-
# @Time    :2019/4/24
# @Author  :武汉-七月
# @File    :test_register.py
# @Software:PyCharm Community Edition
#-*- coding:utf-8-*-
# @Time    :2019/4/23
# @Author  :武汉-七月
# @File    :test_register_param.py
# @Software:PyCharm Community Edition
from ddt import ddt, data, unpack
import json
import unittest
import pymysql
import random
from  homework.API_0423.common.excelparse import *
from  homework.API_0423.common.http_request import *
from  homework.API_0423.common.contants import *
from  homework.API_0423.common.pymysqlparse import PymysqlPrase
from  homework.API_0423.common.log_parser import Catlogs
@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.HttpRequest = HttpRequest()
        cls.sql = PymysqlPrase()

    @classmethod
    def tearDownClass(cls):
        cls.HttpRequest.close()
        cls.sql.sql_close()
        print("用例执行完毕")

    @data (*(ExcelParse(case_file,"register").get_case()))
    @unpack
    def test_register(self,case_id,  method, url, data, expected, sql, title):

        # 判断参数化的标识符
        if data["mobilephone"] == "register_mobile":  # 判断注册手机号是否有标识化
            register_mobile = self.sql.fetchone(sql)[0] #sql语句查询后的返回结果是元组,取值后是字符串
            print("register_mobilephone",register_mobile)
            register_mobile = int(register_mobile)-random.randint(1,6000)
            # replace方法是特换之后重新返回一个新的字符串，所以需要使用data重新接收
            data["mobilephone"] = str(register_mobile)

        resp=self.HttpRequest.httprequest(method, url, data).json()

        try:
             self.assertEqual(eval(expected), resp)
             row=case_id+1
             ExcelParse(case_file,"register").write_result(row, resp, "pass")
             Catlogs().cat_logs("case:{},请求数据data:{},查询的sql:{},测试通过".format(title,data,sql))

        except Exception as e:
             row = case_id + 1
             ExcelParse(case_file, "register").write_result(row, resp, "failed")
             Catlogs().cat_logs("case:{},请求数据:{},查询的sql:{},测试失败".format(title, data, sql))
             raise e
