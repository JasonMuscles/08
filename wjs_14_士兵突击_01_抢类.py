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
            print("「%s」子弹打空了！！！" % self.model)

            return

        # 2.发射子弹 -1
        else:
            self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s]biu biu~~~~[%d]" % (self.model, self.bullet_count))


# 创建一个抢对象
ak47 = Gun("AK47")
ak47.add_bullet(60)
ak47.shoot()



