#导入模块       调用方式--->模块名.功能名
# import random
#使用模块中提供的功能
# print(random.randint(10, 100))

# import random as rd       #起别名
# #使用模块中提供的功能
# print(rd.randint(10, 100))


#导入模块中的功能
from random import randint, choice      #从模块中导入指定的功能     调用方式--->功能名(参数列表)

from random import randint as rint
#使用导入的功能

print(randint(10, 100))
print(choice([1, 2, 3, 4, 5]))
print(choice('hello'))
print(choice((1, 2, 3, 4, 5)))
print(choice({1: 'a', 2: 'b', 3: 'c'}))


# 1。什么是模块?有什么用?
# 模块:就是一个python文件(.py)，其中就包含了变量、函数、类，以及可执行的代码。作用:提高代码复用性，降低开发门槛
# 2.导入模块的常用语法?
import 模块名
from 模块名 import 功能名
from 模块名 import 功能名 as 别名

# 注意:每一个python文件都可以作为一个模块，模块的名字就是文件的名字(建议使用python标识符定义，规范命名)
