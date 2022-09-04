"""
接口名称:修改备注名
接口地址:https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token=ACCESS_TOKEN
请求方式：post
POST数据格式：JSON POST数据示例
{
	"openid":"oDF3iY9ffA-hqb2vVvbr7qxf6A0Q",
	"remark":"pangzi"
}
参数说明:
access_token:调用接口凭据
openid：用户标识
remark:新的备注名，长度必须小于30字节
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
data_fail = config.modify_comments_data_fail1()
data_success = config.modify_comments_data_success()

@ddt
class ModifyComments(unittest.TestCase):
    """修改备注名接口类"""

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
        ModifyComments.access_token = res.json()["access_token"]

    def tearDown(self):
        pass

    #@unittest.skip("暂时不想执行")
    def test_01_modify_comments_correct_filling(self):
        """修改备注名，参数填写正确"""
        log.info("开始执行用例：修改备注名，参数填写正确")
        url = f"https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token={ModifyComments.access_token}"
        data = {
            "openid":"oKBO_6q-Wp5PAS6HLsZFV0COAHs0",
            "remark":"蛇皮1"
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errmsg"]
        #断言
        try:
            self.assertEqual(text,"ok")
            log.info("接口返回数据正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    def test_02_modify_comments_access_token_parameter_not_filled(self):
        """access_token参数未填"""
        log.info("开始执行用例：修改备注名，access_token参数未填")
        url = f"https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token=''"
        data = {
            "openid":"oKBO_6q-Wp5PAS6HLsZFV0COAHs0",
            "remark":"蛇皮1"
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        #断言
        try:
            self.assertEqual(text,40001)
            log.info("接口返回数据正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    #@unittest.skip("暂时不想执行")
    def test_03_modify_comments_access_token_parameter_filling_error(self):
        """access_token参数填写错误"""
        log.info("开始执行用例：修改备注名，access_token参数填写错误")
        url = f"https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token='saf'"
        data = {
            "openid":"oKBO_6q-Wp5PAS6HLsZFV0COAHs0",
            "remark":"蛇皮1"
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        print(res.json())
        text = res.json()["errcode"]
        #断言
        try:
            self.assertEqual(text,40001)
            log.info("接口返回数据正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

    @data(*data_fail)
    @unpack
    def test_04_modify_comments_parameter_error(self,openid,remark,code):
        """修改备注名，openid,remark参数填写错误"""
        log.info("开始执行用例：修改备注名，openid,remark参数填写错误")
        url = f"https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token={ModifyComments.access_token}"
        data = {
            "openid":openid,
            "remark":remark
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errcode"]
        #断言
        try:
            self.assertEqual(text,code)
            log.info("接口返回数据正确")
        except Exception as e:
            print(e)
            print("修改备注名接口请求失败")

    @data(*data_success)
    @unpack
    def test_05_modify_comments_parameter_success(self,remark):
        """修改备注名，openid,remark参数填写正确"""
        log.info("开始执行用例：修改备注名，openid,remark参数填写正确")
        url = f"https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token={ModifyComments.access_token}"
        data = {
            "openid":"oKBO_6q-Wp5PAS6HLsZFV0COAHs0",
            "remark":remark
        }
        data = json.dumps(data)
        res = requests.post(url=url,data=data)
        text = res.json()["errmsg"]
        #断言
        try:
            self.assertEqual(text,"ok")
            log.info("接口返回数据正确")
        except Exception as e:
            print("断言失败，错误信息%s"%e)
            log.info("接口返回数据错误，错误内容%s"%e)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(".", "test_modify_comments.py")
    suite.addTest(testcases)
    path = os.path.dirname(os.path.abspath("."))
    api_name = "修改备注名"
    file_name = path + os.sep + "/report/" + api_name + nowtime + "_report.html"
    name = open(file_name, "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="微信接口修改备注名用例执行报告")
    runner.run(suite)