#-*- coding:utf-8-*-
# @Time    :2019/4/23
# @Author  :武汉-七月
# @File    :pymysqlparse.py
# @Software:PyCharm Community Edition

import pymysql

from API_0423.common.configparse import ReadConfig
#修改修改
#5554546
class PymysqlPrase:
    def __init__(self):
        self.host = ReadConfig().get_cfg_value("sql", "host")
        self.user = ReadConfig().get_cfg_value("sql", "user")
        self.password = ReadConfig().get_cfg_value("sql", "password")
        port = 3306
        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        # port = 3306
        # 1、建立连接：数据库的连接信息：
        self.mysql = pymysql.connect(host=self.host, user=self.user, password=self.password, port=3306, charset="utf8")

        # 2、新建一个查询页面
        self.cursor = self.mysql.cursor()

    # 获取查询结果里面最近的一条数据返回
    def fetchone(self,sql):

        # 3、编写SQL、执行SQL、查询结果
        # sql = "SELECT max(MobilePhone) from future.member"
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    # 获取全部查询结果集
    def fetchall(self,sql):
        self.mysql.commit()
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def commit(self):
        self.mysql.commit()

    def sql_close(self):
        # 4、 关闭查询、关闭数据库连接
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    res=PymysqlPrase().fetchone("select id from future.loan where memberid = 1406 order by id desc limit 1")[0]
    # res = PymysqlPrase().fetchall("SELECT id FROM future.loan where memberid ='1406'")
    print(res)
    print(type(res))