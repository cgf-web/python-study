#join方法的作用:阻塞当前进程，等join前面的进程执行完，再继续往下执行。
#join(timeout)，其中 timeout 是可选参数，表示等多久，单位是秒。
#注意点:

""" 1.p.join()不是让进程p等，而是让“执行这行join代码的那个进程”去等，等的是p这个进程。
2.当达到了timeout 所指定的时间后，进程并不会终止，只是“不再等”了。
3.join 必须在 start 之后 """


import time
import os
from multiprocessing import Process   # Process是个类（注意大写P）  

def speak():
    for i in range(10):
        print(f'第 {i+1} 次说话', f'进程pid是：{os.getpid()}', f'我的父进程是：{os.getppid()}')
        time.sleep(1)       

#定义一个study函数，功能是:每隔一秒学习一次(一共学习15次)
def study():
    for i in range(15):
        print(f'第 {i+1} 次学习', f'进程pid是：{os.getpid()}', f'我的父进程是：{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':    #这是 Python 的主程序入口保护，特别是在使用多进程时非常重要！

    print("我是主进程的第一行打印")
    p1 = Process(target=speak)    #类的实例化   创建进程对象p1
    p2 = Process(target=study)    #这两句是告诉操作系统，计划创建两个进程（还没创建，start()才会创建），分别执行speak和study函数   

    #调用进程对象的start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()   
    p1.join() #让主进程等 p1进程执行完毕后，主进程再继续执行。
    p2.join()
    # 等待子进程执行完毕（可选，确保主进程等待子进程完成）
    # p1.join()
    # p2.join()
    print("主进程结束")

