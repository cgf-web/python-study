
#Queue队列
#Pipe管道   默认duplex=True  是双向的，即：可以同时发送和接收


import time
from multiprocessing import Process,Pipe

def test1(con1):
    time.sleep(2)
    con1.send('hello')
    print('test1发送了hello')    

def test2(con2):
    data=con2.recv()
    print(f'test2接收了数据:{data}')
if __name__ == '__main__':
    con1,con2=Pipe(duplex=False)  # duplex=False表示单向管道，con1只能发送，con2只能接收
    p1 = Process(target=test1,args=(con1,))
    p2 = Process(target=test2,args=(con2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
