#-*- coding:utf-8-*-
# @Time    :2019/4/15 16:37
# @Author  :武汉-七月
# @File    :http_request.py
# @Software:PyCharm Community Edition

import requests
class HttpRequest:
    """
    使用request实现注册，登录，充值接口的相互调用，返回响应数据
    """
    def __init__(self):
        # 初始化一个session实例
        self.session = requests.sessions.session()

    def httprequest(self, method, url, data):
        if method.lower() == "get":
            resp = self.session.request(method, url, data)
        elif method.lower() == "post":
            resp = self.session.request(method, url, data)
        else:
            print("un_support method!")
        return resp
    #
    # def get(self):


    def close(self):
        # 关闭session实例
        self.session.close()

if __name__ == '__main__':
    # resp1=HttpRequest().httprequest("post","http://test.lemonban.com/futureloan/mvc/api/member/login",{"mobilephone": "15810447878", "pwd": "123456"})
    # resp2=HttpRequest().httprequest("post","http://test.lemonban.com/futureloan/mvc/api/member/recharge",{"mobilephone":"15810447878", "amount": "1000"})
    # resp2.close()
    #
    # print(resp1.text)
    # print(resp2.text)
    t = HttpRequest()
    # t1 = HttpRequest()
    # print(id(t))
    # print(id(t1))
    resp1 =t.httprequest("post", "http://test.lemonban.com/futureloan/mvc/api/member/login",
                                      {"mobilephone": "15810447878", "pwd": "123456"})
    # resp2 =t.httprequest("post", "http://test.lemonban.com/futureloan/mvc/api/member/recharge",
    #                                   {"mobilephone": "15810447852", "amount": "41"})
    resp3 = t.httprequest("post", "http://test.lemonban.com/futureloan/mvc/api//member/bidLoan",
                          {"memberId": "1", "pwd": "123456","loanId": "1", "amount": "1000"})

    resp4 = t.httprequest("post","http://test.lemonban.com/futureloan/mvc/api/loan/add",
                          { "id": "199","memberId": "701","title": "贷款投资买房®","amount": "100000.00","loanRate": "18.1","loanTerm": "6",
        "loanDateType": "0","repaymemtWay": "4","biddingDays": "5"})
    # resp2.close()
    print(resp1.text)
    print(resp1.json())
    print(type(resp1.text))
    print(type(resp1.json()))
    print(resp1.status_code)
    # print(resp2.json())
    print(resp3.json())
    print(resp4.json())

    if '{"status":1,"code":"10001","msg":"登录成功","data":null,}'=='{"status":1,"code":"10001","data":null,"msg":"登录成功"}':
        print("dui")
    else:
        print("cuo")