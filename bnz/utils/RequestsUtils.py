# #重构
# import requests
# class Request:
#     """定义公共方法"""
#     def requests_api(self,url,data=None,params=None,headers=None,cookies=None,method="get"):
#         # global re
#         if method == "get":
#             re = requests.get(url,params=params,headers=headers,cookies=cookies)
#         elif method == "post":
#             re = requests.post(url,data=data,headers=headers,cookies=cookies)
#         code = re.status_code
#         try:
#             body = re.json()
#         except Exception as e:
#             body = re.text
#
#         res = dict()
#         res["code"] = code
#         res["body"] = body
#
#         return res
#
#     def get(self,url,**kwargs):
#         return self.requests_api(url,method="get",**kwargs)
#
#     def post(self,url,**kwargs):
#         return self.requests_api(url,method="post",**kwargs)


import requests
import json
import yaml
from InterAutoTest_W1.config.Config import ConfigYaml
config1 = ConfigYaml()
host = config1.get_conf_url()
class HttpApi():



    def send_get(self,url,header=None,body=None):
        re=requests.get(url=host+url,headers=header,params=body)
        try:
            return re.json()
        except:
            return re

    def send_post(self,url,header,body):
        if type(body)==type({}):#传入的请求体为字典类型
            if header['Content-Type']=='application/json':
                body=json.dumps(body)
            elif header['Content-Type']=='application/x-www-form-urlencoded':
                body=body
            else:
                pass#如果是其他的Content-Type类型另做处理
            re = requests.post(url=host+url,headers=header,data=body)
            try:
                return re.json()
            except:
                return re
        else:
            print('请求体错误，请更改请求体为字典类型')

    def send_delete(self,url,header,body):
        if type(body)==type({}):
            if header['Content-Type']=='application/json':
                body=json.dumps(body)
            elif header['Content-Type']=='application/x-www-form-urlencoded':
                body=body
            else:
                return {'code':'contenType error'}
            re = requests.delete(url=host+url,headers=header,data=body)
            return re.json()
        else:
            print('请求体错误，请更改请求体为字典类型')

    def send_put(self,url,header,body):
        if type(body)==type({}):
            if header['Content-Type']=='application/json':
                body=json.dumps(body)
            elif header['Content-Type']=='application/x-www-form-urlencoded':
                body=body
            else:
                pass
            re = requests.post(url=host+url,headers=header,data=body)
            try:
                return re.json()
            except:
                return re
        else:
            print('请求体错误，请更改请求体为字典类型')

    def run_main(self,send_method,url,header=None,body=None):
        if send_method == 'get':
            return self.send_get(url,header,body)
        elif send_method == 'post':
            return self.send_post(url,header,body)
        elif send_method == 'delete':
            return self.send_delete(url,header,body)
        elif send_method == 'put':
            return self.send_put(url,header,body)
        else:
            return {'code':'请求方法错误，请使用get/post/delete/put'}

if __name__ == '__main__':
    HttpApi=HttpApi()
    data = {
        "client_id":"test1",
        "client_secret":123456,
        "grant_type":"password",
        "username":1640936424877,
        "password":"uvfNt3mBZNOiyTUHczTZyQ=="
    }
    header={'Content-Type':'application/x-www-form-urlencoded'}
    res=HttpApi.run_main('post',url='/back/auth/oauth/token',header=header,body=data)
    print(res)