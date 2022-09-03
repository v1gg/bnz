import yaml
import os



def get_yaml_data(yaml_path):
    # 打开yaml文件
    f = open(yaml_path, "r", encoding="utf-8")  # 以读权限获取yaml文件对象
    res = yaml.load(f, Loader=yaml.FullLoader)  # 获取yaml文件中的数据(不包含注释的内容)
    f.close()  # 关闭文件
    return res  # 打印获取到的数据

if __name__ == "__main__":
    current_path = os.path.abspath("../data")  #返回当前目录所在的绝对路径
    yaml_path = os.path.join(current_path, "test.yaml")  #返回当前目录下的“config.yaml”文件所在的绝对路径
    res = get_yaml_data(yaml_path)
    print(res)