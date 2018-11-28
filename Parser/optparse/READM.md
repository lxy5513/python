## 用于在terminal添加参数

```python
from optparse import OptionParser 
parser = OptionParser()
parser.add_option()
...
options,_ = parser.parse_args()
options.dest_name 
```



### action 参数

action参数告诉 optparse该做什么 当它在 命令行中遇到选项是。action有三种存储方式： store store_false store_true 。如果不指定action的值，默认是store，它告诉optparse将继续读取下一个参数（type）。

并将它将值存储在一个变量（dest）中，即将命令行中输入的字符串将它存为options的属性

```python
### dest相同的时候，相当于设定一个bool值
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose")
```

这样的话，当解析到 ‘-v’，options.verbose 将被赋予 True 值，反之，解析到 ‘-q’，会被赋予 False 值。



### type参数

默认是string 也可以是其他的Int和 float等 



### dest参数   用来调用属性

dest 的值将作为parser的属性被存储

> parser.add_option("-f", "--file",action="store", type="string", dest="filename")

当调用options.filename时其实就是命令行接收到 文件名的值。 



### default 参数

设置默认值之后，当从命令行没有接收到参数的是选取默认值。 



### help 参数

对定义的命令参数做一个解释。提供给使用者一个帮助信息，能够让使用者更加明白你这个参数的用法，具体是做什么的。


