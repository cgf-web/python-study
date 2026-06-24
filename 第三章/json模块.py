# 读写json格式文件
# JSON是软件开发中最常用的数据交换格式，而为了简化JSON数据的处理，在Python标准库中就提供了处理JSON数据的核心模块json。

import json

user={
    "name":"张三",
    "age":18,
    "sex":"男",
    "city":"北京"
}
# 将python数据写入json文件
with open("resources/user.json","w",encoding="utf-8") as f:        
    json.dump(user,f,ensure_ascii=False,indent=4)       #序列化，将python数据转换为json格式字符串并写入文件
    #   ensure_ascii:默认为True,确保所有的数据输出的数据都是ascii编码(非ASCII码会进行转义);False，非ASCII码保留原样输出
    #   indent=4: 会在输出的json数据中添加缩进(格式化)

# 从json文件读取数据
with open("resources/user.json","r",encoding="utf-8") as f:
    data = json.load(f)     #反序列化，从文件中读取json数据并转换为 python对象
    print(data)
    print(type(data))
