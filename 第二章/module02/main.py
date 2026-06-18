#导入自定义模块
import my_func


#调用模块中的函数
# print(my_func.PI)
# print(my_func.NAME)

# my_func.log_separator1()


# #导入自定义模块中的功能
# from my_func import log_separator1, log_separator2, PI,NAME
#导入所有功能
from my_func import *        #如果有__all__，则只能导入__all__中的功能

#调用自定义模块中的函数
print(PI)
print(NAME)

log_separator1()
log_separator2()

#导入自定义模块中的所有函数
import my_func  
my_func.log_separator1()

# __all_
# --all__是一个模块级别的特殊变量，用于指定 from  模块名  import *  时会导入哪些功能 (*通配了哪些功能)。


# 注意:__all__控制的是from  模块名  import * 时，要导入的功能，并不会影响直接导入具体的功能(如:from  模块名  import 功能）


# 1.__name__ 与__all__ 这两个特殊变量的作用是什么?
# __name__是Python中非常重要的内置变量，表示的是当前模块的名称
# 当模块直接运行时:__name__的值为"__main__"(if__name_main__")
# 当模块被导入时:__name__等于模块的文件名(不含.py后缀)
# __all__:控制 import *时导入哪些功能


# 包
# 包:本质就是一个文件夹，该文件夹中可以包含若干python模块(.py文件)，文件夹下还包含了一个__init__.py。
# 作用:模块文件较多时，用来管理多个模块。(包的本质也是一个模块)


