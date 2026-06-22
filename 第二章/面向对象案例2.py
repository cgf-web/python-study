# 采用面向对象编程思想完成如下需求
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# 5.退出购物车

def menu():
    print("---------------------------------")
    print("----------0.退出系统-------------")
    print("--------1.添加商品到购物车------")
    print("--------2.修改商品信息-----------")
    print("--------3.删除商品信息-----------")
    print("------4.查询购物车商品信息------")
    print("---------------------------------")

class goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称:{self.name}，商品价格:{self.price}，商品数量:{self.num}"

    def update_goods(self,name=None,price=None,num=None):
        if name is not None:
            self.name=name
        if price is not None:
            self.price=price
        if num is not None:
            self.num=num
        return self


class ShoppingCart:
    def __init__(self):
        self.cart_list = []


    def add_goods(self):       
        name = input("请输入商品名称:")
        if name in [s.name for s in self.cart_list]:
            print("商品名称已存在，不能重复添加")
            return 
        price = input("请输入商品价格:")
        if price == "":
            print("商品价格不能为空")
            return
        num = input("请输入商品数量:")
        if num == "":
            print("商品数量不能为空")
            return
        good = goods(name, float(price), int(num))
        self.cart_list.append(good)

    def update_goods(self):
        name = input("请输入要修改的商品名称:")
        for item in self.cart_list:
            if item.name == name:
                price = input("请输入新的商品价格:")
                num = input("请输入新的商品数量:")
                item.update_goods(price=float(price), num=int(num))
                print("修改成功")
                return
        print("商品名称不存在")

    def delete_goods(self):
        name = input("请输入要删除的商品名称:")
        for item in self.cart_list:
            if item.name == name:
                self.cart_list.remove(item)
                print("删除成功")
                return
        print("商品名称不存在")

    def query_goods(self):
        for item in self.cart_list:
            print(item)



    def run(self):
        while True:
            menu()
            choice = input("请输入您的选择:")
            if choice == "0":
                print("退出系统，欢迎下次光临")
                break
            elif choice == "1":
                self.add_goods()
            elif choice == "2":
                self.update_goods()
            elif choice == "3":
                self.delete_goods()
            elif choice == "4":
                self.query_goods()
            else:
                print("输入有误，请重新输入")


if __name__=="__main__":
    sc=ShoppingCart()
    sc.run()
