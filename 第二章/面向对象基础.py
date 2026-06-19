# 定义类的语法如下:

# #定义类
# class 类名:
#     pass
# #创建对象
# 对象名= 类名()
# 对象名.属性名1=属性值1
# 对象名.属性名2= 属性值2
# 动态添加属性
# 对象名.新属性名= 新属性值


#定义类
# class Car:
#     pass
# #创建对象
# cl = Car() #说明:类名的命名规范，遵循大驼峰命名法，每个单词的首字母都是大写，单词之间没有分隔符，比如:UserInfo, UserAccount
# cl.brand = "BMw"
# cl.name = "X5"
# cl.price = 500000
# print(cl.__dict__)
#说明:__dict__是Python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性，
#每个属性都是一个键值对，键是属性名，值是属性值。
#例如:cl.__dict__ = {'brand': 'BMw', 'name': 'X5', 'price': 500000}


# class Car:
#     pass
# c1=Car()

# #动态添加属性        不推荐使用
# c1.brand="BMw"
# c1.name="X5"
# c1.price=500000
# print(c1)
# print(c1.brand)
# print(c1.__dict__)



# 定义类时指定实例属性
# #定义类
# class类名:
#    def --init__(self,参数列表):          #self:方法的第一个参数，表示当前创建的实例对象，必须是第一个参数，不能省略。
#    self.属性名= 参数值
#    self.属性名= 参数值
# #创建对象
# 对象名= 类名(参数列表)

# 说明:定义在类的外面的称之为函数，定义在类中的函数称之为方法。
#__init__:初始化方法，对象创建后自动调用，主要用于设置对象的初始状态(设置对象属性)
#定义类
# class Car:
    #初始化方法
    #说明:__init__方法是类的特殊方法，用于初始化对象的属性。
    #在对象创建后自动调用，可以在该方法中为对象的属性设置初始状态。
    #self是第一个参数，表示当前创建的实例对象，必须是第一个参数，不能省略。
#     def __init__(self, c_brand, c_name, c_price) :
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的初始化完毕，对象属性已经添加完毕")
        
# #创建对象
# c1 = Car("BMW","X5",500000)
# print(c1.__dict__)

# c2 = Car("Audi","A4",400000)
# print(c2.__dict__)

# 1.定义类时，类名的命名规范?
# 大驼峰命名法,UserInfo、UserAccount
# 2.定义类时，__init__方法的作用?self参数的作用?
# _init_ 是初始化方式，对象创建时自动调用，主要用于设置对象的初始状态(设置对象属性)
# self是类中定义的方法的第一个参数，表示当前创建的实例对象


# 实例方法
# 在类中定义实例方法时，定义语法与之前学习的函数定义的方式是一致的。

# #定义类
# class 类名:
#   def __init__(self,形参列表):
#       self.属性名= 参数值
#       self.属性名= 参数值
#   def 方法名(self，形参列表):
#   def 方法名(self，形参列表):
# #创建对象
# 对象名= 类名(参数列表)对象名.方法名(实参)

# class Car:
#     def __init__(self, brand, name, price):
#         self.brand = brand
#         self.name = name
#         self.price = price

#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶...")
#     def total_cost(self, discount, rate=0.1):
#         """
#         计算提车总价
#         :param discount: 折扣率
#         :param rate: 税率
#         :return: 提车总价
#         """
#         return self.price * discount + self.price * rate

# c1 = Car("BMW", "X5",500000)
# total_cost1 = c1.total_cost(0.9, 0.1)
# print(f"提车总价为:{total_cost1:.2f}")

# total_cost2 = c1.total_cost(0.9)
# print(f"提车总价为:{total_cost2:.2f}")

# c1.running()#调用实例方法running，输出"BMW X5 正在高速行驶..."


# 魔法方法
# 魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如:__init__。
# 魔法方法是不需要我们手动调用的，Python会在合适的时机自动调用。

# 魔法方法                                        | 描述
# ---                                            ---
# __init__                                      | 初始化方法
# __str__                                       | 字符串表示的方法
# __eq__                                        | 相等(equal)比较两个对象是否相等 
#   
# __lt__,__le__, __gt__, __ge__                | 支持比较两个对象的大小(小于(less than), 
#                                               |小于等于(less than or equal), 大于(greater than), 大于等于(greater than or equal))    

class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")
    #魔法方法__str__，用于返回对象的字符串表示，通常用于打印对象时显示对象的属性值
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self, other):
        return self.price == other.price and self.brand == other.brand and self.name == other.name
    def __lt__(self,other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price

c1 = Car("BMW","X5",500000)
print(c1)#BMW X5 500000

c2 = Car("BMW","X5",500000) 
print(c2)#BMW X5 500000

print(c1 == c2)#True
print(c1 < c2)#False
print(c1 > c2)#False


# 属性
# 属性分为:
# 实例属性:实例属性属于每个具体对象的属性，每个对象都是独立的。(各个对象特有的数据)

# 类属性:类属性是属于类本身的属性，所有实例共享的。(所有对象共享的数据或配置)

class Car:
    wheel=4 #轮胎数量                           #类属性(通过 类名.属性 的方式操作)   (所有对象共享的属性)
    tax_rate = 0.1 #购置税

    def __init__(self, c_brand, c_name, c_price):      #实例属性(通过 实例对象.属性 的方式操作)
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")
c1 = Car ("BYD","汉",180000)
print(c1)#BYD 汉 180000
print(c1.wheel)#通过实例对象，查找属性时，会先查找实例属性，实例属性不存在时再查找类属性
print(Car.wheel)#4
print(Car.tax_rate)#0.1

c2 = Car ("Tesla", "Model Y", 260000)
print(c2)#Tesla Model Y 260000

#说明:通过实例查找属性时，会先查找实例属性，实例属性不存在时再查找类属性
