import multiprocessing
import time
import random

def worker(d, key, value):
    t = random.random() * 1
    time.sleep(t)
    d[key] = value

length = 100
t0 = time.time()
array = []
if __name__ == '__main__':
    for i in range(length):
        array.append(i)
        if i % 4 == 0:
            mgr = multiprocessing.Manager()
            d = mgr.dict()
            jobs = [ multiprocessing.Process(target=worker, args=(d, i, i*2))
                 for i in array]
             
            for j in jobs:
                j.start()
            for j in jobs:
                j.join()

            print ('Results:' )
            for i in sorted(d):
                print(d[i])

            array = []


    print(time.time() - t0)
