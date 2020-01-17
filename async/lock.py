from threading import Thread, Lock
import time

mutex1= Lock()

mutex2= Lock()

mutex3= Lock()


def fun1():
    while 1:
        mutex1.acquire()  # 阻塞
        print("线程1 执行")
        mutex2.release()   # 释放锁2，让线程2继续执行
        time.sleep(0.1)

def fun2():
    while 1:
        mutex2.acquire()  # 阻塞
        print("线程2 执行")
        mutex3.release()   # 释放锁3，让线程3继续执行
        time.sleep(0.1)

def fun3():

    while 1:
        mutex3.acquire()  # 阻塞
        print("线程3 执行")
        mutex1.release()   # 释放锁1，让线程1继续执行
        time.sleep(0.1)

 

t1 =Thread(target=fun1)  # 创建一个线程对象
t2 =Thread(target=fun2)  # 创建一个线程对象
t3 =Thread(target=fun3)  # 创建一个线程对象

 
mutex2.acquire()  # 将锁2设置为上锁，线程2不能运行
mutex3.acquire()  # 将锁2设置为上锁，线程2不能运行
 
t1.start()  # 开启线程的执行
t2.start()
t3.start()

t1.join()  # 回收线程资源
t2.join()
t3.join()
