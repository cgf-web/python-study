from multiprocessing import Process
import os, time

class SpeakProcess(Process):   # 继承Process类
    def __init__(self,a,b,**kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.b = b


    def run(self):     #自己定义一个类，得定义一个run方法   run方法其实是在重写父类方法，这样子才能实现多线程
        for index in range(10):
            print(f'{self.a}-{self.b}-我在说话{index}', f'进程pid是：{os.getpid()}', f'我的父进程是：{os.getppid()}')
            time.sleep(1)

class StudyProcess(Process):   # 继承Process类
    def run(self):     #自己定义一个类，得定义一个run方法   run方法其实是在重写父类方法，这样子才能实现多线程
        for index in range(10):
            print(f'我在学习{index}', f'进程pid是：{os.getpid()}', f'我的父进程是：{os.getppid()}')
            time.sleep(1)


if __name__ == '__main__':
    print('我是主程序的第一句打印')
    p1 = SpeakProcess(100,200)
    p2 = StudyProcess()

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('我是主程序的最后一句打印')
