"""
@author:  吴登科
@data: 2021-07-27
@function 易联购客户相关测试用例类
"""
import sys
import time
import pytest
import datetime
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
    不同条件筛选验证数据
    完善资料功能验证
    """

    def test_customer_list_case(self, browser, base_url):
        """
        模拟点击客户列表或我的客户子菜单进入客户列表页：
        1.点击最后一页最后的序号获取总记录数
        2.查询当前员工所属客户总数
        3.验证当前登录员工客户数
        """
        self.login(browser, base_url)
        page = CustomerPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.customer_menu()  # 点击客户列表菜单
        else:
            print("弹层关闭失败")
        page.window_scroll(None, 1000)
        sleep(3)

        page.last_page.click()  # 点击最后一页
        sleep(3)

        total_text = int(page.last_sort.text)
        result = 0
        db_conn = DB(ip='47.103.83.160', user='root', passwd='c587024e9ec3ea0a', db='ylg')
        user = self.get_user()
        sql = "select count(1) total from `xy_client` WHERE  `staff_id` =" + str(user['staff_id']) + " and `clientkind` = 1  and `tradekindid` <> 2  and `closed` = 'F'"
        if user['roles_str'] in [87, 91]:
            sql = "select count(1) total from `xy_client` WHERE  `staff_id` =" + str(user['staff_id']) + " and `clientkind` = 1  and `tradekindid` <> 2  and `closed` = 'F' and `high_quality` = 0"
        clients = db_conn.query(sql)
        if clients:
            result = clients[0]['total']
        sleep(3)
        assert result == total_text
        sleep(2)

    @pytest.mark.parametrize(
        "client_rank",
        ['A', 'B', 'C', 'D']
    )
    def test_customer_rank_case(self, browser, base_url, client_rank):
        """
        模拟点击客户等级下拉框筛选客户
        1.点击客户等级下拉框
        2.选择筛选等级
        3.点击搜索按钮
        """
        self.login(browser, base_url)
        page = CustomerPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.customer_menu()  # 点击客户列表菜单
        else:
            print("弹层关闭失败")
        page.search_client_rank.select_by_visible_text(client_rank)  # 选择客户等级A
        page.search_btn.click()  # 点击搜索按钮
        sleep(2)

        pagination = page.pagination  # 分页
        if len(pagination) > 0:
            page.window_scroll(None, 1000)
            page.last_page.click()  # 点击最后一页
            sleep(2)

        total_text = int(page.last_sort.text)
        result = 0
        db_conn = DB(ip='47.103.83.160', user='root', passwd='c587024e9ec3ea0a', db='ylg')
        user = self.get_user()
        sql = "SELECT count(1) total FROM `xy_client` WHERE  `staff_id` = 5  AND `clientkind` = 1  AND `tradekindid` <> 2  AND `closed` = 'F'  AND `client_rank` ='" + client_rank + "'"
        if user['roles_str'] in [87, 91]:
            sql = "SELECT count(1) total FROM `xy_client` WHERE  `staff_id` = 5  AND `clientkind` = 1  AND `tradekindid` <> 2  AND `closed` = 'F'  AND `client_rank` ='" + client_rank + "' and `high_quality` = 0"
        clients = db_conn.query(sql)
        if clients:
            result = clients[0]['total']

        assert result == total_text
        sleep(2)

    def test_customer_info_update_case(self, browser, base_url):
        """
        模拟修改客户资料功能验证：
        """
        self.login(browser, base_url)
        page = CustomerPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.customer_menu()  # 点击客户列表菜单
        else:
            print("弹层关闭失败")
        sleep(2)

        page.edit_customer_btn.click()  # 点击完善资料按钮
        sleep(2)

        assert page.get_title == '完善资料-北京易联购科技有限公司'


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_customer.py"])
