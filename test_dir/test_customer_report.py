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
from page.offer_page import OfferPage

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)

from dbConn import DB
from .base import Base


class TestCustomerReport(Base):
    """ 客户报备相关测试用例类"""

    def test_report_case(self):
        """
        模拟业务员报备客户:
        1.点击顶级菜单报备报价合同下客户报备菜单
        2.验证是否正常跳转到客户报备列表页
        3.
        """
