import time 
from collections import deque
from threading import Thread 

class queen_data():
    def __init__(self, max_num=100):
        self._items = deque()
        self.num = 0
        self.max_num = max_num

    def pull(self, data):
        if self.num >= self.max_num:
            assert 'queen number larger than 100'
        self.num += 1
        self._items.append(data) 

    def push(self):
        if self.num < 0:
            print('the queen is empty')
            return 0 
        self.num -= 1
        return self._items.popleft()

    def get_num(self):
        return self.num


def request(i, q):
    q.pull(i)
    time.sleep(2)
    print('request: ', i)
    return i 

def post_process(q):
    time.sleep(1.5)
    data = q.push()
    print('post ', data)
    return data


queue = queen_data() 
t0 =  time.time()
for i in range(10):
    t1 = Thread(target=request, args=(i,queue)) 
    t2 = Thread(target=post_process, args=(queue,)) 
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    import ipdb;ipdb.set_trace()
    print(queue.get_num())

    #  data = request((i, queue))
    #  post_process(queue)
print('total time ', time.time() - t0)
