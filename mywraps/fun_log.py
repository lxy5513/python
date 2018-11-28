#! encoding:utf-8
'''
通过在函数名上加装饰器的方法记录日志
用于记录日志， 可以指定函数名称
'''
from functools import wraps
import os

def func_log(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 获取当前路径（文件的绝对路径）
            P = os.path.abspath(__file__).split('/')[:-1]
            path = '/'.join(P)
            PATH = path + '/log/{}'.format(logfile)
            P_dir = PATH.split('/')[:-1]
            PATH_dir = '/'.join(P_dir)
            if not PATH_dir:
                os.makedirs(PATH_dir)

            # Open the logfile and append
            with open(PATH, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
        return wrapped_function
    return logging_decorator

@func_log()
def myfunc1():
    pass
if __name__ == '__main__':
    myfunc1()
    # Output: myfunc1 was called
    # A file called out.log now exists, with the above string

    @func_log(logfile='func2.log')
    def myfunc2():
        pass

    myfunc2()
    # Output: myfunc2 was called
    # A file called func2.log now exists, with the above string
