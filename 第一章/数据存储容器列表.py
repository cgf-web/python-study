
# 数据容器
# 一种可以容纳多份数据的数据类型(容器)，容纳的每一份数据称之为1个元素，每一个元素都可以是任意类型的数据，如:字符串、数字、布尔等。

# 列表(list)
# 字符串(str)
# 元组(tuple)
# 集合(set)
# 字典(dict)

# 列表是数据容器中的一类，是一次性可以存储多个数据(元素)的
# 定义:列表名称=[元素1，元素2，元素3，元素4，元素5...]       s = [54, 15, 75, 108, 23, 78, 75]

# 特点:
# 可以存储不同类型的元素
# 元素有序、可以重复、元素可以修改

#注意:从前向后(正向索引)，下标从0开始;从后向前(反向索引)，下标从-1开始。
#容器中的元素按特定顺序排列的、可通过索引访问的容器类型称之为序列

s=[56,90,88,65,90,"A","Hello",True]
print(type(s))

#访问列表元素
#获取
print(s[0])
print(s[-8])

print(s[2])
print(s[-6])

#修改
s[5]="ABC"
print(s)

#删除
del s[6]
print(s)

#遍历
for item in s:
    print(item)

# 列表 - 切片
# 介绍: 切片是指对操作的数据截取其中一部分的操作。列表、字符串、元组都支持切片操作。

# 语法:序列数据[开始索引:结束索引:步长]
# 不包含结束索引位置对应的元素(开始索引未指定默认为0;结束索引未指定默认为列表长度(直到列表末尾);步长未指定默认为1)
# 索引采用正向、反向索引都可以
# 步长是选取间隔，默认步长为1

s=["A","C","H","K","L","B","D","X","C","U"]

#切片操作  s[开始索引：结束索引：步长]
print(type(s[0:5:1]))
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[:5:2])
print(s[0:-2:1])

#列表的常用方法就是指列表这种数据类型内置的常见功能(添加元素、删除元素、排序等)。
#     方法                            作用                                          样例
# append()                        在列表的尾部追加元素                                s.append (10086)
# insert()                    在指定索引之前，插入该元素                               s.insert(0, 92)
# remove()                        移除列表中第一个匹配到的值                           s.remove(75)
# pop()               删除列表中指定索引位置的元素(如果未指定索引，默认删最后一个)           s.pop(2)/s.pop()
# sort()                  对列表进行排序(列表元素的数据类型一致，才可以进行排序)            s.sort()
# reverse()                       反转列表元素                                      s.reverse()
#对象.方法（参数）

s= [56, 90, 88, 65, 90,100,209, 72, 145]
print(s)
#append():在列表尾部追加元素
s.append(188)
print(s)
#insert():在指定索引之前，插入元素
s.insert(2,80)
print(s)
#remove():移除列表中第一个匹配到的元素
s.remove(90)
print(s)
# pop():删除列表中指定索引位置的元素并返回(如果未指定，默认删除最后一个)
e = s.pop(1)
print(e)
e = s.pop()
print(e)

#sort():排序
s.sort()
print(s)
#reverse():反转列表元素
s.reverse()
print(s)

#将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值

# num_list=[]#空列表
#
# for i in range(10):
#     num=int(input("请输入一个有效的数字："))
#     num_list.append(num)
# print("数字列表:",num_list)
#
# num_list.sort()
# print("排序后：",num_list)
#
# print("最小值:",num_list[0])
# print("最大值:",num_list[9])
#
# print("平均值",sum(num_list)/len(num_list))

#合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
#
# new_list=[]
# for num in num_list1:
#     if num not in new_list:      #判断num元素是否已经存在在new_list中   存在则返回true
#         new_list.append(num)
# print("去除重复元素后的列表",new_list)

#合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# #简化合并
# #解包：将列表这一类容器解开成一个一个独立的元素
# #组包：将多个值合并到一个容器
# num_list=[*num_list1,*num_list2]
# print(num_list)

# new_list=[]
# for num in num_list:
#     if num not in new_list:      #判断num元素是否已经存在在new_list中   存在则返回true
#         new_list.append(num)
# print("去除重复元素后的列表",new_list)


#合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# num_list = num_list1+num_list2
# print(num_list)
#
# new_list=[]
# for num in num_list:
#     if num not in new_list:      #判断num元素是否已经存在在new_list中   存在则返回true
#         new_list.append(num)
# print("去除重复元素后的列表",new_list)

# 如何判断一个元素是否存在于列表之中?
# 可以使用in运算符，语法为:元素in列表
# 返回结果为布尔值，True表示存在，False表示不存在

# 1.生成1-20的平方列表。
# num_list=[]
# for i in range(1,21):   #传统方式
#     num_list.append(i**2)
# print(num_list)

#方式二:列表推导式--->就是按照一定的规则快速生成一个列表的方法-->语法格式1:[要插入的值 for i in 序列/列表]
num_list2=[i**2 for i in range(1,21)]
print(num_list2)

# 2.从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
#列表推导式--->就是按照一定的规则快速生成一个列表的方法-->语法格式2:[要插入的值 for i in 序列/列表   if 条件]
num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
new_list=[i**2 for i in num_list if i%2==0]
print(new_list)

