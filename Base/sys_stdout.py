'''
一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。

flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。

正常情况下缓冲区满时，操作系统会自动将缓冲数据写入到文件中。
'''
import sys 
import time
for i in range(5):
    print('repeat') 
    sys.stdout.flush()
    time.sleep(1)
