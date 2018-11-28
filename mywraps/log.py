import logging
import os
import sys
import logging.handlers
import datetime
'''
直接作为一个包
可以调用
参数error=False时
只能用这种形式：
    logger.info()
'''
# set log
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

def Logger(error=False):
    # 如果error是true的话， 显示error信息

    # 选择当前文件价下的logs
    path_log = os.path.abspath(os.path.join(sys.path[0], './logs/'))
    if not(os.path.exists(path_log)):
        os.makedirs(path_log)

     # set all.log
    all_log_path = path_log + '/all.log'
    rf_handle = logging.handlers.TimedRotatingFileHandler(all_log_path, when='midnight', interval=9,
                                                    backupCount=7, atTime=datetime.time(0, 0, 0, 0 ))
    rf_handle.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
    )
    if not error:
        logger.addHandler(rf_handle)
        return logger

     # set error.log
    error_log_path = path_log + '/error.log'
    f_handler = logging.FileHandler(error_log_path)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
    )
    logger.addHandler(rf_handle)
    logger.addHandler(f_handler)


    # 使用形式
    #  logger.info("prediction time length")
    #  logger.error("data already saved")

    return logger

