#Python中的字典(dict)，里面存储的是键值对(key-value)类型的数据，可以根据键(key)找到对应的值(value)。
#映射  哈希  ===字典(dict)

#现需要存储班级学员高考成绩，其中包含王林(670)，韩立(556)，李慕婉(582)，紫灵(435)，许立国(608)..,该如何存储呢?
# 定义字典存储
#dict1 ={"王林":670,“韩立”:556,“李慕婉”:582,"紫灵":435，"许立国":608，"王政":512,"张紫":678}

# 字典:使用键值对(key:value)来存储数据，每个键都对应一个值，通过键(key)可以快速找到对应的值(value)。
# 特点:键值对(key:value)存储、键(key)不能重复、可修改。
#定义字典

# dict1 = {"王林": 675,"李慕婉":608,"许立国":478,...}
# #定义空字典
# dict2 = {}
# dict3 = dict()

# #根据key获取value
# score = dict1["李思"]
# 注意:字典(dict)中的value可以是任何类型的数据，而且key不能为可变类型(如:不能为列表list、集合set、字典dict)

#key不能重复   重复了后面的值会覆盖前面的值   key还得是不可变类型的（str int float tuple）   value可以是任何类型
#key  不能是可变类型  list set dict
# dict1 = {"王林": 670, "韩立": 556, "李慕婉": 582, "紫灵": 435, "许立国": 608, "王政": 512, "张紫": 678}
# print(dict1)
# print(type(dict1))
# print(dict1["王林"])#获取值
# dict1["王林"]=678
# print(dict1["王林"])

# 3.字典的注意事项
# value可以是任意类型，而key必须是不可变类型(不能为list、set、dict)
# 字典内的key不允许重复，如果重复定义，后面的覆盖前面的
# 字典是没有索引下标的，不能根据索引获取值，只可以根据key获取value

# 字典的增删改查操作方式如下:
dict1 = {"小智": 675, "李思": 608, "李琪": 478, "小黑": 545, "温韬": 429}

"""
| 类型 | 操作                  | 含义                                       | 样例                      |
|------|----------------------|--------------------------------------------|---------------------------|
| 添加 | dict[key] = value    | 往指定字典中添加key-value键值对         | dict1["涛哥"] = 688       |
| 删除 | dict.pop(key)        | 删除字典中指定的key,并返回该key对应的value | score = dict1.pop("涛哥") |
| 删除 | del dict[key]        | 删除字典中指定的键值对                  | del dict1["涛哥"]         |
| 修改 | dict[key] = value    | 修改字典中指定的key对应的值             | dict1["小智"] = 658       |
| 查询 | dict[key]            | 根据key获取value                       | dict1["涛哥"]             |
| 查询 | dict.get(key)        | 根据key获取value (不存在返回None)       | dict1.get("涛哥")         |
| 查询 | dict.keys()          | 获取所有的key                          | dict1.keys()              |
| 查询 | dict.values()        | 获取所有的value                        | dict1.values()            |
| 查询 | dict.items()         | 获取所有的key-value键值对               | dict1.items()             |
"""

#字典 常见操作
# dict1={"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
# print(dict1)
# #添加 - key不存在就是添加
# dict1["涛哥"]=550
# print(dict1)
# #修改- key存在就是修改
# dict1["涛哥"]=620
# print(dict1)
# #查询
# print(dict1["涛哥"])# 根据key获取value
# print(dict1.get("涛哥"))# 根据key获取value

# print(dict1.keys())#获取所有的key
# print(dict1.values()) #获取所有的value
# print(dict1.items())# 获取所有的键值对 key:value

# #删除
# score = dict1.pop("许立国")
# print(score)
# print(dict1)

# #删除
# del dict1["韩立"]
# print(dict1)

# #遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")

# for item in dict1.items():
#     print(f"{item[0]}:{item[1]}")

# for k,v in dict1.item():
#     print(f"{k},{v}")


# 开发一个购物车管理系统，实现商品信息的添加、修改删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的介格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"a商品名称:xxx，商品价格:xxx，商品数量:xxx"
# 5.退出购物车


shopping_cart={}

#1.制作菜单
print("欢迎使用购物车系统 ~")
menu = """
        1.添加购物车
        2.修改购物车
        3.删除购物车
        4.查询购物车
        5.退出购物车
    """

while True:
    #1.制作菜单
    print(menu)
    #2.执行具体操作
    choice = input("请输入你的选择:(1-5): ")

    match choice:
        case "1":
            goods_name = input("请输入商品名称: ")
            goods_price = float(input("请输入商品价格: "))
            goods_num = int(input("请输入商品数量: "))

            if goods_name in shopping_cart:
                print("商品已存在,请重新选择")
            else:
                shopping_cart[goods_name] = {"价格": goods_price, "数量": goods_num}
                print("商品已添加")
            print(shopping_cart)
        case "2":
            goods_name = input("请输入要修改的商品名称: ")
            if goods_name in shopping_cart:
                goods_price = float(input("请输入商品最新价格: "))
                goods_num = int(input("请输入商品数量: "))   
                shopping_cart[goods_name] = {"价格": goods_price, "数量": goods_num}               
            else:
                print("商品不存在,请重新选择")
                continue
            print("商品已修改")     
        case "3":
            goods_name = input("请输入要删除的商品名称: ")
            if goods_name in shopping_cart:
                shopping_cart.pop(goods_name)
                print("商品已删除")
            else:
                print("商品不存在,请重新选择")
        case "4":
            # for goods_name, goods_info in shopping_cart.items():
            #     print(f"{goods_name}:商品价格:{goods_info['价格']},商品数量:{goods_info['数量']}")
            for goods_name in shopping_cart:
                goods_info=shopping_cart[goods_name]
                print(f"商品名称：{goods_name}:商品价格:{goods_info['价格']},商品数量:{goods_info['数量']}")
        case "5":
            print("退出购物车")
            break
        case _:#匹配其他所有情况
            print("输入错误")














