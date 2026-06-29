# GIL (Global Interpreter Lock) 全局解释器锁    是一把互斥锁
# 无论CPU有多少个核心，在某一时刻，只允许进程中的一个线程去执行Python代码
# 这把锁的目的是为了保护Python对象，避免多个线程同时访问和修改导致的数据不一致问题


# 何时释放GIL锁?
# 1. 主动释放(遇到I/O操作) 
# 2. 被迫释放(任务超时)

# CPython解释器中的多线程模型，本质上是并发，而不是并行!(是快速切换，而不是同时进行)

"""
对比维度         | GIL (Global Interpreter Lock) 全局解释器锁                | Lock / RLock (用户态互斥锁)
----------------|---------------------------------------------------       |------------------------------------------
核心本质        | 解释器级别的强制限制                                        | 代码级别的逻辑约定
谁来控制        | Python解释器: 自动加锁，遇到I/O或超时自动释放                | 程序员: 需手动编写 lock.acquire() 和 lock.release()
保护对象        | 保护“解释器不崩”: 维护引用计数、垃圾回收等底层结构的线程安全   | 保护“数据不算错”: 维护用户定义的变量、操作顺序等业务逻辑的完整性
作用范围        | 全局唯一: 一个进程里只有一个GIL，管着所有线程。              | 按需创建: 可以创建多把不同的锁，分别保护不同的业务逻辑资源
典型问题场景    | 导致多线程无法利用多核CPU进行并行计算                        | 若不加锁，售票场景下两个人可能买到同一张车票（数据竞争）
"""

#GIL锁和编码时使用的Lock 和Rlock 不是同一个东西
#Lock 和 Rlock是业务层面的锁，目标是:让业务逻辑别出错
#GIL锁是CPython解释器层面的锁，目标是:让Python代码执行更快

import time
#Rlock示例1:让打印是完整的
from threading import Thread, RLock,current_thread

# def show_info1(lock):
#         for index in range(10):
#             with lock:
#                 print('尚',end='')
#                 print('硅',end='')
#                 print('谷')

# def show_info2(lock):
#     for index in range(10):
#         with lock:
#             print('at', end='')
#             print('gui', end='')
#             print('gu')

# if __name__ == '__main__':
#     print('---------start-------------')
#     lock = RLock()
#     t1 = Thread(target=show_info1, args=(lock,))
#     t2 = Thread(target=show_info2, args=(lock,))
#     t1.start()
#     t2.start()
#    print('---------end-------------')




#同一个进程中的多个线程可以共享数据，因为它们运行在同一个内存空间下
#Rlock示例2:不要让两个窗口卖出同一张票
current = 1 
def sale(lock):
    global current
    while True: 
        with lock:
            if current <= 20:
                print(f'{current_thread().name}出售了第{current}张票！')
                current += 1
            else:
                print('票已售空')
                break
            time.sleep(0.1)


if __name__ == '__main__':
    print('---------start-------------')
    lock = RLock()  # 创建一个可重入锁
    t1 = Thread(target=sale, name='窗口1', args=(lock,))  # 创建线程1，传入锁
    t2 = Thread(target=sale, name='窗口2', args=(lock,))  # 创建线程2，传入锁
    t3 = Thread(target=sale, name='窗口3', args=(lock,))  # 创建线程3，传入锁
    t1.start()  # 启动线程1
    t2.start()  # 启动线程2
    t3.start()  # 启动线程3
    print('---------end-------------')


# CPU密集型任务
# (大部分时间花在“算”上): 图像处理、视频编码/解码、数值计算、模型训练......
# #应该使用多进程，因为多进程可以利用多核CPU进行并行计算，从而提高程序的执行效率
# #多进程之间数据不共享，需要通过队列或管道进行通信


# I/O密集型任务
# (大部分时间花在“等”上): 文件读写、网络请求、数据库操作......
# #应该使用多线程，因为多线程可以利用多核CPU进行并行计算，从而提高程序的执行效率
# #锁的获取和释放需要成对出现，否则会死锁
# #with语句可以自动管理锁的获取和释放，避免死锁






