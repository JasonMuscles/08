class Passon:
    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s，我的体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s 爱吃东西，要发胖" % self.weight)

        self.weight += 1


XiaoMing = Passon("小明", 75.0)
XiaoMing.run()
XiaoMing.eat()
print(XiaoMing)
