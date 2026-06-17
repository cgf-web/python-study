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


def calc_data(*args, **kwargs):#args收集位置参数（为元组类型），kwargs收集关键字参数（为字典类型）key:value
    """
    计算数据的最小值、最大值、平均值
    Args:
        *args: 不定长位置参数，需要计算的这批数据
        **kwargs: 不定长关键字参数
            round: 四舍五入的位数
            print: 是否打印结果
    """
    print(args)
    print(kwargs)
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get('round') is not None:
        avg_data = round(avg_data, kwargs.get('round'))
    if kwargs.get('print'):
        print(f"最小值:{min_data}, 最大值:{max_data}, 平均值:{avg_data}")
    return min_data, max_data, avg_data

data = calc_data(100, 200,300,400, round=2, print=True)#前四个参数是位置参数，round=2是关键字参数，count=0是关键字参数
print(data)
data = calc_data(33, 11, 28, 91, 32, 75, 49,round=3, print=True)
print(data)


# 1.什么是不定长参数?
#     参数个数不确定，此时就可以使用不定长参数解决这类问题
# 2.不定长参数的分类?
#     *args:不定长位置参数，函数调用时，通过位置参数传递多个参数封装到一个元组(tuple)中
#     **kwargs:不定长关键字参数，函数调用时，通过关键字参数传递多个参数封装到一个字典(dict)中
# 3.*args与**kwargs的应用场景?
#     *args适用于处理数量不确定的数据
#     **kwargs适用于处理数量不确定的选项(函数的配置参数，用来定制函数的行为)