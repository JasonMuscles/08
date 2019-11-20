class Cat:
    def __init__(self):
        print("初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "Tom"


# 使用类名（）创建对象的时候，会自调用初始化方法__init__
tom = Cat()

print(tom.name)
 