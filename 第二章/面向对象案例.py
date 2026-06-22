# 采用面向对象编程思想完成如下需求

# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下:

# 1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    # 1.1输入学生姓名、语文成绩、数学成绩、英语成绩
    # 1.2检查学生姓名是否已存在，如果学生不存在，再添加(存在则，不添加)
    # 1.3 验证成绩范围(0-100分)
    # 1.4 创建学生对象并添加到系统中

# 2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
    # 2.1输入学生姓名、语文成绩、数学成绩、英语成绩
    # 2.2检查学生姓名是否存在，如果学生存在，再修改(不存在则，不修改)
    # 2.3 输入要修改的成绩
    # 2.4 更新学生成绩数据

# 3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
    # 3.1输入学生姓名
    # 3.2检查学生姓名是否存在，如果学生存在，再删除(不存在则，不删除)
    # 3.3 删除学生对象
    # 3.4 提示删除成功

# 4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
    # 4.1输入学生姓名  输出格式为:"姓名:张三|语文:85|数学:90|英语:88|总分:263"
    # 4.2检查学生姓名是否存在，如果学生存在，再查询(不存在则，不查询)
    # 4.3 输出学生信息
    # 4.4 提示查询成功

# 5.展示全部学生成绩:展示出系统中所有学生的成绩     
    # 5.1 遍历系统中所有学生对象
    # 5.2 输出每个学生的姓名、语文成绩、数学成绩、英语成绩、总分
    # 5.3 提示展示成功

def menu():
    print("---------------------------------")
    print("----------0.退出系统-------------")
    print("--------1.添加学生成绩-----------")
    print("--------2.修改学生成绩-----------")
    print("--------3.删除学生成绩-----------")
    print("------4.查询指定学生成绩--------")
    print("------5.展示全部学生成绩--------")
    print("---------------------------------")


class Student:
    
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    
    def __str__(self):#重写__str__方法，返回学生信息   输出格式为:"姓名:张三|语文:85|数学:90|英语:88|总分:263"
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}|总分：{self.chinese+self.math+self.english}"

    def update_score(self,chinese=None,math=None,english=None):#修改学生成绩
        if chinese is not None:   #如果语文成绩不为空，就修改
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english
        self.total=self.chinese+self.math+self.english

class EduManagement:
    system_version="1.0"
    system_name="教务管理系统"

    def __init__(self):
        self.student_list=[]   #列表 记录在校学生的信息

    #添加学生成绩
    def add_student(self):
        # 1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        name = input("请输入学生姓名:")
        if name in [s.name for s in self.student_list]:
            print("学生姓名已存在，不能重复添加")  
            return

        # 1.2 检查学生姓名是否已存在，如果学生不存在，再添加(存在则，不添加)

        chinese = int(input("请输入语文成绩:"))
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))

        # 1.3 验证成绩范围(0-100分)
        if not (0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100):
            print("成绩必须在0-100分之间，添加失败")
            return
          
        # 1.4 创建学生对象并添加到系统中
        student = Student(name, chinese, math, english)   #实例化学生对象，调用__init__方法
        self.student_list.append(student)
        print("添加成功")

    #修改学生成绩
    def update_student(self):
        name=input("请输入要修改的学生姓名:")
        if name not in [s.name for s in self.student_list]:
            print("学生姓名不存在，不能修改")
            return
        # 2.3 输入要修改的成绩
        chinese = int(input("请输入修改的语文成绩:"))
        math = int(input("请输入修改的数学成绩:"))
        english = int(input("请输入修改的英语成绩:"))

        if not (0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100):
            print("成绩必须在0-100分之间，修改失败")
            return
        # 2.4 更新学生成绩数据
        for s in self.student_list:
            if s.name==name:
                s.update_score(chinese,math,english)
                print("修改成功")
                print("修改后成绩为:",s)
                return

    #删除学生成绩
    def delete_student(self):
        name=input("请输入要删除的学生姓名:")
        for s in self.student_list:
            if s.name==name:
                self.student_list.remove(s)
                print("删除成功")
                return
            print("学生姓名不存在，不能删除")
            return

    #查询指定学生成绩
    def query_student(self):
        name=input("请输入要查询的学生姓名:")
        if name not in [s.name for s in self.student_list]:
            print("学生姓名不存在，不能查询")
            return
        for s in self.student_list:
            if s.name==name:
                print("查询成功")
                print(s)
                return

    #展示全部学生成绩
    def show_all_students(self):
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print("欢迎使用" + self.system_name)
        print("系统版本：" + self.system_version)
        print("系统开始运行")
           
        while True:
            menu()
            print()           
            choice=input("请输入您的选择:")
            try:
                if choice=="1":
                    self.add_student()
                elif choice=="2":
                    self.update_student()
                elif choice=="3":
                    self.delete_student()
                elif choice=="4":
                    self.query_student()
                elif choice=="5":
                    self.show_all_students()
                elif choice=='0':
                    print("系统退出  Bye~")
                    break
                else:
                    print("系统运行错误，请重新输入")   
            except ValueError as e:
                print("输入信息有误，请重新输入！：",e)
            except Exception as e:
                print("程序运行出错，请联系管理员！：",e)


if __name__=="__main__":
    em=EduManagement() #实例化教务管理系统对象
    em.run()


# 什么是异常
# 异常(也称为Bug)就是程序运行过程中出现的错误，它会中断程序的正常执行流程。

# 作用:
# 保证数据、逻辑的正确性，避免程序执行混乱
# 在开发阶段，尽量发现更多的问题，尽早解决问题，保障程序正常执行
# NameError   TypeError   IndexError  KeyError  ValueError
# 异常不是坏东西，而是编写健壮程序的重要工具

# 异常处理
# 程序运行过程中出现异常，有两种处理方案:
# 1.不做处理:整个程序因为一个Bug，中断执行。(之前编程的程序)
# 2.捕获异常:按照我们自己的处理方式，处理完异常，程序继续执行。(Python的程序异常处理)

try:
    # 可能出现异常的代码
    pass
except Exception as e:     # 捕获所有异常并赋值给变量e，方便输出异常信息
    # 异常处理代码

    pass

finally:
    # 无论是否发生异常，都会执行的代码
    print("释放资源")
    pass
