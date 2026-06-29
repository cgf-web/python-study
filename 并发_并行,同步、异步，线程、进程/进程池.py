from concurrent.futures import ProcessPoolExecutor, as_completed
import time, os

#创建『进程池执行器』、使用submit 方法提交任务、使用 shutdown 方法等待任务完成。

# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     time.sleep(2)


# if __name__ == '__main__':
#     print('--------------start----------------')
#     #创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     #使用submit 方法提交任务
#     executor.submit(work, 1)
#     executor.submit(work, 2)
#     executor.submit(work, 3)
#     executor.submit(work, 4)
#     executor.submit(work, 5)
#     executor.submit(work, 6)
#     executor.submit(work, 7)

#     #shutdown 的作用:不再接收新的任务。
#     #wait=True 的作用:阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print('-----------------end---------------')


# 2.获取子进程执行后的返回结果(Future类的实例对象+result方法)

# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     time.sleep(2)
#     return f'我是任务{n}的结果'


# if __name__ == '__main__':
#     print('--------------start----------------')
#     #创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     #使用submit 方法提交任务(submit只负责提交任务，不会阻塞主进程)
#     # f1=executor.submit(work, 1)
#     # f2=executor.submit(work, 2)
#     # f3=executor.submit(work, 3)
#     # f4=executor.submit(work, 4)
#     # f5=executor.submit(work, 5)
#     # f6=executor.submit(work, 6)
#     # f7=executor.submit(work, 7)    
#     futures=[executor.submit(work,i) for i in range(1,8)]
   
#     #wait=True 的作用:阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # print(futures[0].result())
#     # print(futures[1].result())
#     # print(futures[2].result())
#     # print(futures[3].result())
#     # print(futures[4].result())
#     # print(futures[5].result())
#     # print(futures[6].result())
#     #print(f'{[i.result() for i in futures]}')  # 获取所有任务的返回结果
#     for i in futures:
#         print(i.result())

#     print('-----------------end---------------')



#3使用as_completed:按“完成顺序”获取结果
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     if n==1:
#         time.sleep(15)
#     elif n==2:
#         time.sleep(10)
#     else :
#         time.sleep(1)    
#     return f'我是任务{n}的结果'

# if __name__ == '__main__':
#     print('------------start----------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     #submit 只是"提交"任务，不会等待任务执行完，它立刻返回一个 Future 对象，这个对象包含任务的执行结果。
#     futures = [executor.submit(work, index) for index in range(1, 8)]  #执行完任务结果也都存放在列表里  futures = [Future1, Future2, ..]
#     result_list=[]
#     for f in as_completed(futures):  #as_completed:迭代器，会按照任务完成的先后顺序，逐个返回 Future 对象。
#         result_list.append(f.result())

#     executor.shutdown(wait=True)
#     #打印每个任务的结果
#     print(result_list)

#     print('-------------end-------------')



# 4.使用 add_done_callback 方法，为任务添加完成时的回调函数
# def work(n):
#     print(f'work正在执行任务{n}.........{os.getpid()}')
#     time.sleep(2)
#     return f'我是任务{n}的结果'

# if __name__ == '__main__':
#     print('--------------start----------------')
#     #创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     result_list=[]

#     #任务完成后的回调函数
#     def done_func(future):
#         result_list.append(future.result())
    
#     #开启7个任务,并为每个任务添加完成时的回调函数
#     for i in range(1, 8):
#         f=executor.submit(work,i)
#         f.add_done_callback(done_func)

#     print(result_list)  # 打印每个任务的结果


#     #shutdown 的作用:不再接收新的任务。
#     #wait=True 的作用:阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print('-----------------end---------------')


# 5使用map方法批量提交任务(注意:map方法是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的)#
# def work(n):
#     time.sleep(2)
#     if n==1:
#         time.sleep(15)
#     elif n==2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'我是任务{n}的结果'

# if __name__ == '__main__':
#     print('---------start-------------')
#     #创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
  
#     #开启7个任务，并指定回调函数
#     #通过 map 方法批量提交任务(结果按照提交的顺序来)
#     results=executor.map(work, range(1, 8))
    
#     for result in results:
#         print(result)
#     #等所有任务都完成
#     executor.shutdown(wait=True)
#     print('------------end------------')


def work(n):
    time.sleep(2)
    if n==1:
        time.sleep(15)
    elif n==2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'我是任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')

    #创建一个进程池执行器
    with ProcessPoolExecutor(3) as executor:
        #开启7个任务，并指定回调函数
        #通过 map 方法批量提交任务(结果按照提交的顺序来)
        results=executor.map(work, range(1, 8))
        for result in results:
            print(result)
    #等所有任务都完成
    executor.shutdown(wait=True)
    print('------------end------------')















