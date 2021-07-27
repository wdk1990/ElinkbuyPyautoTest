"""
@author:  吴登科
@data: 2021-07-27
@function 易联购客户相关测试用例类
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
from page.customer import CustomerPage
from dbConn import DB
from .base import Base


class TestCustomer(Base):
    """客户相关功能测试"""



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_customer.py"])
