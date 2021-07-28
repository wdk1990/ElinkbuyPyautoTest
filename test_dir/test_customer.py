"""
@author:  吴登科
@data: 2021-07-27
@function 易联购客户相关测试用例类
"""
import sys
import time
import pytest
import datetime
from dateutil.relativedelta import relativedelta
from time import sleep
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.customer_page import CustomerPage
from dbConn import DB
from .base import Base


class TestCustomer(Base):
    """
    客户列表相关功能测试:
        1.客户等级筛选
        2.注册方式筛选
        3.客户状态筛选
        4.合作状态筛选
        5.vip等级筛选
        6.无需维护筛选
        7.回访状态筛选
        8.手机号筛选
        9.关键词筛选
    """

    def test_customer_list_case(self, browser, base_url):
        """
        模拟点击客户列表或我的客户子菜单进入客户列表页
        1.验证当前登录员工所属全部客户数据
        """
        self.login(browser, base_url)
        self.page = CustomerPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.page.customer_menu.click()  # 点击客户管理菜单栏
        else:
            print("弹层关闭失败")
        self.page.customer_list.click()  # 点击客户列表菜单
        sleep(3)









if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_customer.py"])
