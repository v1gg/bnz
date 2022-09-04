"""
接口名称:删除标签
接口地址:https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=ACCESS_TOKEN
请求方式：post
参数实例：
{   "tag":{        "id" : 134   } }
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
data_fail = config.delete_labal_fail1()


@ddt
class TestDeleteLabel(unittest.TestCase):
    """删除标签接口类"""

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
        TestDeleteLabel.access_token = res.json()["access_token"]

    def tearDown(self):
        pass

    #@unittest.skip("暂时不想执行")
    def test_01_tags_delete_labels_success(self):
        """参数填写正确"""
        log.info("开始执行用例：获取标签，参数填写正确")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/delete?access_token={TestDeleteLabel.access_token}"
        data = {
            "tag": {"id":124}
        }
        data=json.dumps(data)
        res = requests.post(url=url,data=data)
        print(res.json())
        text = res.json()["errmsg"]
        try:
            self.assertEqual(text,"ok")
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    def test_02_tags_delete_labels_fail(self):
        """access_token参数未填"""
        log.info("开始执行用例：删除标签标签，access_token参数未填")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=''"
        data = {
            "tag": {"id":124}
        }
        data=json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,40001)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    def test_03_tags_delete_labels_access_token_fail(self):
        """access_token参数填写错误"""
        log.info("开始执行用例：删除标签，access_token参数填写错误")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/delete?access_token='adf'"
        data = {
            "tag": {"id":124}
        }
        data=json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,40001)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    @data(*data_fail)
    @unpack
    def test_04_tags_delete_labels_parament_error(self,id,code):
        """参数填写错误"""
        log.info("开始执行用例：删除标签标签，参数填写错误")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/delete?access_token={TestDeleteLabel.access_token}"
        data = {
            "tag": {"id":id}
        }
        data=json.dumps(data)
        res = requests.post(url=url,data=data)
        print(res.json())
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,code)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)


if __name__ == '__main__':
    #unittest.main(verbosity=2)
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(".", "test_delete_label.py")
    suite.addTest(testcases)
    path = os.path.dirname(os.path.abspath("."))
    api_name = "删除标签"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口删除标签用例执行报告")
    runner.run(suite)