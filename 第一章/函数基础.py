# 什么是函数?
# 函数是组织好的、可重复使用的、用来实现特定功能的代码片段。
# 函数定义与调用:
# #定义函数
# def 函数名(参数列表):
#     函数体
#     return 返回值
    
# #调用函数
# 函数名(参数)

# #定义函数
# def out_line():
#     print('-----------------')

# #调用函数
# out_line()

# 注意:函数定义时的参数列表与返回值语句是可有可无的(由需求确定)，
# 函数必须先定义后调用执行(函数定义时，内部代码并未执行，在调用时才执行)

# 函数的定义
from calendar import c


def out_line():
    print('-----------------')  # 函数中通过缩进来描述归属关系

# 函数的调用
out_line()  #调用函数才会执行函数体    并且先定义后调用


#定义函数
# def 函数名(参数列表):
#     函数体
#     return 返回值
# #调用函数
#     函数名(参数)
# #计算圆的面积
# def circle_area(r):
#     area = 3.14*r*r
#     return area
# #调用函数
# c_area = circle_area(10)
# print (c_area)
# #计算长方形的面积
# def rectangle_area(l, w):#形参
#     area= l* w
#     return area
# #调用函数
#     r_area = rectangle_area(20, 10)#实参
#     print(r_area)
# 注意:函数定义时如果有多个参数，多个参数之间使用逗号(，)分隔。
# 注意:return语句只有返回功能，而没有输出打印的功能，如果要输出，需要结合print()函数来实现


# def circle_area_len(r):
#     return round(3.14*r**2,1),round(2*3.14*r,1)#多个返回值，会封装到一个元组中返回
# #调用函数
# al = circle_area_len(10)
# print(al) 
# print(type(al))

# 函数的嵌套调用
# 嵌套调用指的是在一个函数中，又调用了另外一个函数。
# 函数调用遵循栈结构，最后被调用的函数最先返回，遵循后进先出的原则 LIFO(Last In First Out，后进先出)   弹夹

# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")
# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")
# def function_c():
#     print("c ...")

# function_a()


# 1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
# def triangle_area(b, h):
#     """根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。"""
#     return 0.5*b*h
# area=triangle_area(10,5)
# print(area)  # 输出三角形的面积

# help(triangle_area)  # 输出函数的文档字符串


# 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
# def count_aeiou(s):
#     """计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。"""
#     aeiou_list=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     count=0
#     for i in s:
#         if i in aeiou_list:
#             count+=1
#     return count
# count=count_aeiou("hello world")
# print(count)

# # 3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回元组中。
# def calc_score(score_list):
#     """计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回元组中。"""
#     max_score=max(score_list)
#     min_score=min(score_list)
#     avg_score=round(sum(score_list)/len(score_list),1)
#     return max_score, min_score, avg_score

# info=calc_score([670, 556, 582, 435, 608, 512, 678])
# print(info)
# print(type(info))
# max_score,min_score,avg_score=info  # 解包元组
# print("最高分:",max_score)
# print("最低分:",min_score)
# print("平均分:",avg_score)

# 1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数>=90:A
# 分数>=75:B
# 分数>=60:C
# 分数<60:D
# def score_grade(score):
#     """根据传入的分数，计算对应的分数等级并返回。"""
#     if score>=90:
#         return "A"
#     elif score>=75:
#         return "B"
#     elif score>=60:
#         return "C"
#     else:
#         return "D"
# grade=score_grade(85)
# print(grade)

# # 2.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# def is_palindrome(s):
#     """用于判断一个字符串是否是回文串，返回bool值。"""
#     return s==s[::-1]
# # 把字符串反转，如果和原字符串相同，就是回文串。(如:"level"，"radar"，"黄山落叶松叶落山黄")
# print(is_palindrome("level"))  # 输出: True

# # 3.定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def time_convert(s):
#     """完成时间转换功能，将传入的秒转换为小时、分钟、秒。"""
#     h=s//3600
#     m=(s%3600)//60
#     s=s%60
#     return h, m, s
# print(time_convert(3665))  # 输出: (1, 1, 5)  # 调用函数并输出结果
# # 4.定义一个函数:根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)  
# def triangle_type(a, b, c):
#     """根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。"""
#     if a+b<=c or a+c<=b or b+c<=a:
#         return "不能构成三角形"
#     elif a==b==c:
#         return "等边三角形"
#     elif a==b or a==c or b==c:
#         return "等腰三角形"
#     else:
#         return "普通三角形"
# print(triangle_type(6,6,6))  # 输出: 等边三角形
# print(triangle_type(6,6,7))  # 输出: 等腰三角形
# print(triangle_type(6,7,8))  # 输出: 普通三角形


# 变量的作用域指的是变量的作用范围(标识这个变量在哪里可以使用，在哪儿不可以使用)。
#定义函数
num=100   #函数外部定义的变量，称为全局变量

def circle_area(r):
    """计算圆的面积"""
    pi = 3.14           #函数内部定义的变量，称为局部变量
    area= pi * r *r

    num=10000       
    print("num=:",num)   #局部变量num    只在局部有效，而且不会影响全局变量num
    return area
count = 0          #函数外部定义的变量，称为全局变量
#调用函数
c_area = circle_area(10)     
print(c_area)
print("num=:", num)      #与局部变量中的num同名，局部变量优先，但不影响全局变量num
# print(pi)
# print(area)  #局部变量只能在函数内部使用，外部无法访问

# 全局变量:在函数之外定义的变量，称之为全局变量，在整个文件中(包括函数内)都可以使用(通常定义在文件的顶部)
# 局部变量:在函数内部定义的变量，称之为局部变量，只能在该函数内部使用，外部无法访问(函数执行完毕后，会自动销毁其内部局部变量)


#global关键字

num1=1#全局变量

def fun1():
    global num1#告诉python解释器，函数中使用全局变量num1
    num1=100 #修改全局变量num1
    print(num1)
fun1() # 100
print(num1) # 100

# 1.什么是局部变量，全局变量?
# 在函数内部定义的变量就是局部变量，函数外声明的变量是全局变量。
# 2.global关键字的作用?
# 在函数内部使用，声明接下来要使用的是全局变量，语法:global  xxx
# 3.注意事项
# 尽量避免在函数中使用全局变量，因为会使代码难以维护和调试
# 考虑使用函数参数和返回值来传递数据,而不是依赖全局变量
# global主要用在程序的状态、配置和计数器等场景中


debug_mode = False

def enable_debug_mode():
    global debug_mode
    debug_mode = True
print("调试模式已开启")     #global的妙用

def disable_debug_mode():
    global debug_mode
    debug_mode = False
print("调试模式已关闭")     #global的妙用