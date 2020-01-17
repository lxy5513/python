import os
from kafka import KafkaConsumer
from hashlib import md5
import hashlib
import cv2
from tqdm import tqdm
import gc
from multiprocessing import Process, Manager
server = "10.0.0.222:9022"

# 向共享缓冲栈中写入数据:
def write_frame(stack, cam, top: int) -> None:
    """
    :param cam: 摄像头参数
    :param stack: Manager.list对象
    :param top: 缓冲栈容量
    :return: None
    """
    print('Process to write: %s' % os.getpid())
    cap = cv2.VideoCapture(cam)
    while True:
        _, img = cap.read()
        if _:
            stack.append(img)
            # 每到一定容量清空一次缓冲栈
            # 利用gc库，手动清理内存垃圾，防止内存溢出
            if len(stack) >= top:
                del stack[:]
                gc.collect()



def gene_topic(srcbyte):
    srcbyte = srcbyte.encode("gb2312")
    testnew = hashlib.new("md5", data=srcbyte).hexdigest()
    m = md5()
    m.update(srcbyte)
    srcbyte = m.hexdigest()
    topic = "topic_" + srcbyte
    return topic

# 向共享缓冲栈中写入KAFKA数据:
def write_kafka(stack, topic,  top: int) -> None:
    print('Process to write: %s' % os.getpid())
    consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[server],
    )

    while True:
        for msg in consumer:
            info = str(msg.value, 'utf-8')
            try:
                det = eval(info)["fall_det"]
                result = eval(info)
                stack.append(result)
                # 每到一定容量清空一次缓冲栈
                # 利用gc库，手动清理内存垃圾，防止内存溢出
                if len(stack) >= top:
                    del stack[:]
                    gc.collect()
            except Exception as e:
                print("Error: ", e)


def add_text(image, loc, text):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = loc # (10,500)
    fontScale              = 2
    fontColor              = (255,255,2)
    lineType               = 2

    cv2.putText(
        image,
        text,
        bottomLeftCornerOfText,
        font,
        fontScale,
        fontColor,
        lineType)
    return image


# 在缓冲栈中读取数据:
def read(stack_frame, strack_info) -> None:
    print('Process to read: %s' % os.getpid())
    while True:
        if len(stack_frame) != 0 and len(strack_info)!=0:
            frame = stack_frame.pop()
            result = strack_info.pop()

            kpts=result['kpts']
            candidates = result['candidates']
            server_time = result['abs_timestamps']
            fall_det = result['fall_det']
            alarm = result['alarm']
            loc = (30, 30)
            if fall_det:
                print("CAUTION!")
                frame = add_text(frame, loc, "caution")
            if alarm:
                print("HELP!!")
                frame = add_text(frame, loc, "help")

            cv2.imshow("img", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break


if __name__ == '__main__':
    path = "rtsp://admin:t3chc7l123@10.0.0.193:554/ch1/sub/av_stream"
    topic = gene_topic(path)
    # 父进程创建缓冲栈，并传给各个子进程：
    q1 = Manager().list()
    q2 = Manager().list()
    pw = Process(target=write_frame, args=(q1, path, 100))
    pw2 = Process(target=write_kafka, args=(q2,topic, 10))
    pr = Process(target=read, args=(q1, q2))
    # 启动子进程pw，写入:
    pw.start()
    pw2.start()
    # 启动子进程pr，读取:
    pr.start()

    # 等待pr结束:
    pr.join()
    # pw进程里是死循环，无法等待其结束，只能强行终止:
    pw.terminate()
    pw2.terminate()
