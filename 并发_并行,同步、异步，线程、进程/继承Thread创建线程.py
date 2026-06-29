from concurrent.futures import thread
import os
import time
from multiprocessing import Process
from threading import Thread, get_native_id, RLock

#定义一个speak 函数，功能是:每隔一秒说话一次(一共说话10次)
class SpeakThread(Thread):
    def __init__(self, lock):
        super().__init__()  # 不需要传参，直接调用父类初始化
        self.lock = lock

    def run(self):
        with self.lock:
            print(f'我在说话{index}，进程pid是:{os.getpid()},我的父进程是:{os.getppid()}，我的线程id是:{get_native_id()}')
            time.sleep(1)
class StudyThread(Thread):
    def __init__(self, lock):
        super().__init__()  # 不需要传参，直接调用父类初始化
        self.lock = lock
    def run(self):
        with self.lock:
            print(f'我在学习{index}，进程pid是:{os.getpid()}，我的父进程是:{os.getppid()}，我的线程id是:{get_native_id()}')
            time.sleep(1)

if __name__ == '__main__':
    print('---------start-------------')
    lock = RLock()
    #继承Thread类创建线程对象  传递参数lock，用于线程同步
    t1 = SpeakThread(lock)
    t2 = StudyThread(lock)
    #调用线程对象的start 方法，会立刻将该线程交由操作系统进行调度。
    t1.start()  # 启动线程1
    t2.start()  # 启动线程2
    #调用线程对象的join 方法，会阻塞调用线程，直到被调用线程执行完毕。
    t1.join()  # 等待线程1执行完毕
    t2.join()  # 等待线程2执行完毕
    print('我是主进程中的[最后一行】打印')



#线程和进程的用法都一样
#Thread 的参数
# group:默认为None(应当始终为None)。
# target:子线程要执行的可调用对象，默认值为None。
# name:线程名称，默认为None。如果设置为None，Python 会自动分配名字
# #args:给target 传的位置参数(元组)
# kwargs:给target 传的关键字参数(字典)
# daemon:标记线程是否为守护线程，取值为布尔值(默认为 None)   

#主进程里都至少有一个线程：是主线程
#线程是CPU调度的最小单位    进程





