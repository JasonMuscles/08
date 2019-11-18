class Cat:

    def eat(self):
        print("吃鱼")

    def drink(self):
        print("喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)
addr = id(tom)

# %d（10进制输出）%x（16进制输出）
print("%d" % addr)
