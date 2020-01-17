import multiprocessing
import time
import collections 
Queue = collections.deque(maxlen=10)

def consume(interval):
    while True:
        print("Queue: ", Queue)
        if len(Queue) == 0:
            print("no data")
            time.sleep(0.5)
        else:
            num = Queue.pop()
            print("Num: ", num)
            time.sleep(0.5)

    print("worker_1")
    time.sleep(interval)
    print("end worker_1")

def productor(interval):
    while True:
        print("productor")
        time.sleep(interval)
        Queue.append(1)
        print("length of queue is: ", len(Queue))

    print("end worker_2")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = consume, args = (2,))
    p2 = multiprocessing.Process(target = productor, args = (3,))

    p1.start()
    p2.start()


