def consumer():
    status = True 
    while True:
        n = yield status 
        print("I get {}!".format(n))
        if n==3:
            status=False 


def producer(consumer):
    n = 5 
    while n > 0:
        yield consumer.send(n)
        n -= 1 

c = consumer() 
print(type(c)) 
c.send(None) 
p = producer(c) 

for status in p:
    if status == False:
        print('Only need 3 4 5')
        break 

print('program over')


