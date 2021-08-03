"""
@author:  吴登科
@data: 2021-07-27
@function 公共方法基类
"""
import sys
import time
import csv
import codecs
from time import sleep
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.common import Common


class Base:
    # 获取测试用户信息
    def get_user(self):
        with codecs.open(base_path + "/test_dir/data/test_staff_info.csv", 'r', encoding='gbk') as fp:
            user_info = {}
            fp_key = csv.reader(fp)
            for csv_key in fp_key:
                csv_reader = csv.DictReader(fp, fieldnames=csv_key)
                for row in csv_reader:
                    user_info = dict(row)
        return user_info

    # 登录操作
    def login(self, browser, base_url):
        self.common = Common(browser)
        self.common.get(base_url + '/index.php/employform/index')
        user = self.get_user()
        if self.common.get_url == base_url + '/index.php/employform/login/index':
            self.common.input_staff_name = user['name']
            self.common.input_password = user['password']
            self.common.login_button.click()
        sleep(15)

    # 关闭全部弹窗
    def close_layer(self):
        flag = False
        if len(self.common.layer_divs) > 0:  # 弹出弹窗
            for layer_shade in self.common.layer_shades:
                self.common.execute_script('arguments[0].click()', layer_shade)  # 关闭弹窗
            flag = True
        assert flag is True, "弹窗关闭失败!"

    # 退出登录操作
    def logout(self):
        self.common.avatar_warn.click()  # 点击右上角用户头像
        is_display = self.common.avatar_box.is_displayed()  # 用户头像下拉框
        if is_display is True:
            self.common.logout_btn.click()  # 点击退出登录

    # 客户列表菜单
    def customer_menu(self):
        self.common.customer_menu.click()  # 点击客户管理菜单栏
        self.common.customer_list.click()  # 点击客户列表菜单

    # 客户报备菜单
    def customer_report_menu(self):
        self.common.customer_report_menu.click()  # 点击报备报价合同菜单栏
        self.common.customer_report_list.click()  # 点击客户报备菜单
