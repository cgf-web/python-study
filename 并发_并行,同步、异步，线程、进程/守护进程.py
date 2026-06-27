#什么是守护进程?
#1.一种"依附于主进程存在的子进程"，一旦主进程结束，它就会被自动终止。
#2.简言之:主进程一死，守护进程必跟着死。

#守护进程的使用场景
#1.后台监控类任务
#2.日志/统计/采样类任务
#3.辅助型"陪跑任务"




#注意点:
""" 1.守护进程必须是子进程。
2.主进程结束，守护进程也会随之结束。
3.守护进程中，不允许再创建新的子进程。
4.必须在start()之前，start()之后，不能再设置 daemon 属性。 """
import os, time
from multiprocessing import Process

def monitor():
    """守护进程：持续监控并写入日志"""
    count = 0
    while True:
        count += 1
        print(f'[守护进程 {os.getpid()}] 第{count}次运行...')
        
        # 以追加模式打开文件并写入
        with open(r'.\并发_并行,同步、异步，线程、进程\log.txt', 'a', encoding='utf-8') as f:
            f.write(f'我是守护进程{os.getpid()}，正在运行... 第{count}次\n')
            f.flush()  # 刷新缓冲区
        
        time.sleep(1)

def test():
    for i in range(30):
        print(f"我是测试进程({os.getpid()})")    
        time.sleep(1)

if __name__ == '__main__':
    print(f'[主进程 {os.getpid()}] 开始执行')

    # 第一步：先写入一些初始数据
    print('[主进程] 正在写入初始数据...')
    with open(r'.\并发_并行,同步、异步，线程、进程\log.txt', 'a', encoding='utf-8') as f:
        for index in range(10):
            f.write(f'hello world{index}\n')
            f.flush()
    
    # 第二步：创建守护进程
    print('[主进程] 创建守护进程...')
    p = Process(target=monitor)  # 创建进程对象
    p.daemon = True  # 设置为守护进程（关键！）
    p.start()  # 启动进程
    p1=Process(target=test)
    p1.start()
    print(f'[主进程] 守护进程已启动，PID: {p.pid}')
    
    # 第三步：主进程做一些工作
    print('[主进程] 主进程正在工作...')
    time.sleep(5)  # 主进程工作5秒
    
    # 第四步：主进程结束
    print(f'[主进程 {os.getpid()}] 主进程即将结束')
    print('[提示] 主进程结束后，守护进程会自动终止！')
