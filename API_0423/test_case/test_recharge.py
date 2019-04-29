#-*- coding:utf-8-*-
# @Time    :2019/4/16
# @Author  :武汉-七月
# @File    :test_recharge.py
# @Software:PyCharm Community Edition

from ddt import ddt, data, unpack  #导入ddt模块
import json
import unittest
from  homework.API_0423.common.excelparse import *
from  homework.API_0423.common.http_request import *
from  homework.API_0423.common.contants import *
from  homework.API_0423.common.pymysqlparse import PymysqlPrase
from  homework.API_0423.common.log_parser import Catlogs


@ddt
class Testrecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.HttpRequest = HttpRequest()
        cls.sql = PymysqlPrase()

    @classmethod
    def tearDownClass(cls):
        cls.HttpRequest.close()
        cls.sql.sql_close()
        print("用例执行完毕")

    @data (*(ExcelParse(case_file,"recharge").get_case()))
    @unpack
    def test_recharge(self,case_id, method, url, data, expected, sql, title):
        # 充值前查询下当前充值账户的余额
        if sql is not None :
            number = self.sql.fetchone(sql)[0]
            self.before = int(number)
        resp=self.HttpRequest.httprequest(method, url, data).json()
        try:
            self.assertEqual(eval(expected)["msg"],resp["msg"])
            row=case_id+1
            ExcelParse(case_file,"recharge").write_result(row,resp,"pass")
            #充值成功后，查询账户余额是否符合预期
            if sql is not None:
                number = self.sql.fetchone(sql)[0]
                self.after= int(number)
                charge_amount= int(data["amount"])
                self.assertEqual(self.before+charge_amount,self.after)
            ExcelParse(case_file, "recharge").write_result(row, resp, "pass")
            Catlogs().cat_logs("case:{},请求数据data:{},查询的sql:{},测试通过".format(title, data, sql))
        except Exception as e :
            ExcelParse(case_file, "recharge").write_result(row, resp, "fail")
            Catlogs().cat_logs("case:{},请求数据data:{},查询的sql:{},测试失败".format(title, data, sql))
            raise e





