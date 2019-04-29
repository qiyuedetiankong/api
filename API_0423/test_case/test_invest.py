# -*- coding:utf-8-*-
# @Time    :2019/4/25
# @Author  :武汉-七月
# @File    :test_invest.py
# @Software:PyCharm Community Edition
from ddt import ddt, data, unpack  # 导入ddt模块
import json
import unittest
from  homework.API_0423.common.excelparse import *
from  homework.API_0423.common.http_request import *
from  homework.API_0423.common.contants import *
from  homework.API_0423.common.pymysqlparse import PymysqlPrase
from  homework.API_0423.common.contexts import Contexts


@ddt
class Testinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.HttpRequest = HttpRequest()
        cls.sql = PymysqlPrase()

    @classmethod
    def tearDownClass(cls):
        cls.HttpRequest.close()
        cls.sql.sql_close()
        print("用例执行完毕")

    @data(*(ExcelParse(case_file, "invest").get_case()))
    @unpack
    def test_invest(self, case_id, method, url, data, expected, sql,title):

        # 在请求之前替换参数化的值
        data = json.loads(Contexts().replace(json.dumps(data)))  # 替换前的data是字典，需转化成字符串，request请求传参需字典，故再转成字典
        resp = self.HttpRequest.httprequest(method, url, data).json()
        try:
            self.assertEqual(str(expected), resp["code"])
            row = case_id + 1
            ExcelParse(case_file, "invest").write_result(row, resp, "pass")

            # 判断加标成功之后，查询数据库，取到loan_id
            if resp["msg"] == "加标成功":
                # sql="select id from future.loan where memberid = 1406 order by id desc limit 1"
                loan_id = self.sql.fetchone(sql)[0]
                print(loan_id)
                # 给类属性重新赋值
                setattr(Contexts, "loan_id", str(loan_id))

        except Exception as e:
            row = case_id + 1
            ExcelParse(case_file, "invest").write_result(row, resp, "failed")
            raise e
