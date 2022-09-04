import os
import yaml

#1、创建类
class YamlReader:

    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileExistsError("文件不存在")
        self._data = None
        self._data_all = None
    def data(self):
        """读取单个yaml文件"""
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
            return self._data

    def data_all(self):
        """读取多个yaml文件"""
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
            return self._data_all