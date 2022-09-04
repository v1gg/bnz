"""
接口名称:获取标签
接口地址:https://api.weixin.qq.com/cgi-bin/tags/get?access_token=ACCESS_TOKEN
请求方式：GET

"""
import json
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import requests
import random
from ddt import ddt,data,unpack
from weixin.config.config_yaml import ConfigYaml
from weixin.comment.log import Log
config = ConfigYaml()
log = Log()


@ddt
class TestGetLabel(unittest.TestCase):
    """获取标签接口类"""

    access_token = ""
    def setUp(self):
        log.info("获取touken值")
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type":"client_credential",
            "appid":"wx0e86f42f1bf2a80d",
            "secret":"5deed6399a910c1849ac9a85f345780b"
        }
        res = requests.get(url,params=data)
        TestGetLabel.access_token = res.json()["access_token"]

    def tearDown(self):
        pass

    #@unittest.skip("暂时不想执行")
    def test_01_tags_get_labels_success(self):
        """参数填写正确"""
        log.info("开始执行用例：获取标签，参数填写正确")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/get?access_token={TestGetLabel.access_token}"
        res = requests.get(url=url)
        text = res.json()["tags"][0]["name"]
        try:
            self.assertEqual(text,"星标组")
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    def test_02_tags_get_labels_fail(self):
        """access_token参数未填"""
        log.info("开始执行用例：获取标签，access_token参数未填写")
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        res = requests.get(url=url)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,41001)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    def test_03_tags_get_labels_access_token_fail(self):
        """access_token参数填写错误"""
        log.info("开始执行用例：获取标签，access_token参数填写错误")
        url = "https://api.weixin.qq.com/cgi-bin/tags/get?access_token='asdf'"
        res = requests.get(url=url)
        text = res.json()["errcode"]
        #断言
        try:
            self.assertEqual(text,40001)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)



if __name__ == '__main__':
    #unittest.main(verbosity=2)
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(".", "test_get_label.py")
    suite.addTest(testcases)
    path = os.path.dirname(os.path.abspath("."))
    api_name = "获取标签"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口获取标签用例执行报告")
    runner.run(suite)