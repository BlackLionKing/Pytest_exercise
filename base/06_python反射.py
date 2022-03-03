class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s吃粑粑" % self.name)

# 正常调用
# p = Person('haha')
# p.eat()


# 反射
p = Person('haha')
# find = getattr(p, 'eat')    # 查找p对象内有没有eat方法
# find()  # 执行

# print(getattr(p, 'age', '20'))  # 查找p对象内有没有age方法或属性 如果没有就输出20

print(hasattr(p, 'eat'))    # 判断p对象内是否有eat方法或属性 返回true或false


