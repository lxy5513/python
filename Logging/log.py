"""
需求：
    １. 将所有级别的所有日志写入磁盘文件中
    2. all.log文件中记录所有的日志信息　格式：日期和时间　－　日志级别　－　日志信息
    3. error.log文件中单独记录error级别以上的信息　格式为：　日期时间　－　日志级别　－　文件名[:行号]　－　日志信息
    4. 要求all.log 按时间进行日志切割

分析：
    １　要求记录所有级别的日志　因此日志器的有效level需要设置为最低级别－BEBUG;
    2   日志器需要被发送到两个不同的目的地　需要设置两个handle 两个目的地都是磁盘文件　因此两个handle都与FileHandle有关
    3　　all.log要求切割　使用logging.handles.TimedRotatingFileHandle
    4    分别设置格式器
"""
import logging
import logging.handlers
import datetime


logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# set all.log
rf_handle = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1,
                                                   backupCount=7, atTime=datetime.time(0, 0, 0,0 ))
rf_handle.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

# set error.log
f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
)

logger.addHandler(rf_handle)
logger.addHandler(f_handler)

logger.debug("This is a bebug log")
logger.info("This is a info log")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("critical message")
print("over")

logger.info("sasa", "aaaa")

