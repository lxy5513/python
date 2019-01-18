import ipdb 
#  ipdb.set_trace()
import sys 
import pprint 

from mywraps.log import Logger 

logger = Logger() 
import time

for i in range(30):
    time.sleep(1)
    logger.info('xxxx --> {} '.format(i))
