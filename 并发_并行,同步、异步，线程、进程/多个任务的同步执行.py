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
    #调用三次work函数，分别得到三个协程对象
    coroutine1 = work(1,2)
    coroutine2 = work(2,2)
    coroutine3 = work(3,2)

    #此处会等待coroutine1执行完成
    res1 = await coroutine1
    print(res1)
    #等待上面的coroutine1完成后，再等待coroutine2完成
    res2 = await coroutine2
    print(res2)
    #等待上面的coroutine2完成后，再等待coroutine3完成
    res3 = await coroutine3
    print(res3)
    end = time.time()
    print(f'耗时:{end-start:.2f}秒')
    print('main结束')

    return 'main的返回值'

# asyncio.run() 必须在函数外部调用
result = asyncio.run(main())
print(result)










