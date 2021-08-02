"""
@author:  吴登科
@data: 2021-07-12
@function 易联购登录页面测试用例类
"""
import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.login_page import LoginPage


def get_data(file_path):
    """读取登录测试数据"""
    data = []
    with(open(file_path, "r", encoding="utf8")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(i)
    return data


class TestLogin:
    """登录页面测试"""

    @pytest.mark.parametrize(
        "data",
        get_data(base_path + "/test_dir/data/test_login_data.json")
    )
    def test_login_case(self, data, browser, base_url):
        """
        模拟登录
        步骤：
        1，输入用户名
        2.输入密码
        3.点击登录按钮
        检查点：
        *检查输入用户名和密码是否为空
        """
        page = LoginPage(browser)
        page.get(base_url + "/index.php/employform/Login/index")
        page.input_staff_name = data["user"]
        page.input_password = data["pwd"]
        page.login_button.click()
        sleep(2)

        if data['user'] == '' and page.user_error.text != '':
            result = page.user_error.text
        elif data['pwd'] == '' and page.pwd_error.text != '':
            result = page.pwd_error.text
        elif data['user'] == 'error_user_name' and data['pwd'] == 'error_password' and page.all_error.text != '':
            result = page.all_error.text
        else:
            result = '登录成功'

        assert result == data['expected']
        sleep(2)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])
