#异常处理
# try:
#     print("=============")
#     print(my name)
#     print("=============")  

# except NameError as e: #
#     print("程序运行出错，请联系管理员！：",e)

# try:
#     print("=============")
#     #print(1/0)
#     #print("ABC"[10])
#     print("ABC".hello)
#     print("=============")  

# except ZeroDivisionError as e: # 捕获除零错误
#     print("0不能作为除数！：",e)

# except IndexError as e: # 捕获索引超出范围错误
#     print("索引超出范围！：",e)
# except AttributeError as e: # 捕获属性错误
#     print("属性不存在！：",e)

# except Exception as e: # 捕获所有异常
#     print("程序运行出错，请联系管理员！：",e)



# finally:   # 无论是否发生异常，都会执行的代码块，通常用于释放资源，比如文件关闭、数据库连接关闭等
#     print("释放资源")  # 释放资源


# 1.为什么要捕获异常?
# 当程序运行出现异常，提供预案，处理异常，而不是让程序中止运行，保障程序的健壮性

# 2.如何捕获异常?
# try:
#     # 可能出现异常的代码
#     pass
# except ExceptionName as e:
#     # 异常处理代码
#     pass


# 异常的传递
# 异常传递就是异常在函数调用中层层上报的过程，直到有人处理它，或者程序崩溃。

def fun1():
    print("funl ... running ...")
    fun2()
def fun2():
    print("fun2 ... running ...")
    fun3()
def fun3():
    print("fun3 ... running ...")
    print(my_color)
if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("程序运行出错，请联系管理员！：",e)
        
# 主程序入口
# if __name__ == '__main__'
#         │
#         ▼
#     fun1()  ←───────────────┐
#         │                    │
#         ▼                    │
#     fun2()  ←───────────────
#         │                    │
#         ▼                    │
#     fun3()  ←───────────────┤
#         │                    │
#         ▼                    │
#     print(my_color)  ← 这里出错！│
#         │                    │
#         │  NameError:        │
#         │  'my_color'未定义  │
#         │                    │
#         └────────────────────┘
#         #异常向上传播（冒泡）
        
# 如果没有try-except捕获：
# 程序崩溃 ❌

# 如果有try-except捕获：
# 在某个层级被捕获 → 执行except代码 → 程序继续运行 ✓