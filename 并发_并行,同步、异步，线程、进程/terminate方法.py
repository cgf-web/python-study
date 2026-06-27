#定义一个speak 函数，功能是:每隔一秒说话一次(一共说话10次)
import time
import os
from multiprocessing import Process   # Process是个类（注意大写P）  

def speak():
    try:
        for i in range(10):
            print(f'第 {i+1} 次说话', f'进程pid是：{os.getpid()}', f'我的父进程是：{os.getppid()}')
            time.sleep(1)       
            #注意terminate()终止进程，不会引起finally执行
    finally:
        print("我哦是finally里的逻辑")

#定义一个study函数，功能是:每隔一秒学习一次(一共学习15次)
def study():
    for i in range(15):
        print(f'第 {i+1} 次学习', f'进程pid是：{os.getpid()}', f'我的父进程是：{os.getppid()}')
        time.sleep(1)






if __name__ == '__main__':    #这是 Python 的主程序入口保护，特别是在使用多进程时非常重要！

    print("我是主程序第一行代码")
    p1 = Process(target=speak)
    p2 = Process(target=study)

    #调用进程对象的start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()  #异步
    p2.start()
    
    time.sleep(3)
    p1.terminate()  # 终止p1进程
    p1.join()  # 等待p1进程执行完毕
    print(p1.is_alive())  # 检查p1进程是否还活着

    print("主进程结束")

#terminate是暴力终止，不会执行finally里的逻辑
