import json
import os
import yaml
# path = os.path.abspath('../data')
# print(path)

class YamlUtil:

    def read_yaml_data(self,yaml_name):
        """读取测试用例yaml文件"""
        with open(os.path.abspath('../data')+yaml_name,mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def get_yaml_data(self,yaml_name):
        # 打开yaml文件
        f = open(os.path.abspath('../data')+yaml_name, "r", encoding="utf-8")  # 以读权限获取yaml文件对象
        value = yaml.load(f, Loader=yaml.FullLoader)  # 获取yaml文件中的数据(不包含注释的内容)
        f.close()  # 关闭文件
        return value # 打印获取到的数据

if __name__ == '__main__':
    a = YamlUtil()
    text = a.read_yaml_data('\get_token_bnz.yaml')
    print(text,type(text))
    # current_path = os.path.abspath("../data")  # 返回当前目录所在的绝对路径
    # yaml_path = os.path.join(current_path, "test.yaml")  # 返回当前目录下的“config.yaml”文件所在的绝对路径
    # res = YamlUtil().get_yaml_data('\\get_token_bnz.yaml')
    # print(res)