class Cat:

    def eat(self):
        # 那个对象调用方法，self就是哪一个对象的引用（Tom/大懒猫）
        print("%s吃鱼" % self.name)

    def drink(self):
        print("%s喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用  .属性名  利用赋值语句可实现(不推荐通过这种方式)
tom.name = "Tom"

tom.eat()
tom.drink()

# 不推荐在类的外部给对象加属性
# tom.name = "Tom"
