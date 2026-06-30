# await关键字的作用:
# 1.挂起:await会暂停当前协程的执行。
# 2.等待:遇到await关键字，事件循环会立即安排avait后面的对象去执行，并等待该对象执行完成，并且可以拿到执行结果。
#     关键点:在执行 await 后面的对象时，会出现两种情况:
#         情况一:如果在执行该对象中的代码时，遇到了【await I/O操作】(需要等待外部资源返回结果的操作)
#         例如:网络请求、文件读写等。
#         那CPU 的控制权就会交给事件循环。
#         事件循环会去调度循环中的其他任务(如果有的话)

#         情况二:如果该对象中的代码，不包含任何[await I/o操作】
#         例如:print打印、数学计算、逻辑计算等。
#         此时事件循环拿不到CPU控制权，无法调度循环中的其他任务，不会发生任务切换。
# 3.恢复:当await后的对象执行完毕，事件循环会恢复之前被挂起的协程，该协程会从当时挂起的位置继续执行，并拿到返回值。

# 注意点:await 后面只能写『可等待的对象』，常见的可等待对象:1.协程对象、2.Future对象、3.Task对象。

import asyncio

# async def work():
#     """
#     模拟一个不包含 I/O 操作的协程任务。
#     注意：由于内部没有 await I/O 操作，执行期间不会发生任务切换，会一直占用 CPU 直到执行完毕。
#     """
#     print('work开始')
#     print('work执行中..')
#     print('work结束')
#     return '工作结果!'


# async def main():
#     """
#     主协程函数。
#     1. 打印 'main'
#     2. await work(): 
#        - 挂起 main 协程。
#        - 执行 work() 协程。
#        - 因为 work() 中没有 I/O 等待，它会立即同步执行完毕。
#        - main 协程恢复执行，并获取 work() 的返回值（虽然这里未接收）。
#     3. 打印 'main执行完毕'
#     4. 返回字符串
#     """
#     print('main')
#     # 等待 work 协程执行完毕
#     # 此处演示的是“情况二”：work 中无 I/O 操作，因此不会触发事件循环的任务调度切换
#     res=await work()
#     print(res)
#     print('main执行完毕')
#     return 'main执行完毕'

# # asyncio.run() 创建事件循环并运行 main 协程，直到其完成
# result = asyncio.run(main())
# # 打印 main 协程的返回值
# print(result)


async def work():
    print('work开始')
    print('work执行中..')
    res = await asyncio.sleep(2)# 模拟I/O操作
    print(res)# 打印结果
    return '工作结果'
async def main():
    print('main开始')
    # await去等待一个协程对象
    res = await work()
    print(res)
    print('main结束')
    return 'main的返回值'
result = asyncio.run(main())
print(result)

























