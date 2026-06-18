#1.导入模块
import utils.my_func       #导入包下的模块

utils.my_func.log_separator1()

from utils import my_func       #从包下导入模块
my_func.log_separator2()

#注意:在通过'from 包名import*’导入全部模块的时候，需要在init__.py 文件中添加__all__=[]'，控制允许导入的模块列表
#注意如果要通过fromimport * 导入包下的所有模块，需要init__.py 文件中添加__all__=[]
from utils import *       #从包下导入所有模块
my_func.log_separator3()
my_func.log_separator4()

print(my_var.PI)    
print(my_var.NAME)

#2.导入模块中的功能
from utils.my_func import log_separator5   #相对路径写法
from 第二章.utils.my_func import log_separator6    #绝对路径写法

log_separator5()
log_separator6()

# 1.什么是包?有什么作用?
# 包就是一个文件夹，里面可以存储很多Python模块(py文件)，通过包可以对模块进行归类
# 2.__init__.py文件的作用?
# 标识这是一个包，而不是普通的文件夹
# 控制在import * 时导入的模块列表(__all__变量)
# 3.导入包的方式?
import 包名.模块名
from 包名 import 模块名
from 包名 import *
from 包名.模块名 import 功能名
from 包名.模块名 import *




