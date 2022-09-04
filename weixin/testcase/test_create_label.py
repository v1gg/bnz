"""
接口名称:创建标签
接口地址:https://api.weixin.qq.com/cgi-bin/tags/create?access_token=ACCESS_TOKEN
请求方式：post
POST数据格式：JSON POST数据示例
{   "tag" : {     "name" : "广东"//标签名   } }
参数说明:
access_token:调用接口凭据
name:标签名（30个字符以内）
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
data_fail = config.create_labal_fail1()
data_sueecss = config.create_labal_success()

@ddt
class TestCreateLabel(unittest.TestCase):
    """分组管理接口类"""

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
        TestCreateLabel.access_token = res.json()["access_token"]

    def tearDown(self):
        pass

    #@unittest.skip("暂时不想执行")
    def test_01_tags_create_correct_filling(self):
        """参数填写正确"""
        log.info("开始执行用例：创建标签，参数填写正确")
        url = f" https://api.weixin.qq.com/cgi-bin/tags/create?access_token={TestCreateLabel.access_token}"
        num = random.randint(1,100000)
        name = "广西老表"+str(num)
        data = {
            "tag":{"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["tag"]["name"]
        utf8_text= text.encode("utf-8").decode("unicode_escape")
        #断言
        try:
            self.assertEqual(utf8_text,name)
            log.info("返回数据正确，返回结果%s"%utf8_text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    @data(*data_sueecss)
    @unpack
    def test_02_tags_create_correct_filling(self,name):
        """参数填写正确(name长度边界)"""
        log.info("开始执行用例：创建标签参数填写正确，name字符长度正确")
        url = f" https://api.weixin.qq.com/cgi-bin/tags/create?access_token={TestCreateLabel.access_token}"
        data = {
            "tag":{"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        print(res.json())
        text = res.json()["tag"]["name"]
        utf8_text= text.encode("utf-8").decode("unicode_escape")
        #断言
        try:
            self.assertEqual(utf8_text,name)
            log.info("接口数据返回正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s")


    #@unittest.skip("暂时不想执行")
    def test_02_tags_create_access_token_parameter_not_filled(self):
        """access_token参数未填"""
        log.info("开始执行用例：创建标签，access_token参数未填")
        url = " https://api.weixin.qq.com/cgi-bin/tags/create?access_token=''"
        num = random.randint(1,100000)
        name = "广西老表"+str(num)
        data = {
            "tag":{"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,40001)
            log.info("接口返回数据正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    @data(*data_fail)
    @unpack
    def test_03_tags_create_name_parameter_not_filled(self,name,code):
        """name参数填写错误"""
        log.info("开始执行用例：name参数填写错误")
        url = f" https://api.weixin.qq.com/cgi-bin/tags/create?access_token={TestCreateLabel.access_token}"
        data = {
            "tag":{"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,code)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    def test_04_tags_create_access_token_parameter_filling_error(self):
        """access_token参数填写错误"""
        log.info("开始执行用例：access_token参数填写错误")
        url = f" https://api.weixin.qq.com/cgi-bin/tags/create?access_token='asfsf12'"
        num = random.randint(1,100000)
        name = "广西老表"+str(num)
        data = {
            "tag":{"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,40001)
            log.info("接口返回数据正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)



if __name__ == '__main__':
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(".", "test_create_label.py")
    suite.addTest(testcases)
    path = os.path.dirname(os.path.abspath("."))
    api_name = "创建标签"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口创建标签用例执行报告")
    runner.run(suite)