#集合(set)
#介绍:集合(set)是一种无序的、不可重复、可修改的数据容器。
#列表[]
#元组()
#集合 {}
#注意:空集合的定义不可以使用{，[表示的是空字典;由于集合是无序的，因此是不支持下标索引访问的。
# from os import P_NOWAITO


# set1 = {1, 2, 3, 4, 5,2,1}
# print(set1)
# print(type(set1))
# set2 = ()#空集合定义

# set3={}#空字典
# print(type(set3))

# 集合(set)中的常见方法:
# 操作	                         含义	                                                样例
# add(...)	                    添加元素到集合中	                                    s1.add('t')
# remove(...)	                移除集合中的指定元素(指定元素不存在将报错)	              s1.remove('t')
# pop()	                        随机删除集合中的元素并返回	                             e = s1.pop()
# clear()	                    清空集合	                                           s1.clear()#清空集合
# difference(...)	     求取两个集合的差集(包含在第一个集合但不包含在第二个集合的元素)	    s1.difference(s2)
# union(...)	                求取两个集合的并集	                                    s1.union(s2)
# intersection(...)	            求取两个集合的交集	                                    s1.intersection(s2)


#add():添加元素到集合
# s1 = {100,200,300,400,500,600,700,800}
# print(s1)

# s1.add(1200)
# print(s1)
# #remove():移除集合中的指定元素(指定元素不存在将报错)
# s1.remove(200)
# print(s1)
# #pop():随机删除集合中的元素并返回
# e = s1.pop()
# print(e)
# print(s1)
# #clear():清空集合
# s1.clear()
# print(s1)
# s2 = {"A", "B", "C", "D", "E", "X", "Y"}
# s3 = {"C", "E", "Y", "Z"}
# # difference():求两个集合的差集(存在于第一个集合，但不存在于第二个集合)
# print(s2.difference(s3))
# print(s3.difference(s2))

# #union():求两个集合的并集
# print(s2.union(s3))
# print(s3.union(s2))
# #intersection():求两个集合的交集
# print(s2.intersection(s3))
# print(s3.intersection(s2))


# 根据提供的班级学生的选课情况，完成如下需求:
# 1.找出同时选修了法语和艺术的学生
# 2.找出同时选修了所有四门课程的学生
# 3.找出选修了足球，但是没有选修篮球的学生

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "虎咆", "姜老道", "天运子", "厉飞雨", "韩立", "紫林"}

# 根据提供的班级学生的选课情况，完成如下需求:
# 1.找出同时选修了法语和艺术的学生
#方式一，求交集
french_art_students = french_set.intersection(art_set)
print(f"同时选修了法语和艺术的学生:", french_art_students)  
#方式二  &
fa_set=french_set & art_set
print(f"同时选修了法语和艺术的学生:", french_art_students)

# 2.找出同时选修了所有四门课程的学生
all_subjects_students = football_set.intersection(basketball_set, french_set, art_set)
print(f"同时选修了所有四门课程的学生:", all_subjects_students)

all_set=football_set&basketball_set&art_set&french_set
print(f"同时选修了所有四门课程的学生:",all_set)

# 3.找出选修了足球，但是没有选修篮球的学生
#求差集 difference
football_not_basketball = football_set.difference(basketball_set)
print(f"选修了足球但没有选修篮球的学生:", football_not_basketball)

#   -号   
fb_set=football_set-basketball_set
print(f"选修了足球但没有选修篮球的学生:",fb_set)

#方式三  集合推导式   快速构建集合，语法  {要往集合中添加的数据  for s in set  if 条件}
fb_set3={s for s in football_set if s not in basketball_set}
print(f"选修了足球但没有选修篮球的学生:",fb_set3)

#4.统计每一个学生选修的课程数量
#1.先获取所有学生名单
#all_set=football_set.union(basketball_set).union(art_set).union(french_set)
all_set1=football_set|basketball_set|french_set|art_set
print(all_set1)  #并集会去重  得到所有学生名单
#2.获取每个学生的选课数量
all_list=[*football_set,*basketball_set,*art_set,*french_set]  #列表，元素可重复   得到所有学生选的所有课出现的名单
for s in all_set1:#s是在all_set1中的每一个元素，即遍历每个学生名字
    print(f"{s}选修了{all_list.count(s)}门课程")  # 统计每个学生在all_list中出现的次数，即为该学生选修的课程数量







