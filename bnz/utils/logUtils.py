import logging.handlers
import os
import time
from bnz.config.Config import ConfigYaml
#定义日志级别映射
log_l= {
    "debug":logging.DEBUG,
    "info":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR,
}
class Log:
    """日志类"""
    def __init__(self,log_name,log_level):
        """
        定义参数
        :param log_name: logger名称
        :param log_level: 日志级别
        """
        self.log_name = log_name
        self.log_level = log_level
        #1、设置logger名称
        self.logger = logging.getLogger(self.log_name)
        #2、设置log级别
        self.logger.setLevel(log_l[self.log_level])


    def __console(self,log_level, message):

        #创建一个handler，用于写入日志文件
        rq = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'
        #获取处理器 控制台
        sh = logging.StreamHandler()
        th = logging.handlers.TimedRotatingFileHandler(filename=log_name,
                                                       when="midnight",
                                                       interval=1,
                                                       backupCount=30,
                                                       encoding="utf-8")
        #设置格式器
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - %(message)s"
        fm = logging.Formatter(fmt)

        #将格式器添加到处理器控制台
        sh.setFormatter(fm)
        th.setFormatter(fm)

        #将处理器添加到日志器
        self.logger.addHandler(sh)
        self.logger.addHandler(th)
        if log_level == 'info':
            self.logger.info(message)
        elif log_level == 'debug':
            self.logger.debug(message)
        elif log_level == 'warning':
            self.logger.warning(message)
        elif log_level == 'error':
            self.logger.error(message)
            # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(sh)
        self.logger.removeHandler(th)
        # 关闭打开的文件
        th.close()
    def debug(self, message):
        self.__console("debug",message)
    def info(self, message):
        self.__console("info",message)
    def warning(self, message):
        self.__console("warning",message)
    def error(self, message):
        self.__console("error",message)

log_level = ConfigYaml().get_conf_log()

def log(log_name=__file__):
    return Log(log_name=log_name,log_level=log_level)


if __name__ == '__main__':
    log = log("v1")
    log.info("这是一个info")
    log.warning("这是一个warning")