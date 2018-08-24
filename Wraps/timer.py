# encoding:utf-8
'''
用于测试一个函数用了多少时间
'''
from functools import wraps
import time
import pdb

def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        print('函数: {} 开始执行...'.format(function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        t = t1-t0
        if t > 3600:
            h = int(t/3600)
            m = int(t/60)
            s = t%60
            s = round(s, 2)
            timer = '{} 小时 {} 分钟 {} 秒'.format(h, m, s)
        elif t > 60:
            m = int(t/60)
            s = int(t%60)
            s = round(s, 2)
            timer = '{} 分钟 {} 秒'.format(m, s)
        else:
            t = round(t, 2)
            timer = '{} 秒'.format(t)

        # pdb.set_trace()
        print('函数: {} 结束执行, spent time: {}'.format(function.__name__, timer))
        return result
    return function_timer

@func_timer
def test(x, y):
    s = x + y
    time.sleep(61)
    print('the sum is: {0}'.format(s))


'''
后面是对于函数在执行过程中的计时器
'''
start_time = 0
def consume_time():
    end_time = time.time()
    interval = end_time - start_time
    seconds = interval
    if seconds > 60:
        minutes = int(seconds/60)
        seconds = seconds % 60
        seconds = round(seconds, 2)
        print("耗时 {} 分 {} 秒".format(minutes, seconds))
    else:
        print("耗时 {} 秒".format(round(seconds, 2)))


if __name__ == '__main__':
    test(1, 2)
    # 输出结果
    '''
    函数: test 开始执行...
    the sum is: 3
    函数: test 结束执行, spent time: 1 分钟 1 秒
    '''
