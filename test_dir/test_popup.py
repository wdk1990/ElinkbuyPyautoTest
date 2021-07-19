"""
@author:  吴登科
@data: 2021-07-14
@function 易联购页头弹窗测试
"""
import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.popup_page import PopupPage


class TestPopup:
    """弹窗功能测试"""

    def login(self, browser, base_url):
        page = PopupPage(browser)
        page.get(base_url + '/index.php/employform/index')
        page.input_staff_name = '唐静'
        page.input_password = 'sh987654'
        page.login_button.click()
        sleep(10)

    def test_popup_show_case(self, browser, base_url):
        """
        检测弹窗弹出：
        步骤：
        1.检测弹层是否正常弹出
        2.检测点击信息图标是否正常出现下拉菜单
        """
        self.login(browser, base_url)
        self.page = PopupPage(browser)

        flag = False
        layer_divs = self.page.layer_divs  # 弹出弹窗
        if len(layer_divs) > 0:
            flag = True

        layer_shades = self.page.layer_shades
        for layer_shade in layer_shades:
            self.page.execute_script('arguments[0].click()', layer_shade)  # 关闭弹窗
        sleep(2)

        self.page.message_button.click()  # 点击信息图标
        is_display = self.page.message_box.is_displayed()

        if flag is True and is_display is True:
            flag = True
        else:
            flag = False

        assert flag is True

        # def test_wait_visit_case(self, browser, base_url):
        """
        模拟业务员弹窗待回访数据验证:
        1.
        """


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_popup.py"])
