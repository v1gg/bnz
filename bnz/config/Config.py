import os
from bnz.utils.YamlUtil import YamlReader
#1、获取项目基本目录
#获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
#定义Config目录路径
_config_path = BASE_DIR + os.sep +"config"
#定义config.yaml文件的路径
_config_file = _config_path + os.sep + "config.yaml"
def get_config_path():
    return _config_path

def get_config_file():
    return _config_file


#读取配置文件
#创建类
class ConfigYaml:

#初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

    def get_conf_url(self):
        return self.config["BASE"]["test"]["host"]

    def get_conf_log(self):
        return self.config["BASE"]["log_level"]

if __name__ == '__main__':
    config = ConfigYaml()
    text = config.get_conf_log()
    print(text)