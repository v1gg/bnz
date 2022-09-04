"""
接口名称:获取token
接口地址:https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
请求方式：get
参数说明:
grant_type:获取access_token填写client_credential
appid:第三方用户唯一凭证
secret:第三方用户唯一凭证密钥，即appsecret
"""
import os
import time
from HTMLTestRunner import HTMLTestRunner
from weixin.comment.log import Log
import requests
import unittest
from ddt import ddt,data,unpack
from weixin.config.config_yaml import ConfigYaml
config = ConfigYaml()
yaml_data = config.get_token()
yaml_data1 = config.get_token1()
log = Log()

@ddt
class testToken(unittest.TestCase):
    """获取token测试类"""

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_01_param_fill_in(self):
        """所有接口参数都填写正确"""
        log.info("开始执行接口用例：所有接口参数都填写正确")
        appID = "wx0e86f42f1bf2a80d"
        appsecret = "5deed6399a910c1849ac9a85f345780b"
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(appID,appsecret)
        res = requests.get(url)
        #断言
        try:
            text = res.json()["expires_in"]
            self.assertEqual(text,7200)
            log.info("断言成功")
        except Exception as e:
            print(e)
            log.info("获取token请求接口失败")

    @data(*yaml_data)
    @unpack
    def test_02_param_required(self,grant_type,appID,appsecret,code):
        """一个参数未填写"""
        log.info("开始执行接口用例：一个参数未填写")
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=%s&appid=%s&secret=%s"%(grant_type,appID,appsecret)
        res = requests.get(url)
        #断言
        try:
            text = res.json()["errcode"]
            self.assertEqual(text,code)
            log.info("断言成功")
        except Exception as e:
            print(e)
            log.info("断言失败")

    @data(*yaml_data1)
    @unpack
    def test_03_param_required1(self,grant_type,appID,appsecret,code):
        """一个参数填写错误"""
        log.info("一个参数填写错误")
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=%s&appid=%s&secret=%s"%(grant_type,appID,appsecret)
        res = requests.get(url)
        #断言

        try:
            text = res.json()["errcode"]
            self.assertEqual(text,code)
            log.info("断言成功")
        except Exception as e:
            print(e)
            log.info("断言失败")


if __name__ == "__main__":

    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(".", "test_token.py")
    suite.addTest(testcases)
    path = os.path.dirname(os.path.abspath("."))
    api_name = "获取token"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口获取token接口用例执行报告")
    runner.run(suite)