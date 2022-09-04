import os
from weixin.utils.utils_yaml import YamlReader
#1、获取项目基本目录
#获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
#定义Config目录路径
_data_path = BASE_DIR + os.sep +"data"
#定义config.yaml文件的路径

_token_data_file = _data_path + os.sep + "token_data.yaml"
_token_data_file1 = _data_path + os.sep + "token_data1.yaml"
_create_labal_fail1 = _data_path + os.sep + "create_labal_fail1.yaml"
_create_labal_success= _data_path + os.sep + "create_labal_success.yaml"
_edit_labal_fail1 = _data_path + os.sep + "edit_data_fail1.yaml"
_edit_labal_sueccess= _data_path + os.sep + "edit_data_sueccess.yaml"
_delete_labal_fail1= _data_path + os.sep + "delete_data_fail1.yaml"
_modify_comments_data_fail1= _data_path + os.sep + "modify_comments_data_fail1.yaml"
_modify_comments_data_success= _data_path + os.sep + "modify_comments_data_success.yaml"

def get_data_path():
    return _data_path
def get_token_file():
    return _token_data_file
def get_token_file1():
    return _token_data_file1
def create_labal_fail1():
    return _create_labal_fail1
def create_labal_success():
    return _create_labal_success
def edit_labal_fail1():
    return _edit_labal_fail1
def edit_labal_sueccess():
    return _edit_labal_sueccess
def delete_label_fail1():
    return _delete_labal_fail1
def modify_comments_data_fail1():
    return _modify_comments_data_fail1
def modify_comments_data_success():
    return _modify_comments_data_success
#读取配置文件
#创建类
class ConfigYaml:

    #初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_token_file()).data_all()
        self.config1 = YamlReader(get_token_file1()).data_all()
        self.config2 = YamlReader(create_labal_fail1()).data_all()
        self.config3 = YamlReader(create_labal_success()).data_all()
        self.config4 = YamlReader(edit_labal_fail1()).data_all()
        self.config5 = YamlReader(edit_labal_sueccess()).data_all()
        self.config6 = YamlReader(delete_label_fail1()).data_all()
        self.config7 = YamlReader(modify_comments_data_fail1()).data_all()
        self.config8 = YamlReader(modify_comments_data_success()).data_all()


    def get_token(self):
        return self.config

    def get_token1(self):
        return self.config1

    def create_labal_fail1(self):
        return self.config2

    def create_labal_success(self):
        return self.config3

    def edit_labal_fail1(self):
        return self.config4

    def edit_labal_sueccess(self):
        return self.config5

    def delete_labal_fail1(self):
        return self.config6
    def modify_comments_data_fail1(self):
        return self.config7
    def modify_comments_data_success(self):
        return self.config8

if __name__ == '__main__':
    config = ConfigYaml()
    text = config.get_token()
    text1 = config.get_token1()
    text2 = config.create_labal_fail1()
    text3 = config.create_labal_success()
    text4 = config.edit_labal_fail1()
    text5 = config.edit_labal_sueccess()
    text6 = config.delete_labal_fail1()
    text7 = config.modify_comments_data_fail1()
    text8 = config.modify_comments_data_success()
    print(text8)

