# 第一题：斐波那契数列 
length = input('input a fib length(positive interger): ')

def fib(max):
    assert max >= 1 and max == int(max), 'please input a positive interger'

    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    print('finish')

length = int(length)
print(list(fib(length)))
