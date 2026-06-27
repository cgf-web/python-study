#我们之前学过 list、tuple、dict，它们的特点是:数据想怎么拿数据，就怎么拿。
# 队列(Queue)是:一种“先进先出"的数据结构(先放进去的数据，一定会先取出来)
#栈是“后进先出"的数据结构(后放进去的数据，一定会先取出来)

from multiprocessing import Queue, Process   # Queue是多进程队列，可以跨进程通信
# from queue import Queue    # 这个里面的Queue不能跨进程通信，多进程场景不要用
import time

def test(q):
    time.sleep(3)
    result=q.get()
    #print(result)
    print('我从队列中取出了一个元素',result)


#创建一个队列(不限制大小，即:不设置容量上限)
# q1 = Queue()
#创建一个队列(最多能保存3个元素)
# q2 = Queue(3)

#1 put方法:往队列里放数据(入队)
# q1.put(10)
# q1.put(20)
# q1.put(30)
#2 get方法:从队列里取数据(出队)
""" value1 = q1.get()
value2 = q1.get()
value3 = q1.get()
print(value1)
print(value2)
print(value3) """

# 3.empty方法:判断队列是否为空
""" result = q1.empty()
print(result) """

# 4.full方法:判断队列是否已满
""" result = q1.full()
print(result) """

""" q2.put(10)
q2.put(20)
q2.put(30)

result=q2.empty()
print(result)
result = q2.full()
print(result) """

#5. qsize方法:获取队列的大小
""" result = q1.qsize()
print(result) """


#6. 队列具备等待模式
# q2.put(100)
# q2.put(200)
# q2.put(300)
# # # (1).当队列已满，继续 put，就会进入等待模式，等别人调用get方法，取走一个元素
# # q2.put(400)
# # print('放入完毕')

# #(2).当队列已满，执行:put(元素，timeout=秒数)，就会等待指定秒数。
# q2.put(400,timeout=3)
# print('放入完毕')     #如果队列已满，就会等待3秒，如果3秒内有元素被取走，就会继续执行，否则就会报错

# (3).put_nowait 方法，会直接向队列中添加元素，不会进入等待模式，若队列已满，会抛出异常。
# 备注:put_nowait 等价于 put(元素，block=False)，block的默认值为 True
# q2.put(400, block=False)
# q2.put(400, block=False)

#get读多了，也会进入等待模式
# q2.get()
# q2.get()
# q2.get()

#(1).当队列已空，继续get，就会进入等待模式。
#q2.get()

#(2).当队列已空，执行:get(元素，timeout=秒数)，就会等待指定秒数。
# q2.get(timeout=3)

#3. get_nowait方法，会直接从队列中获取元素，不会进入等待模式，若队列为空，会抛出异常。
""" q2.get_nowait()
print('获取完毕') """

#备注:get_nowait等价于get(block=False)    block的默认值为 True   阻塞的意思
#q2.get_nowait()
#q2.get(block=False)


#通过多进程，演示一下:当队列满了以后，再次put会等待，当有人从队列中取出元素后，put会继续。

if __name__ == '__main__':
    q=Queue(2)
    q.put('尚硅谷')
    q.put('atguigu')
    print(f'队列是否已满：{q.full()}')

    p1=Process(target=test,args=(q,))  #传的参数是元组时，元组的逗号不能省略，否则会报错
                # Python 靠逗号 , 来识别元组，不是靠括号！一个元素的元组，逗号绝对不能省！ 否则会理解成一个元素带括号，而不是元组
    p1.start()

    print('继续将向已满的队列中put元素，会等待')
    q.put('hello')

    print('目前队列中的元素:')
    print(q.get())
    print(q.get())

