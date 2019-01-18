import sys 
import os 

# 这个是指执行python所在的路径，而不是脚本本身的路径，在不同的地方执行命令，结果不同
print('terminal\'s current path is',os.path.abspath(os.curdir))

filename = sys.argv[0]
dirname = os.path.dirname(filename)
abspath = os.path.abspath(dirname)

#  print(filename, '------', dirname)
# 这个是脚本的绝对路径
print('script abs path is ', abspath)
