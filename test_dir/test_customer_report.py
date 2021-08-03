"""
@author:  吴登科
@data: 2021-08-03
@function 易联购客户报备操作测试
"""
import sys
import time
import pytest
import datetime
from time import sleep
from os.path import dirname, abspath
from page.customer_report_page import CustomerReportPage

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)

from dbConn import DB
from .base import Base


class TestCustomerReport(Base):
    """ 客户报备相关测试用例类"""

    def test_report_case(self, browser, base_url):
        """
        模拟业务员报备客户:
        1.点击顶级菜单报备报价合同下客户报备菜单
        2.验证是否正常跳转到客户报备列表页
        3.验证报备列表数据
        """
        self.login(browser, base_url)
        self.close_layer()
        self.customer_report_menu()  # 点击进入客户报备列表页
        sleep(2)

        page = CustomerReportPage(browser)
        assert page.get_title == "客户报备-北京易联购科技有限公司"

        pagination = page.pagination  # 分页
        if len(pagination) > 0:
            page.last_page.click()  # 点击最后一页
            sleep(2)

        total_text = int(page.last_sort.text)  # 页面总计客户数
        db_conn = DB(ip='47.103.83.160', user='root', passwd='c587024e9ec3ea0a', db='ylg')
        user = self.get_user()
        result = 0
        reports = db_conn.query("select count(1) total from xy_report where staff_id=" + str(user['staff_id']) + "")
        if reports:
            result = reports[0]['total']
        assert result == total_text
        sleep(2)

        page.report_button.click()  # 点击报备按钮
        sleep(2)

        assert page.get_title == '报备验证-北京易联购科技有限公司'
        page.report_name_input = '张三'
        page.report_search_button.click()
        sleep(5)

        url_temps = page.get_url.replace("//", '').split('/')
        


    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_customer_report.py"])
