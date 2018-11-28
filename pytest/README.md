## pytest function 
执行pytest命令，pytest将运行当前目录及其子目录下所有名称为“test_*.py”或“*_test.py”的文件

> pytest 
 
我们使用了assert语句来验证测试期望值，pytest中有一种断言反思机制，能智能地报告assert表达式的中间值  



## 断言引发异常
使用raises可以帮助我们断言某些代码会引发某个异常，新建一个test_sysexit.py文件，输入以下代码：
```python 
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

这样在出现该异常的时候，这个测试用例也不会标记为失败，以quiet报告模式执行测试功能  
> pytest -q test_sysexit.py 
   

