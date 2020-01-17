import threading

a = [1, 2, 3, 4 , 5]
# 这个函数名可随便定义
def pop_it():
    while a:
        a.pop() 
        print(a)

def push_it(x):
    while True:
        a.append(x)
        print(a)

if __name__ == "__main__":
    t1 = threading.Thread(target=pop_it, args=())
    t2 = threading.Thread(target=push_it, args=(0,))
    t1.start()
    t2.start()
