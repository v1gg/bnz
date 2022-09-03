import os
import unittest
from bnz.common.yml_data import YamlUtil
from bnz.common.yaml_data_bnz import get_yaml_data
from ddt import ddt,data,unpack
import requests

# current_path = os.path.abspath("../data")  #返回当前目录所在的绝对路径
# yaml_path = os.path.join(current_path, "get_token_bnz.yaml")  #返回当前目录下的“config.yaml”文件所在的绝对路径
text = YamlUtil().read_yaml_data('\get_token_bnz.yaml')
print(text)


@ddt
class TestToken(unittest.TestCase):
    """token类"""

    @unittest.skip('暂不执行')
    def test_token(self):
        """获取token，所有参数必填"""
        url = 'https://dev.bnzedu.com/back/auth/oauth/token'
        data = {
            "client_id": "test1",
            "client_secret": "123456",
            "grant_type": "password",
            "username": "1655445717373",
            "password": "uvfNt3mBZNOiyTUHczTZyQ=="
        }
        rep = requests.request('post',url,data=data)
        # 断言响应状态码200
        self.assertEqual(rep.status_code,200)
        # 获取账号信息
        text = rep.json()['userName']
        self.assertEqual('1655445717373',text)
        print(rep.json())

    #@unittest.skip('暂不执行')
    @data(*text)
    @unpack
    def test_params_mandatory(self,client_id,client_secret,grant_type,username,password):
        """参数是否必填"""

        url = 'https://dev.bnzedu.com/back/auth/oauth/token'
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "username": username,
            "password": password
        }
        rep = requests.request('post', url, data=data)
        print(rep.json())

if __name__ == '__main__':
    unittest.main()