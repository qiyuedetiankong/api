# -*- coding:utf-8-*-
# @Time    :2019/6/10
# @Author  :武汉-七月
# @File    :web_operate.py
# @Software:PyCharm Community Edition
# 请在课堂派中实现以下操作：
# 0、使用帐号和密码登陆课堂派。
# 1、进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少
# 2、获取1中作业下，作业被分享的同学名称。
# 3、在1中，切换到作业讨论，并发表你的评论。
#  4、点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。
# 5、在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。
# 【进阶思考：设计一条测试用例，来确认你的搜索结果与期望的匹配。使用unittest哦！！】
# ps：代码连接运行5次都通过的情况下，才算比较稳定。提交上来的代码，一定要是自己运行通过的。
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 开启goolge浏览器
driver = webdriver.Chrome()
# 访问课堂派 webdriver中只有get方法源码中设置了等待
driver.get("http://www.ketangpai.com")
# 点击首页的登录按钮
driver.find_element_by_xpath('//a[text()="登录"]').click()
# 点击登录后又新界面弹出，需要设置等待，此处使用全局等待的方式等待20s
driver.implicitly_wait(20)
#1. 点击账号登录、输入用户名和密码，点击登录后，跳转到班级页面，关掉通知窗口
driver.find_element_by_xpath('//a[text()="账号登录"]').click()
driver.find_element_by_xpath('//input[@name="account"]').send_keys("XXXX")
driver.find_element_by_xpath('//input[@type="password"]').send_keys("XXXXX")
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]//a[text()="登录"]').click()
driver.find_element_by_xpath('//a[@class="close"]').click()
# 进入该学生所在班级
driver.find_element_by_xpath('//dt[@class="bgclass0"]//a[@title="Python全栈第15期"]').click()
# 随机查看一个有成绩的作业
driver.find_element_by_xpath('//a[@title="2019-04-23 完成数据校验"]').click()
# 2.获取改作业下被分享的同学名称
eles = driver.find_elements_by_xpath('//p[@class="share-name"]')
for ele in eles:
    print(ele.text)
# 3.切换到作业讨论，点击添加评论，写评语，点击确定
driver.find_element_by_xpath('//a[text()="作业讨论"]').click()
driver.find_element_by_xpath('//p[text()="添加评论"]').click()
driver.find_element_by_xpath('//textarea[@class="comment-txt"]').send_keys("Like the last and the one before")
# driver.find_element_by_xpath('//textarea[@placeholder="添加评论"]').send_keys("Like the last and the one before")
driver.find_element_by_xpath('//a[@class="sure active"]').click()
# 4.点击其中一个进行评语的同学进行回复
# driver.find_element_by_xpath('//li[@data-id="MDAwMDAwMDAwMLOcy5mHqbtthbVyoQ"]//a[@title="回复"]').click()
# driver.find_element_by_xpath('//textarea[@placeholder="添加评论"]').send_keys("Like the last and the one before")
# driver.find_element_by_xpath('//a[@class="sure active"]').click()
# 4.1 回到学生界面对其中一个同学进行回复
driver.find_element_by_xpath('//span[text()="Python全栈第15期"]').click()
driver.find_element_by_xpath('//a[text()="同学"]').click()


driver.find_element_by_xpath('//li[@data-uid="MDAwMDAwMDAwMLSsz96Iqadq"]//a[@class="call"]').click()
driver.find_element_by_xpath('//textarea[@class="ps-container"]').send_keys("test")
driver.find_element_by_xpath('//a[text()="发送"]').click()


# 5.搜索学生id，显示其相关信息






# driver.quit()



# 手机短信验证码登录
# driver.find_element_by_xpath('//a[text()="手机短信登录"]').click()
# driver.find_element_by_xpath('//input[@name="tel"]').send_keys("15071177296")
# driver.find_element_by_xpath('//input[@name="pass"]').send_keys("421979")
