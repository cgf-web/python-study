# 字符串
# 介绍:字符串是字符的容器，一个字符串中可以存放任意数量的字符。如:"Python" 'Python'  """Python"n"
#特点:不可变性(无法修改)、有序性、可迭代性。
#字符串中的每一个字符元素都有其对应的下标(索引)，通过元素对应的索引，就可以获取到对应的元素。
#注意:从前向后(正向索引)，下标从0开始;从后向前(反向索引)，下标从-1开始。

# 介绍:切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
# 语法:序列对象[开始索引:结束索引:步长]

s="hello-python"
print(s[4])
print(s[-8])

#s[4]="x"  #字符串是常量，不可修改
for i in s:
    print(i)

print(s[0:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:])
print(s[6::])

print(s[:5:2])
print(s[-1:-7:-1])
print(s[::-1])#整个字符串反转

# 方法                                      作用                                                  样例
# find()                  在字符串中查找子串，返回第一次出现:的索引位置，找不到返回-1                 s.find('Python')
# count()                 统计子串在字符串中出现的次数                                          s.count('H')
# upper()                 将字符串中的所有字母转换为大写                                         s.upper()
# lower()                 将字符串中的所有字母转换为小写                                         s.lower()
# split()                 将字符串按指定分隔符分割成列表                                         s.split(' ')
# strip()                 去除字符串两端的空白字符或指定字符                                      s.strip() /s.strip('*')
# replace()               将字符串中的指定子串替换为新的子串。                                    s.replace('H','C')
# startswith()            检查字符串是否以指定子串天干头，返回布尔值                               s.startswith('P')

s = "Hello-Python-Hello-World"
#find()查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)
#count()统计子字符串在指定字符串中出现的次数
c= s.count("o")
print(c)
#upper()转为大写
su = s.upper()
print(su)
#lower()转为小写
sl = s.lower()
print(sl)
#split()将字符串按照指定字符串切割- 列表
slist = s.split("-")
print(slist)
#strip()去除字符串两端的空格
ss=s.strip()
print(ss)
#replace()将字符串中的指定子串替换为新的内容
sr = s.replace("-","_")
print(sr)
#startswith()/endswith()判断字符串是否是以指定的字符串开头/结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

# 1.邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。

# mail=input("请输入邮箱：")
# if mail.count("@")==1 and mail.count(".")>=1:
#     print("邮箱合法")
# else:
#     print("邮箱非法")

#方法二：用in运算符
# mail=input("请输入邮箱：")
# if mail.count("@")==1 and "." in mail:
#     print("邮箱合法")
# else:
#     print("邮箱非法")

# 1.输入一个字符串，判断该字符串是否是回文(两边对称)
# 黄山落叶松叶落山黄
# 上海自来水来自海上
def is_palindrome(s: str) -> bool:
    # 方法1：直接用 Python 切片反转字符串对比
    return s == s[::-1]

# 测试
if __name__ == "__main__":
    s = input("请输入一个字符串：")
    if is_palindrome(s):
        print(f'"{s}" 是回文')
    else:
        print(f'"{s}" 不是回文')


# 2.将用户输入的5个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
result_list = []
# 接收用户输入的5个字符串
for i in range(5):
    s = input(f"请输入第 {i+1} 个字符串：")
    # 1. 反转字符串（切片法）
    reversed_s = s[::-1]
    # 2. 转换为大写
    upper_reversed_s = reversed_s.upper()
    # 3. 存入列表
    result_list.append(upper_reversed_s)

# 遍历输出
print("\n处理后的结果：")
for idx, item in enumerate(result_list, start=1):
    print(f"第 {idx} 个：{item}")







