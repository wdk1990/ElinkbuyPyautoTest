"""
@author:  吴登科
@data: 2021-08-02
@function 易联购客户报价操作测试
"""
import sys
import time
import pytest
import datetime
from time import sleep
from os.path import dirname, abspath
from page.offer_page import OfferPage

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)

from dbConn import DB
from .base import Base


class TestOffer(Base):
    """
    模拟业务原给指定客户报价操作
    """

    def test_offer_case(self, browser, base_url):
        """
        验证报价页面是否正常打开
        点击添加验证价格列表页面是否能正常打开
        """
        self.login(browser, base_url)
        page = OfferPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.customer_menu()  # 点击客户列表菜单
        else:
            print("弹层关闭失败")
        sleep(2)

        page.offer_button.click()  # 点击报价按钮
        sleep(2)

        customer_list_handle = page.current_window_handle  # 当前页面句柄
        all_handles = page.window_handles  # 所有页面句柄
        for handle in all_handles:
            if handle != customer_list_handle:
                page.switch_to_window(handle)

        assert page.get_title == '报价单-北京易联购科技有限公司'
        client_id = page.client_id.get_attribute('value')
        page.add_goods_price_btn.click()  # 点击添加按钮
        sleep(2)

        assert page.get_title == '价格列表-北京易联购科技有限公司'
        page.search_keyword = 'LC10M'  # 输入货品名称
        page.search_button.click()
        sleep(2)

        page.price_check.click()  # 点击阶梯价格查询按钮
        sleep(3)

        url_temps = page.get_url.replace("//", '').split('/')
        price_id = url_temps[-1]  # 价格ID
        flag = False
        if 'priceCompute' in url_temps:  # 价格计算页面
            flag = True
        assert flag is True


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_offer.py"])
