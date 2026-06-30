import asyncio
import time

#定义一个协程函数
async def work(n, delay):
    print(f'work{n}开始')
    print(f'work{n}执行中.#模拟一个I0等待')
    await asyncio.sleep(delay)
    print(f'work{n}结束')
    return f'work{n}的返回值'

async def main():
    print('main开始')
    start = time.time()#获取当前时间
    
    ##asyncio.create_task 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中
    task1 = asyncio.create_task(work(1,2))
    task2 = asyncio.create_task(work(2,2))
    task3 = asyncio.create_task(work(3,2))

    #此处会等待task1执行完成
    res1 = await task1
    print(res1)
    #等待上面的task1完成后，再等待task2完成
    res2 = await task2
    print(res2)
    #等待上面的task2完成后，再等待task3完成
    res3 = await task3
    print(res3)
    end = time.time()
    print(f'耗时:{end-start:.2f}秒')
    print('main结束')

    return 'main的返回值'

# asyncio.run() 必须在函数外部调用
result = asyncio.run(main())
print(result)










