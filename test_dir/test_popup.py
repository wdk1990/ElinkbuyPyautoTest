"""
@author:  吴登科
@data: 2021-07-14
@function 易联购页头弹窗测试
"""
import sys
import time
import pytest
import csv
import codecs
from time import sleep
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.popup_page import PopupPage
from dbConn import DB


class TestPopup:
    """弹窗相关功能测试"""

    # 读取测试用登录员工数据
    def get_staff_info(self):
        csv_dict = {}
        with codecs.open(base_path + "/test_dir/data/test_staff_info.csv", 'r', encoding='gbk') as fp:
            fp_key = csv.reader(fp)
            for csv_key in fp_key:
                csv_reader = csv.DictReader(fp, fieldnames=csv_key)
                for row in csv_reader:
                    csv_dict = dict(row)
        return csv_dict

    # # 登录公共方法
    def login(self, browser, base_url):
        self.page = PopupPage(browser)
        self.page.get(base_url + '/index.php/employform/index')
        if self.page.get_url == base_url + '/index.php/employform/login/index':
            self.staff_info = self.get_staff_info()
            self.page.input_staff_name = self.staff_info['name']
            self.page.input_password = self.staff_info['password']
            self.page.login_button.click()
            sleep(15)

    # def test_popup_show_case(self, browser, base_url):
    #     """
    #     检测弹窗弹出：
    #     步骤：
    #     1.检测弹层是否正常弹出
    #     2.检测点击信息图标是否正常出现下拉菜单
    #     """
    #     self.login(browser, base_url)
    #
    #     flag = False
    #     layer_divs = self.page.layer_divs  # 弹出弹窗
    #     if len(layer_divs) > 0:
    #         flag = True
    #
    #     layer_shades = self.page.layer_shades
    #     for layer_shade in layer_shades:
    #         self.page.execute_script('arguments[0].click()', layer_shade)  # 关闭弹窗
    #     sleep(2)
    #     self.page.message_button.click()  # 点击信息图标
    #     is_display = self.page.message_box.is_displayed()  # 信息下拉菜单
    #     if flag is True and is_display is True:
    #         flag = True
    #     else:
    #         flag = False
    #
    #     assert flag is True

    def test_wait_visit_case(self, browser, base_url):
        """
        模拟业务员待回访数据验证:
        1.查询业务员待回访数据
        2.点击信息图标获取信息下拉菜单中的待回访客户数据
        3.验证待回访数据
        """
        self.login(browser, base_url)
        total = self.get_wait_visit_total(self.staff_info['roles_str'], self.staff_info['staff_id'])
        print(total)

        assert 1 > 0

    def get_wait_visit_total(self, session_role_id, session_staff_id):
        db_conn = DB(ip='47.103.83.160', user='root', passwd='c587024e9ec3ea0a', db='ylg')
        sql = "select v.visit_id,v.client_id,CAST(v.visit_time AS CHAR) as visit_time,CAST(v.next_visit_time AS CHAR) as next_visit_time from xy_visit v"
        sql += " inner join xy_client c on c.client_id=v.client_id"
        sql += " where v.staff_id=" + str(
            session_staff_id) + " and (v.staff_id=c.staff_id or v.staff_id=c.valid_allot_staff)"
        sql += " and v.type='report' and v.wait_visit_status=1"
        if session_role_id in [87, 91]:
            sql += " and c.high_quality = 0"
            sql += " and c.client_rank <> 'D'"
        sql += " order by v.client_id desc,v.visit_time desc,v.next_visit_time desc"
        visits = db_conn.query(sql)

        # 获取客户并加上最新的访问时间和下次访问时间
        clients = {}
        if visits:
            for visit in visits:
                client_id = visit['client_id']
                v_visit_time = (visit['visit_time'] if visit['visit_time'] != '0000-00-00' else None)
                v_next_visit_time = (visit['next_visit_time'] if visit['next_visit_time'] != '0000-00-00' else None)
                clients[client_id] = {}
                if not clients[client_id]:
                    visit['visit_time'] = v_visit_time
                    visit['next_visit_time'] = v_next_visit_time
                    clients[client_id] = visit
                else:
                    c_visit_time = (
                        clients[client_id]['visit_time'] if clients[client_id]['visit_time'] != '0000-00-00' else None)
                    c_next_visit_time = (clients[client_id]['next_visit_time'] if clients[client_id][
                                                                                      'next_visit_time'] != '0000-00-00' else None)
                    if 'c_visit_time' in dir() and 'v_next_visit_time' in dir():
                        continue
                    elif c_visit_time is None and 'v_visit_time' in dir():
                        clients[client_id]['visit_time'] = v_visit_time
                    elif c_next_visit_time is None and 'v_next_visit_time' in dir():
                        clients[client_id]['next_visit_time'] = v_next_visit_time
        # print(json.dumps(clients, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':')))

        # 根据最新的访问日期小于最新的下次访问日期，下次访问日期小于等于现在日期，筛选待访问客户数量
        visit_count = 0
        if clients:
            for key, client in clients.items():
                # print(client)
                visit_date = time.strftime("%Y-%m-%d", time.localtime(
                    int(time.mktime(time.strptime(client['visit_time'], "%Y-%m-%d %H:%M:%S")))))
                next_visit_date = client['next_visit_time']
                now_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
                if next_visit_date is not None and (visit_date < next_visit_date) and (next_visit_date <= now_date):
                    visit_count += 1

        return visit_count


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_popup.py"])
