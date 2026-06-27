#进程之间不共享内存，因此也就不共享任何变量。

from multiprocessing import Process

""" num=100
names=[]

def test1():
    global num, names
    num+=10
    names.append("张三")
    print(f'我是test1进程,操作之后的num为：{num},names为：{names}')#110
def test2():
    global num, names
    num-=10
    names.append("李四")
    print(f'我是test2进程,操作之后的num为：{num},names为：{names}')#90
if __name__ == '__main__':
    print('主进程中的[第一行】代码')
    p1 = Process(target=test1)#实例化，创建进程对象
    p2 = Process(target=test2)
    p1.start()  #向操作系统申请启动进程p1
    p2.start()  #向操作系统申请启动进程p2
    p1.join()  #等待进程p1执行完毕
    p2.join()
    print('主进程中的[最后一行】代码，num的值为：',num,'names为：',names)#100 """

#三个进程中都操作了全局变量num和names，但都是隔离的，互不干扰

def test1(num,names):
    num+=10
    names.append("张三")
    print(f'我是test1进程,操作之后的num为：{num},names为：{names}')#110
def test2(num,names):
    num-=10
    names.append("李四")
    print(f'我是test2进程,操作之后的num为：{num},names为：{names}')#90
if __name__ == '__main__':
    print('主进程中的[第一行】代码')
    num=100
    names=[]

    p1 = Process(target=test1,args=(num,names))#实例化，创建进程对象，传递参数num和names，num和names虽然是可变对象，但进程之间不共享变量，所以每个进程都有自己独立的num和names
    p2 = Process(target=test2,args=(num,names))
    p1.start()  #向操作系统申请启动进程p1
    p2.start()  #向操作系统申请启动进程p2
    p1.join()  #等待进程p1执行完毕
    p2.join()
    print('主进程中的[最后一行】代码，num的值为：',num,'names为：',names)#100


#因为每个进程启动的时候，其实就相当于把这个文件重新编译运行了一遍，所以说是互不干扰的，就相当于运行了三遍











