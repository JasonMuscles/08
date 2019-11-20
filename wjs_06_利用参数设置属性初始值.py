class Cat:
    def __init__(self, new_name):
        print("初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 使用类名（）创建对象的时候，会自调用初始化方法__init__
tom = Cat("Tom")

print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()

