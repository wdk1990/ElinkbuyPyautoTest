"""
@author:  zzz
@data: 2021-08-04
@function 易联购数据统计类页面是否正常
"""
import sys
import pytest
from time import sleep
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from .base import Base
from page.data_page import DataPage
from page.common import Common


class TestData(Base):
    """数据统计"""

    # 登录操作
    def login(self, browser, base_url):
        self.common = Common(browser)
        self.common.get(base_url + '/index.php/employform/index')
        if self.common.get_url == base_url + '/index.php/employform/login/index':
            self.common.input_staff_name = '陈旭标'
            self.common.input_password = 'sh987654'
            self.common.login_button.click()
        sleep(15)

    def data(self):
        page_info = {
            # "fsc_link": "全部客户反馈统计-北京易联购科技有限公司",
            # "fsci_link": "客户反馈统计-北京易联购科技有限公司",
            # "fsq_link": "问题类型统计-北京易联购科技有限公司",
            # "fsb_link": "全部客户反馈次数统计-北京易联购科技有限公司",
            # "fsbi_link": "客户反馈次数统计-北京易联购科技有限公司",
            # "fsr_link": "全部责任人反馈类型统计-北京易联购科技有限公司",
            # "fsri_link": "责任人反馈类型统计-北京易联购科技有限公司",
            #
            # 'gsi_link': "热销产品统计-北京易联购科技有限公司",
            # 'gss_link': "正式订单产品统计-北京易联购科技有限公司",
            # 'gsg_link': "新产品销售排行设置-北京易联购科技有限公司",

            "vsc_link": "全部回访数/回头率客户统计-北京易联购科技有限公司",
            "vsci_link": "回访数/回头率客户统计-北京易联购科技有限公司",
            "vsi_link": "全部新客户有效回访统计-北京易联购科技有限公司",
            "vsa_link": "新客户有效回访统计-北京易联购科技有限公司",
            "vsr_link": "全部公共池客户有效回访统计-北京易联购科技有限公司",
            "vsal_link": "公共池客户有效回访统计-北京易联购科技有限公司",
            "vsp_link": "全部客户回访率统计-北京易联购科技有限公司",
            "vsall_link": "客户回访率统计-北京易联购科技有限公司",
            "vsvr_link": "客户行业统计-北京易联购科技有限公司",
            "vsav_link": "24小时分配回访率统计-北京易联购科技有限公司",
            "vsm_link": "维护客服回访统计-北京易联购科技有限公司",
            "vsb_link": "客户回访与订单回购统计-北京易联购科技有限公司",
            "vsmr_link": "客服有效回访奖励统计-北京易联购科技有限公司",
            "vsn_link": "维护客服回访效果统计-北京易联购科技有限公司",
            "vsrr_link": "维护客服回访回头率-北京易联购科技有限公司",
            "vsrv_link": "报备回访统计-北京易联购科技有限公司",
            "vsq_link": "优质客户回访统计-北京易联购科技有限公司",

        }
        return page_info

    def test_feedback_clerkIndex(self, browser, base_url):
        """
           名称：数据统计
                    -全部客户反馈类型统计
                    -客户反馈类型统计
                    -问题类型统计
                    -全部客户反馈次数统计
                    -客户反馈次数统计
                    -全部责任人反馈类型统计
                    -责任人反馈类型统计
           检查点：
           * 能否正常打开
         """
        page = DataPage(browser)
        self.login(browser, base_url)

        self.close_layer()

        page.data_link.click()
        sleep(5)
        self.close_layer()

        data = self.data()

        for k, v in data.items():
            str = "page." + k + ".click() "
            exec(str)
        
            handles = browser.window_handles  # 获取当前浏览器的所有窗口句柄
            page.switch_to_window(handles[-1])  # 切换到最新的窗口
            assert browser.title == v
            sleep(2)
            page.switch_to_window(handles[0])
            # js = 'document.getElementByclassName("ui-sortable").scrollLeft=500'
            # page.execute_script(js)
            # sleep(2)


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_data_statistics.py"])
