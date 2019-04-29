#-*- coding:utf-8-*-
# @Time    :2019/4/24
# @Author  :武汉-七月
# @File    :test_add.py
# @Software:PyCharm Community Edition
from ddt import ddt, data, unpack  #导入ddt模块
import json
import unittest
from  homework.API_0423.common.excelparse import *
from  homework.API_0423.common.http_request import *
from  homework.API_0423.common.contants import *
from  homework.API_0423.common.pymysqlparse import PymysqlPrase
from  homework.API_0423.common.contexts import Contexts
from  homework.API_0423.common.log_parser import Catlogs


@ddt
class Testadd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.HttpRequest = HttpRequest()
        cls.sql = PymysqlPrase()

    @classmethod
    def tearDownClass(cls):
        cls.HttpRequest.close()
        cls.sql.sql_close()
        print("用例执行完毕")

    @data (*(ExcelParse(case_file,"add").get_case()))
    @unpack
    def test_add(self,case_id, method, url, data, expected, sql,title):

        # 在请求之前替换参数化的值
        data = json.loads(Contexts().replace(json.dumps(data))) #替换前的data是字典，需转化成字符串，request请求传参需字典，故再转成字典
        # 加标前，查看该member_id的数据库的loan条数
        if sql:
            number = self.sql.fetchall(sql)
            self.before = len(number)
            Catlogs().cat_logs("case:{},加标前的loan条数{}".format(title,self.before))


        resp=self.HttpRequest.httprequest(method, url, data).json()
        try:
             self.assertEqual(str(expected), resp["code"])
             row=case_id+1
             ExcelParse(case_file,"add").write_result(row, resp, "pass")
             Catlogs().cat_logs("case:{},请求数据data:{},查询的sql:{},测试通过".format(title, data, sql))
             # 加标成功后，查看数据库是否有新增一条loan
             if sql:
                 number = self.sql.fetchall(sql)
                 self.after = len(number)
                 self.assertEqual(self.before + 1, self.after)
                 Catlogs().cat_logs("case{},加标后的loan条数{}".format(title,self.after))

        except Exception as e:
             row = case_id + 1
             ExcelParse(case_file, "add").write_result(row, resp, "failed")
             Catlogs().cat_logs("case:{},请求数据data:{},查询的sql:{},测试失败".format(title, data, sql))
             raise e