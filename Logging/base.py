import logging
import os 
import sys 
import logging.handlers
import datetime

# set log
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# set all.log
path_log = os.path.abspath(os.path.join(sys.path[0], './log/'))
if not(os.path.exists(path_log)):
    os.makedirs(path_log)

all_log_path = path_log + '/all.log'
rf_handle = logging.handlers.TimedRotatingFileHandler(all_log_path, when='midnight', interval=9,
                                                   backupCount=7, atTime=datetime.time(0, 0, 0, 0 ))
rf_handle.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
)

# set error.log
error_log_path = path_log + '/error.log'
f_handler = logging.FileHandler(error_log_path)
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
)
logger.addHandler(rf_handle)
logger.addHandler(f_handler)




logger.info("prediction time length")
logger.error("data already saved")

