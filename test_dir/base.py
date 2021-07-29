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
        self.common_page = Common(browser)
        self.common_page.get(base_url + '/index.php/employform/index')
        user = self.get_user()
        if self.common_page.get_url == base_url + '/index.php/employform/login/index':
            self.common_page.input_staff_name = user['name']
            self.common_page.input_password = user['password']
            self.common_page.login_button.click()
        sleep(15)

    # 关闭全部弹窗
    def close_layer(self):
        flag = False
        if len(self.common_page.layer_divs) > 0:  # 弹出弹窗
            for layer_shade in self.common_page.layer_shades:
                self.common_page.execute_script('arguments[0].click()', layer_shade)  # 关闭弹窗
            flag = True
        return flag

    # 退出登录操作
    def logout(self):
        self.common_page.avatar_warn.click()  # 点击右上角用户头像
        is_display = self.common_page.avatar_box.is_displayed()  # 用户头像下拉框
        if is_display is True:
            self.common_page.logout_btn.click()  # 点击退出登录
