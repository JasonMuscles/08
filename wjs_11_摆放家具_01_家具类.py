class HomeItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        print("[%s] 占地 %.2f" % (self.name, self.area))

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


# 创建家具
bed = HomeItem("席梦思", 4.0)
chest = HomeItem("衣柜", 2.0)
table = HomeItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

