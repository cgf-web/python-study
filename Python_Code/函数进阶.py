# 函数-传参方式
# 传参方式指的是，在调用函数时，传递实参的方式。
# 1.位置参数:调用函数时根据函数定义时的位置来传递参数。
#定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
# #调用函数
# stu = reg_stu("张三",18,"男","北京")
# print(stu)
# 要求:调用函数时参数顺序与定义函数时参数顺序完全一致，否则会报错

# 2.关键字参数:调用函数时根据参数名来传递参数。
# 关键字参数:调用函数时以函数定义时形参名称作为关键字，以"键=值"的形式来传递参数，不要求顺序
#定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功,姓名:{name},年龄:{age}, 性别:{gender}, 城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
# #调用函数
# stu = reg_stu(name="张三",age=18,gender="男",city="北京")
# print(stu)
# stu2 = reg_stu(gender="男",name="王武",city="上海",age=22)
# print(stu2)
# stu2 = reg_stu("赵四",28,gender="男",city="上海")
# print(stu2)  # 输出: {'name': '赵四', 'age': 28, 'gender': '男', 'city': '上海'}

#位置参数
# 优点:简洁
# 缺点:可读性差、易出错、维护难
#使用场景：参数较少时，且参数顺序固定时

#关键字参数
# 优点:可读性好、不易出错、维护Easy
#使用场景：参数较多时，或参数顺序不固定时


# 默认参数也称为缺省参数，用于在定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数。
#定义函数
# def reg_stu(name, age, gender, city='北京' ):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender}，城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
# #调用函数
# stu = reg_stu("张三",18,"男")
# print(stu)
# stu = reg_stu("赵四",22,"男", "深圳")
# print(stu)
# 注意:默认参数必须放在没有默认值的参数列表的后面，一个函数在定义时是可以设置多个默认参数的。
# 注意:函数调用时，如果为默认参数传递了值，则会修改默认的参数值;如果没有传递该参数，则直接使用默认值。


# 不定长参数
# 介绍:不定长参数也叫可变参数，用于函数定义及调用时参数个数不确定(0个或多个)的场景。
# 类型:
#   位置传递
#   关键字传递


# 需求:定义函数，根据传入的数据，计算这批数据中的最小值、最大值、平均值。
# 注意:传递的所有匹配的位置参数都会被args变量收集，这些参数会合并封装为一个元组，args是元组类型(注意并不会封装关键字参数)
# 注意:args只是约定俗成的变量名，并不是关键字，这里可以使用任何合法的变量名(如 *data)
# def calc(*argv):  #argv是元组类型
#     max_data = max(argv)
#     min_data = min(argv)
#     avg_data = sum(argv) / len(argv)
#     return max_data, min_data, avg_data
#     info = (max(argv), min(argv), sum(argv) / len(argv))
#     return info
# max_data,min_data,avg_data=calc(1,2,3,4,5) #解包赋值，将返回的元组中的元素分别赋值给max_data,min_data,avg_data三个变量
# print(max_data,min_data,avg_data)
# data=calc(1,2,3,4,5,6,7,8,9,10)#
# print(data)

# 不定长参数-关键字传递(**kwargs)
#定义函数
# def calc_data(*args, **kwargs):#args收集位置参数（为元组类型），kwargs收集关键字参数（为字典类型）key:value
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     if kwargs.get('round'):
#         avg_data = round(avg_data, kwargs.get('count'))
#     return min_data, max_data, avg_data

# data = calc_data(100, 200,300,400, round=2, count=1)#前四个参数是位置参数，round=2是关键字参数，count=0是关键字参数
# print(data)
# data = calc_data(33, 11, 28, 91, 32, 75, 49)
# print(data)
# 注意:参数是以"键=值"形式传递的关键字参数，这些"键=值"参数都会被kwargs接受，并合并封装为字典类型


# def calc_data(*args, **kwargs):#args收集位置参数（为元组类型），kwargs收集关键字参数（为字典类型）key:value
#     """
#     计算数据的最小值、最大值、平均值
#     Args:
#         *args: 不定长位置参数，需要计算的这批数据
#         **kwargs: 不定长关键字参数
#             round: 四舍五入的位数
#             print: 是否打印结果
#     """
#     print(args)
#     print(kwargs)
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     if kwargs.get('round') is not None:
#         avg_data = round(avg_data, kwargs.get('round'))
#     if kwargs.get('print'):
#         print(f"最小值:{min_data}, 最大值:{max_data}, 平均值:{avg_data}")
#     return min_data, max_data, avg_data

# data = calc_data(100, 200,300,400, round=2, print=True)#前四个参数是位置参数，round=2是关键字参数，count=0是关键字参数
# print(data)
# data = calc_data(33, 11, 28, 91, 32, 75, 49,round=3, print=True)
# print(data)


# 1.什么是不定长参数?
#     参数个数不确定，此时就可以使用不定长参数解决这类问题
# 2.不定长参数的分类?
#     *args:不定长位置参数，函数调用时，通过位置参数传递多个参数封装到一个元组(tuple)中
#     **kwargs:不定长关键字参数，函数调用时，通过关键字参数传递多个参数封装到一个字典(dict)中
# 3.*args与**kwargs的应用场景?
#     *args适用于处理数量不确定的数据
#     **kwargs适用于处理数量不确定的选项(函数的配置参数，用来定制函数的行为)




# 函数的参数类型
# 普通参数:数字、布尔、字符串、列表、元组、集合、字典等。
#特殊参数：函数

# def add (x, y):
#     return x+y
# def subtract (x, y):
#     return x-y
# #乘
# def multiply (x, y):
#     return x*y
# #除
# def divide (x, y):
#     return x/y

# def calc(x,y,oper):
#     return oper(x,y)

# result = calc(10, 20, add)
# print(result)
# result = calc(10, 20, subtract)
# print(result)
# result = calc(10, 20, multiply)
# print(result)
# result = calc(10, 20, divide)
# print(result)


# 匿名函数
# 匿名函数指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写(单行表达式)。
# 语法:lambda 参数列表: 表达式
# 例如:lambda x, y: x + y   
#lambda:print("hello world")

# out_line=lambda : print("-----------------")
# add = lambda x, y:x + y

# out_line()
# print(add(100, 200))

#注意:函数逻辑比较简单(单行表达式)且只在一个地方使用时，可以考虑使用匿名函数，简化书写(通常作为高阶函数的参数使用)
#注意:匿名函数中可以返回结果，也可以不返回结果。返回结果时，不需要写return，表达式的运行结果就是要返回的结果。

# 需求3:完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序;

# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java","Go","JavaScript","Rust"]
# data_list.sort(key=lambda item: len(item))
# data_list.sort(key=lambda item: len(item),reverse=True)
# #sort原型     sort(*, key=None, reverse=False)默认参数为None   key:排序的依据函数，reverse:是否倒序排序
# #If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their return values.
# print(data_list)


# 定义一个函数，根据传入的数字，计算该数字阶乘的结果。
# 分析:
# 8的阶乘:8* 7* 6*5* 4*3 *2* 1

# def factorial(n):
#     """
#     计算阶乘
#     Args:
#         n: 阶乘的数字
#     Returns:
#         阶乘的结果
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)    #递归调用，直到n=0，返回1    函数中自己调用自己，直到满足条件，返回结果
# print(factorial(8))

# 电商订单计算器
# 定义一个函数，用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
# 具体规则如下:
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)

def calc_order_price(*args:tuple[str,float,int], coupon:float=0,score:float=0,express:float=0):
    """
    计算订单的总金额
    Args:
        *args: 不定长位置参数，需要计算的这批商品信息("鼠标",100,2)(("键盘",100,1))  
        coupon: 优惠券金额
        score: 积分抵扣金额
        express: 运费金额
    Returns:
        订单的总金额= 商品总金额 - 优惠券 - 积分抵扣 + 运费
    """

    #1.计算商品总金额
    total_price = []
    for goods in args:
        # 处理单个商品元组
        if isinstance(goods, tuple) and len(goods) == 3:
            total_price.append(goods[1] * goods[2])
        # 处理直接传入的单个商品参数（如 "鼠标", 100, 2）
        # 这种情况下需要特殊处理，因为args会是 ("鼠标", 100, 2, ("键盘", 100, 1), ...)
        # 更好的做法是让所有商品都以元组形式传入
    total_cost=sum(total_price)
    #2.扣减优惠券
    if total_cost >=5000 and coupon <= total_cost:
        total_cost-=coupon
    #3.扣减积分抵扣
    if total_cost >= 5000 and score//100 <= total_cost:    #//取整，确保积分只能整百抵扣
        total_cost-=score//100
    #4.加上运费
    total_cost+=express
    return total_cost

# total=calc_order_price("鼠标",100,2,("键盘",100,1),("手机",3999,1) ,coupon=100, score=4000, express=9.9)
# print(total)

total=calc_order_price("鼠标",100,2,("键盘",100,1),("手机",6999,1) ,coupon=100, score=4000, express=9.9)
print(total)

    
# 类型注解
# 类型注解是Python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型从而使代码更清晰、更安全、更易读、更易维护。
# 
#定义变量
a:int= 695
score:float= 98.5
hobby: str="Python"
flag:bool= True
pic: None=None
names: list[str|int]=["A","C","E"]
phones:set[str]= {"13309091111", "15209109121"}
options: dict[str, int]= {"count": 0, "total":0}
goods: tuple[str,int,int]=("手机",5999,1)


names.append(100)
# 类型推断
# 类型推断是指Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力，而无需开发者显式声明。

#注意:在对变量进行直接赋值，或者涉及到变量的运算、容器的推导等场景时，解释器会自动推导出变量的类型，而无需开发者显式声明。


# 函数-类型注解
# 为函数添加类型注解，其实主要就是为函数的参数和返回值添加类型注解，具体语法如下:
# def 函数名(参数1:类型1,参数2:类型2,)->返回值类型:
#     函数体
#     return 返回值
# 
def calc(scores: list[int])-> float:    #list[int]参数的类型    float返回值的类型
    """
    计算列表中所有整数的平均值
    Args:
        scores: 包含整数的列表
    Returns:
        列表中所有整数的平均值
    """
    return sum(scores)/ len(scores)

def calc_data(scores:list[int])-> tuple[int,int, float]:
    """
    计算列表中所有整数的最大值、最小值和平均值
    Args:
        scores: 包含整数的列表
    Returns:
        一个元组，包含列表中所有整数的最大值、最小值和平均值
    """
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores)/ len(scores)
    return max_v, min_v, avg_v  
avg=calc([1,2,3,4,5])
print(avg)
max_v,min_v,avg_v=calc_data([1,2,3,4,5])
print(max_v,min_v,avg_v)
