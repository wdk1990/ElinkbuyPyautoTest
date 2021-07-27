"""
@author:  吴登科
@data: 2021-07-14
@function 易联购页头弹窗测试用例类
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
from page.popup_page import PopupPage
from dbConn import DB
from .base import Base


# 获取待回访客户数据
def get_wait_visit_total(role_id, staff_id):
    db_conn = DB(ip='47.103.83.160', user='root', passwd='c587024e9ec3ea0a', db='ylg')
    sql = "select v.visit_id,v.client_id,CAST(v.visit_time AS CHAR) as visit_time,CAST(v.next_visit_time AS CHAR) as next_visit_time from xy_visit v"
    sql += " inner join xy_client c on c.client_id=v.client_id"
    sql += " where v.staff_id=" + str(staff_id) + " and (v.staff_id=c.staff_id or v.staff_id=c.valid_allot_staff)"
    sql += " and v.type='report' and v.wait_visit_status=1"
    if role_id in [87, 91]:
        sql += " and c.high_quality = 0"
        sql += " and c.client_rank <> 'D'"
    sql += " order by v.client_id desc,v.visit_time desc,v.next_visit_time desc"
    visits = db_conn.query(sql)

    # 获取最近回访客户去重
    clients = []
    new_dict = {}
    new_list = []
    for visit in visits:
        if visit['client_id'] not in new_list:
            new_dict['visit_id'] = visit['visit_id']
            new_dict['client_id'] = visit['client_id']
            new_dict['visit_time'] = visit['visit_time']
            new_dict['next_visit_time'] = visit['next_visit_time']
            clients.append(new_dict)
            new_list.append(visit['client_id'])
            new_dict = {}

    # 根据最新的访问日期小于最新的下次访问日期，下次访问日期小于等于现在日期，筛选待访问客户数量
    visit_count = 0
    if clients:
        for client in clients:
            visit_date = time.strftime("%Y-%m-%d", time.localtime(int(time.mktime(time.strptime(client['visit_time'], "%Y-%m-%d %H:%M:%S")))))
            next_visit_date = client['next_visit_time']
            now_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            if next_visit_date is not None:
                if (visit_date < next_visit_date) and (next_visit_date <= now_date):
                    visit_count += 1
    return visit_count


class TestPopup(Base):
    """弹窗相关功能测试"""

    def test_popup_show_case(self, browser, base_url):
        """
        检测弹窗弹出：
        步骤：
        1.检测弹层是否正常弹出
        2.检测点击信息图标是否正常出现下拉菜单
        """
        self.login(browser, base_url)
        flag = False
        self.page = PopupPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.page.message_button.click()  # 点击信息图标
        else:
            print("弹层关闭失败")
        is_display = self.page.message_box.is_displayed()  # 信息下拉菜单
        if is_display is True:
            flag = True
        else:
            print('找不到信息框')
            flag = False
        assert flag is True

    def test_wait_visit_case(self, browser, base_url):
        """
        模拟业务员待回访弹窗数据验证:
        1.查询业务员待回访数据
        2.点击信息图标获取信息下拉菜单中的待回访客户菜单
        3.验证待回访数据
        """
        self.login(browser, base_url)
        self.user = self.get_user()
        wait_visit_total = get_wait_visit_total(self.user['roles_str'], self.user['staff_id'])
        print('待回访客户：' + str(wait_visit_total))
        sleep(2)

        self.page = PopupPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.page.message_button.click()  # 点击信息图标
        else:
            print("弹层关闭失败")

        is_display = self.page.message_box.is_displayed()  # 信息下拉菜单
        wait_visit_text = 0
        if is_display is True:
            wait_visit_text = int(self.page.wait_visit_count.text)
        else:
            print("找不到信息框")
        assert wait_visit_total == wait_visit_text
        sleep(2)

    def test_wait_visit_quality_case(self, browser, base_url):
        """
        模拟业务员待回访优质客户弹窗数据验证
        1.查询业务员待回访优质客户数据
        2.点击信息下拉框下待回访优质客户菜单
        3.验证待回访优质客户数据
        """
        self.login(browser, base_url)
        wait_visit_quality_total = 0
        self.user = self.get_user()
        if self.user['roles_str'] not in [87, 97]:
            db_conn = DB(ip='47.103.83.160', user='root', passwd='c587024e9ec3ea0a', db='ylg')
            clients = db_conn.query("select code,name,client_id,clientid,staff_id from xy_client where clientid> 0  and staff_id='" + str( self.user['staff_id']) + "'and high_quality=1")
            if clients:
                for client in clients:
                    begin_date = datetime.date.today() - relativedelta(months=+2)
                    status = db_conn.query("select visit_id from xy_visit where client_id=" + str( client['client_id']) + " and type='report' and visit_time>'" + str(begin_date) + "' limit 1")
                    if not status:
                        wait_visit_quality_total += 1
        print('待回访优质客户：' + str(wait_visit_quality_total))
        sleep(2)

        self.page = PopupPage(browser)
        flag = self.close_layer()  # 关闭弹层
        if flag:
            self.page.message_button.click()  # 点击信息图标
        else:
            print('弹层关闭失败')
        is_display = self.page.message_box.is_displayed()  # 信息下拉菜单
        wait_visit_quality_text = 0
        if is_display is True:
            wait_visit_quality_text = int(self.page.wait_visit_quality_count.text)
        else:
            print("找不到信息框")
        assert wait_visit_quality_total == wait_visit_quality_text
        sleep(2)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_popup.py"])
