import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


def run_all():
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover("./testcase", "test*.py")
    suite.addTest(testcases)
    path = os.path.abspath(".")
    api_name = "微信接口"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口接口用例执行报告")
    runner.run(suite)

run_all()