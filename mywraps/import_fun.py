'''
实验几个函数导入的功能与效果
'''
import log
from timeout import timeout
from timer import timer, consume_time
import time

start_time = time.time()

# 测试函数耗时
@timer
def test_fun1():
    print('用装饰器来测试函数运行时间...')
    time.sleep(4)

# 限制函数运行不能超过多久
@timeout(2)
def Time_out():
    print('函数运行时间不能超过2秒')
    time.sleep(3)

if __name__ == '__main__':
    # 测试日志记录
    loger = log.Logger(error=False)
    loger.info('记录日志')

    test_fun1()

    # 测试目前为程序耗时
    time.sleep(2)
    print('程序总共运行时间。。。')
    consume_time(start_time)
    
    Time_out()


