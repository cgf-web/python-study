#__all__     :指定 from  模块名   import *   时会导入哪些功能(*通配了哪些功能)。
__all__ = ["log_separator1","log_separator3","PI"]

#常量:大写字母命名，一般不建议修改
PI = 3.1415926
NAME="黑马涛哥"

def log_separator1():
    print("-" * 30)   #字符串重复输出  
def log_separator2():
    print("+ "* 30)
def log_separator3():
    print("#"* 30)
def log_separator4():
    print("* "* 30)

#测试函数
#__name__   :python中的内置变量，表示当前模块的名称，默认值为__main__，

#执行当前文件，则会执行以下代码，如果被当作模块导入，则不会执行以下代码
if __name__=="__main__":       #如果当前模块是主模块，才执行测试代码
    log_separator1()             #__name__ 就是让 Python 区分"这个文件是主角（直接运行）还是配角（被导入）"的标记。
