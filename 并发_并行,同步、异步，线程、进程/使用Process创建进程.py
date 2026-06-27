#定义一个speak 函数，功能是:每隔一秒说话一次(一共说话10次)
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



#注意:一定要写if __name__ == '__main__'这个判断，原因如下

#1.当创建子进程时，Python并不会把父进程内存里的speak函数接交给子进程。
#2. Python会启动一个全新的Python解释器进程，重新执行当前的.py文件(作为模块)；
#3. 在执行过程中，重新定义出一个speak 函数，交给子进程。

if __name__ == '__main__':    #这是 Python 的主程序入口保护，特别是在使用多进程时非常重要！
    #创建两个Process 类的实例对象(进程对象)，分别是p1和p2。
    #注意点1:p1和 p2就对应着以后的两个子进程，在创建它们的时候，就要指定好他们要执行的任务。
    #注意点2:此时的p1和p2只是代码层面的两个进程对象，操作系统还没有真的创建 p1和p2 两个进程。
    p1 = Process(target=speak)
    p2 = Process(target=study)

    #调用进程对象的start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()
    
    # 等待子进程执行完毕（可选，确保主进程等待子进程完成）
    # p1.join()
    # p2.join()
    print("主进程结束")

