# 文件操作入门
# 日常我们操作文件时，基本分为三步操作:打开、读/写、关闭。

# #1.打开文件
# f= open("resources/望庐山瀑布.txt","r",encoding="utf-8")   #全球最通用，兼容性最好的打开方式
# #2.读取文件
# content = f.read()
# print(content)
# #3.关闭文件
# f.close()


# #1.打开文件
# f= open("resources/静夜思.txt","w",encoding="utf-8")
# #2.写入文件
# f.write("窗前明月光，\n")
# f.write("疑是地上霜。\n")
# f.write("举头望明月，\n")
# f.write("低头思故乡。\n")
# #3.关闭文件
# f.close()

# 编码:是将字符(文字、数字、符号)转换为计算机能够存储和处理的数字代码的规则系统，如:ASCII、GBK、UTF-8

# 注意:如果操作完文件，并未调用close方法关闭文件，同时程序没有停止运行，那么这个文件将一直被Python程序占用，无法进行其他操作。


# f = open("resources/望庐山瀑布.txt","r",encoding="utf-8")
# # content=f.read()    #读取文件内容
# # print(content)

# content_list = f.readlines()    #读取文件内容，返回一个列表，每行一个元素
# for line in content_list:
#     print(line.strip())
# f.close()   #关闭文件



# f=open("resources/静夜思.txt","w",encoding="utf-8")   #打开文件
# f.write("静夜思(李白)\n\n")
# f.write("床前明月光，\n")
# f.write("疑是地上霜。\n")
# f.write("举头望明月，\n")
# f.write("低头思故乡。\n")
# f.close()

# 资源释放
# 在Python中，文件操作完成后，需要调用close方法关闭文件，释放资源。可以使用with语句来自动管理文件的打开和关闭，确保文件在操作完成后被正确关闭，即使发生异常也能保证文件被关闭。

f=open("resources/静夜思.txt","w",encoding="utf-8")   #打开文件
try:
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    #i=1/0
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
except Exception as e:    #捕获所有异常
    print("写入文件时出错：",e)
finally:
    f.close()


# 提示:with语句(上下文管理器)的核心作用就是确保资源的总是被正确获取和释放(即使发生异常，也会被正确释放)，也是项目开发中的推荐方式

with open("resources/静夜思.txt","w",encoding="utf-8") as f:   #打开文件
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")

# with语句会自动管理文件的打开和关闭，因此不需要显式调用close方法
