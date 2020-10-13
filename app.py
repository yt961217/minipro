import logging.handlers
import os


def log_conf():
    """初始化日志"""
    # 日志文件位置
    logPath = './log'

    # 日志器
    logger = logging.getLogger()

    # 设置日志级别
    logger.setLevel(logging.INFO)

    # 处理器
    sh = logging.StreamHandler()  # 控制台
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logPath + os.sep + 'mini.long',
                                                     when='midnight', interval=1, backupCount=7,
                                                     encoding='utf-8')
    # 格式化字符串
    f = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 格式化器
    formatter = logging.Formatter(f)

    # 处理器添加格式化器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)

    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 基础路径
base_url = 'http://e.cn/api/v1'

# 微信code
code = '0311fp000KHYrK18TN30097Cic21fp0p'

# 请求头
headers = {"Content-Type": "application/json",
           "token": "0cdaf2949a078c65fc13f5f6c6f89fbf"}
