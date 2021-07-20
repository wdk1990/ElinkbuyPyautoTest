# coding=utf-8
import os
import time
import logging
import allure
import pytest
import click
import yagmail
from conftest import REPORT_DIR, zipDir
from config import RunConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py  (回归模式，生成HTML报告)
  > python run_tests.py -m debug  (调试模式)
'''


def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")


@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)
        init_env(RunConfig.NEW_REPORT)
        html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
        xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--alluredir=./temp",  # 生成allure报告临时数据目录
                     "--capture=sys",
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
        os.system('allure generate ./temp -o ./allure-2.14.0/report --clean')

        zipDir(RunConfig.NEW_REPORT, RunConfig.NEW_REPORT + '.zip')  # 压缩测试报告目录
        html_report_zip = RunConfig.NEW_REPORT + '.zip'
        yag = yagmail.SMTP(user="513411425@qq.com", password="xilwsmpslpzjbijf", host='smtp.qq.com')
        yag.send(['513411425@qq.com', '599403836@qq.com', '445140615@qq.com'], now_time + "_易联购测试报告", ["请查看附件"],
                 [html_report_zip])
        yag.close()
        print("测试报告邮件发送成功！")
        
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
