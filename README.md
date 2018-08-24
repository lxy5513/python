## 用来保存长久性的 公用的程序

## 执行方法
> from log import func_log  
> from timer import func_timer  
> from timeout import timeout  


> @func_log('import_log')  
def test_log():  
    print('log')  


> @func_timer  
def test_timer():  
    import time  
    time.sleep(3)  
    print('timer over')  



> @timeout(3)  
def test_timeout():  
    import time  
    print('time start...')  
    time.sleep(4)  
    print('time over ...')
