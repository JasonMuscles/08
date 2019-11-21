class Gun:
    def __init__(self, model):

        # 1.抢的型号
        self.model = model
        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹数量
        if self.bullet_count <= 0:

            return "「%s」哦豁~  子弹打空了！！！" % self.model

        # 2.发射子弹 -1
        else:
            self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s]biu biu~~~~[%d]"
              % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 1. 姓名
        self.name = name

        # 2. 枪（新兵没有枪）
        self.gun = None

    def fire(self):
        # 1 > 判断是否有枪，没有枪没法冲锋
        # if self.gun == None:
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        # 2 > 喊一声口号
        print("%s冲向前方..." % self.name)
        # 3 > 装填子弹
        self.gun.add_bullet(50)
        # 4 > 射击
        self.gun.shoot()


# 1. 创建一个抢对象
ak47 = Gun("AK47")


# 2. 创建一个士兵
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)

