# -*- coding:utf-8-*-
# @Time    :2019/4/24
# @Author  :武汉-七月
# @File    :contexts.py
# @Software:PyCharm Community Edition
import re
from homework.API_0423.common.configparse import ReadConfig
import configparser


class Contexts:
    loan_id = None

    def replace(self, data):

        p = "#(.*?)#"  # 正则表达式 从#开始匹配，从#结束
        while re.search(p, data):  # 判断datal里面有没有符合p表达式的值
            m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
            k = m.group(1)  # 取到参数化的key
            try:
                v = ReadConfig().get_cfg_value("data", k)  # 根据key值找到配置文件中的value
            except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去Context里面取
                if hasattr(Contexts, k):
                    v = getattr(Contexts, k)  # 在context类中添加一个对应的key
                else:
                    print("没有找到需要参数化的值")
                    raise e
            print()
            # 替换后的内容，继续用data接收
            data = re.sub(p, v, data, count = 1)
        return data


if __name__ == '__main__':
    data = '{"id":"#loan_id#","status":4}'
    res = Contexts().replace(data)
    print(res)
    print(type(res))
