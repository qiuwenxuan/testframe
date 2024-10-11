# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: main.py
# @Time: 2021/3/12 19:59
# @Author: sun
import unittest
import os
import time
from Comm.email import Email
from Comm.log import LOGGER
from conf.config import CASE_DIR, REPORT_DIR
from BeautifulReport import BeautifulReport


def summary_format(result):
    summary = "\n" + u"<p>          测试结果汇总信息                </p>" + "\n" + \
                 u"<p> 开始时间: " + result['beginTime'] + u" </p>" + "\n" + \
                 u"<p> 运行时间: " + result['totalTime'] + u" </p>" + "\n" + \
                 u"<p> 执行用例数: " + str(result['testAll']) + u" </p>" + "\n" + \
                 u"<p> 通过用例数: " + str(result['testPass']) + u" </p>" + "\n" + \
                 u"<p> 失败用例数: " + str(result['testFail']) + u" </p>" + "\n" + \
                 u"<p> 忽略用例数: " + str(result['testSkip']) + u" </p>" + "\n"
    return summary


def send_email(file, context):
    LOGGER.info("Send mail")
    title = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '自动化测试结果'
    mail = Email(title, context, file)
    send = mail.send_mail()
    if send:
        print('测试报告邮件发送成功')
    else:
        print('测试报告邮件发送失败')


def get_suite(case_dir=CASE_DIR, rule="test_*.py"):
    """加载所有的测试用例"""
    LOGGER.info("Discover testcase")
    unittest_suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern=rule, top_level_dir=None)
    for each in discover:
        unittest_suite.addTests(each)
    LOGGER.info("All test cases: %s" % unittest_suite._tests)
    return unittest_suite


def suite_run(unittest_suite):
    """执行所有的用例, 并把结果写入测试报告"""
    LOGGER.info("Start test")
    run_result = BeautifulReport(unittest_suite)

    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = now + '_report.html'
    run_result.report(filename=filename, description=now, report_dir=REPORT_DIR)
    rpt_summary = summary_format(run_result.fields)
    return os.path.join(REPORT_DIR, filename), rpt_summary


if __name__ == "__main__":
    suite = get_suite()
    report_file, report_summary = suite_run(suite)
    print(report_summary)
    send_email(report_file, report_summary)
