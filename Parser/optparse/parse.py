from optparse import OptionParser 

parser = OptionParser()

addp = parser.add_option 
addp('-p', '--path', help='script input file path', dest='path', default='./path/default')
addp('-v', '--version', help='python version desc', dest='version', default='python 3')

# 生成一个字典类型
options, _ = parser.parse_args() 
print(options)
# {'path': './path/default', 'version': 'python 3'}

# 根据dest名称找到对应的值
Path = options.path 
# ./path/default
print(Path)
