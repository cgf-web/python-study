# CPU密集型任务，更适合用多进程。
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# 准备一个 CPU 密集型任务
def cpu_task(n):
    print(f'任务{n}开始了')
    total = 0
    for i in range(10000000):
        total += i * i
    return total
       
if __name__ == '__main__':
    print('=====多进程完成[CPU密集型任务】====')
    start = time.time()#距离1970年1月1日0点0分0秒的秒数
    #开启四个进程进行计算
    with ProcessPoolExecutor(4) as executor:
        list(executor.map(cpu_task, [1, 2, 3, 4]))#map本身是不阻塞的，用list()将其结果转换为列表 才能确保所有任务都完成
    end = time.time() - start       #计算总耗时
    print(f'多进程总耗时:{end}秒\n')  #0.57808秒

    # print('=====多线程完成【CPU密集型任务】=====')
    # start = time.time()#开启四个线程进行计算
    # with ThreadPoolExecutor(max_workers=4) as executor:
    #     results = list(executor.map(cpu_task, [1, 2, 3, 4]))#map本身是不阻塞的，用list()将其结果转换为列表 才能确保所有任务都完成
    # end = time.time() - start       #计算总耗时
    # print(f'多线程总耗时:{end}秒')  #1.78069秒
