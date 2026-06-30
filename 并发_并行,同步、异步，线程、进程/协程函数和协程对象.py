# 协程
# 什么是协程?

# 协程的基本原理
# 第一种描述:协程是一种可以被挂起,并且在挂起之后，还可以恢复执行的函数。
# 第二种描述:协程又称微线程，是种用户态内的上下文切换技术。
# 
# 注意:协程不是操作系统提供的，是由程序员在用户态，实现的一种切换机制。而是程序员自己实现的。



#1.协程函数(coroutine Function):使用『async关键字』修饰的函数，就是协程函数。
#2.协程对象(coroutine Object):调用『协程函数』，就会得到『协程对象』。协程对象是『可等待对象』。
#注意:调用『协程函数』，并不会执行『协程函数』中的代码。
import asyncio

async def work():
    print('协程函数')
    print('协程函数执行完毕')
    return '协程函数执行完毕'


#调用协程函数，会得到协程对象
#asyncio.run方法做了3件事:
# 1.创建一个事件循环。asyncio.run方法会自动创建一个事件循环。
# 2.将收到的协程对象，包装成一个任务(task)，交给事件循环。asyncio.run方法会自动将协程对象包装成任务。
# 3.启动事件循环。asyncio.run方法会自动启动事件循环。
# 4.等待任务执行完毕，并返回结果。asyncio.run方法会自动等待任务执行完毕，并返回结果。

#注意:asyncio.run 会阻塞当前线程，直到任务执行完毕，并返回该任务 return 的最终结果。
coroutine_object = work()
result = asyncio.run(coroutine_object)

print(result)
print(coroutine_object)




