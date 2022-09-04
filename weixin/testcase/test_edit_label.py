"""
接口名称:编辑标签
接口地址: https://api.weixin.qq.com/cgi-bin/tags/update?access_token=ACCESS_TOKEN
请求方式：post
POST数据格式：JSON POST数据示例
{   "tag" : {     "id" : 134,     "name" : "广东人"   } }
参数说明:
access_token:调用接口凭据
id:需要编辑标签的id
name:修改id的名称
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
data_fail = config.edit_labal_fail1()
data_sueecss = config.edit_labal_sueccess()

@ddt
class TestEditLabel(unittest.TestCase):
    """编辑标签接口类"""

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
        TestEditLabel.access_token = res.json()["access_token"]

    def tearDown(self):
        pass

    #@unittest.skip("暂时不想执行")
    def test_01_tags_edit_label_success(self):
        """参数填写正确"""
        log.info("开始执行用例：编辑标签，参数填写正确")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/update?access_token={TestEditLabel.access_token}"
        num = random.randint(1,100000)
        name = "广西老表"+str(num)
        data = {
            "tag":{
                "id":101,"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errmsg"]
        try:
            self.assertEqual(text,"ok")
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)


    #@unittest.skip("暂时不想执行")
    def test_02_tags_edit_label_access_token_not(self):
        """access_token未填写"""
        log.info("开始执行用例：编辑标签，access_token参数未填写")
        url ="https://api.weixin.qq.com/cgi-bin/tags/update?access_token=''"
        num = random.randint(1,100000)
        name = "广西老表"+str(num)
        data = {
            "tag":{
                "id":101,"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,40001)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    @unittest.skip("暂时不想执行")
    def test_03_tags_edit_label_access_token_error(self):
        """access_token填写错误"""
        log.info("开始执行用例：编辑标签，access_token参数未填写")
        url ="https://api.weixin.qq.com/cgi-bin/tags/update?access_token='asdf'"
        num = random.randint(1,100000)
        name = "广西老表"+str(num)
        data = {
            "tag":{
                "id":101,"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        try:
            self.assertEqual(text,40001)
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    @data(*data_sueecss)
    @unpack
    def test_04_tags_edit_label_parameter_success(self,id,name):
        """参数正确"""
        log.info("开始执行用例：编辑标签，参数填写正确")
        url = f"https://api.weixin.qq.com/cgi-bin/tags/update?access_token={TestEditLabel.access_token}"
        data = {
            "tag":{
                "id":id,"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errmsg"]
        print(text)
        try:
            self.assertEqual(text,"ok")
            log.info("返回数据正确，返回结果%s"%text)
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    @data(*data_fail)
    @unpack
    def test_05_tags_edit_label_parameter_error(self,id,name,code):
        """参数填写错误"""
        url = f"https://api.weixin.qq.com/cgi-bin/tags/update?access_token={TestEditLabel.access_token}"
        data = {
            "tag":{
                "id":id,"name":name}
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
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
    testcases = unittest.defaultTestLoader.discover(".", "test_edit_label.py")
    suite.addTest(testcases)
    path = os.path.dirname(os.path.abspath("."))
    api_name = "编辑标签"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口编辑标签用例执行报告")
    runner.run(suite)