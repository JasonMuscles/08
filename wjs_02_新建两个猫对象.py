class Cat:

    def eat(self):
        print("吃鱼")

    def drink(self):
        print("喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

# 再创建一个猫对象
# lazy_cat 和tom不是同一个对象
lazy_cat = Cat()

lazy_cat.drink()
lazy_cat.eat()

print(lazy_cat)

# 是同一个对象
lazy_cat2 = lazy_cat
