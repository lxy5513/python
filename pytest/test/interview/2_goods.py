import random 

# 随机选一个1-4之间的数
num = random.randint(0,4)

dicts = {1:'袜子', 2:'鞋子', 3:'拖鞋', 4:'项链'}

num1 = 10
num2 = 20
num3 = 30
num4 = 40

def probility(num):

    total = num1 + num2 + num3 + num4
    if num == 1:
        result = num1/total 
    elif num == 2:
        result = num2/total 
    elif num == 3:
        result = num3/total 
    else:
        result = num4/total 
    return result 


print('{}被返回的概率是 {}%'.format(dicts[num], probility(num)*100))

