"""
@author:  吴登科
@data: 2021-07-27
@function 易联购客户相关测试用例类
"""
import sys
import time
import pytest
import datetime
from time import sleep
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)

from dbConn import DB
from .base import Base


class TestOffer(Base):
    """
    模拟业务原给指定客户报价操作
    """

