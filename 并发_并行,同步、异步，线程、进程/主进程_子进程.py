import os
import time

print(f'当前进程ID:{os.getpid()}')
print(f'当前进程的父进程ID:{os.getppid()}')
time.sleep(10000)
