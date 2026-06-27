#定义一个speak 函数，功能是:每隔一秒说话一次(一共说话10次)
import time
import os
from multiprocessing import Process, current_process,Lock,RLock   # Process是个类（注意大写P）  

def speak(lock,msg):
    for i in range(10):

        #上锁,如果锁是空闲的   立刻上锁，继续往下执行；如果锁被别人拿着，就等待，直到锁被释放
        lock.acquire()
        lock.acquire()
        print('好好', end='')
        print('学习', end='')      #用锁包住，原子操作
        print('天天', end='')
        print('向上')
        lock.release()#释放锁：acquire和release必须成对出现，否则会永远卡住（死等）

        time.sleep(1)       

#定义一个study函数，功能是:每隔一秒学习一次(一共学习15次)
def study(lock):
    for i in range(15):
        with lock:   #with上下文管理器，自动上锁和释放锁
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)


#with lock:会自动完成两件事:
# (1).进入前:自动执行 lock.acquire()上锁
# (2).离开后:自动执行 lock.release()释放锁
# 好处:即便代码块里发生异常，也能保证释放锁，避免“卡死”



#注意:一定要写if __name__ == '__main__'这个判断，原因如下

#1.当创建子进程时，Python并不会把父进程内存里的speak函数接交给子进程。
#2. Python会启动一个全新的Python解释器进程，重新执行当前的.py文件(作为模块)；
#3. 在执行过程中，重新定义出一个speak 函数，交给子进程。

if __name__ == '__main__':    #这是 Python 的主程序入口保护，特别是在使用多进程时非常重要！
   
    # p1 = Process(target=speak)
    lock=RLock()   #RLock()可多次上锁 ，一个线程可以多次获取同一个锁，但必须成对出现，否则会永远卡住（死等）

    p1 = Process(target=speak,name='speak',args=(lock,),kwargs={'msg':'hello'})
    p2 = Process(target=study,name='study',args=(lock,))

    print(p1.name) #系统分配的进程名，可以自定义 Process-1
    print(p2.name) #系统分配的进程名，可以自定义 Process-2

    #调用进程对象的start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()
    
    # 等待子进程执行完毕（可选，确保主进程等待子进程完成）
    # p1.join()
    # p2.join()
    print("主进程结束")

#Process的参数:
""" group:默认值为None(应当始终为None)；
target:子进程要执行的可调用对象，默认值为 None。
name:进程名称，默认为None，如果设置为 None，Python 会自动分配名字。
args:给target 传的位置参数(元组)
kwargs:给 target传的关键字参数(字典)
daemon:标记进程是否为守护进程，取为布尔值(默认为None，表示从创建方进程继承) """