"""
    封装行为
        属性原理 property - 拦截
            保护实例变量
"""


# 1. 创建类变量(与实例变量名称相同)
# 2. 创建属性(property对象)
# 3. 创建读取方法
# 4. 创建写入方法

# 结论：拦截
#      如果没有以上步骤,操作的是实例变量
#      如果具有以上步骤,操作的是属性(property对象)

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def get_age(self):
        print("你大爷的")#没有返回你大爷的，说明有set的情况下不会经过get（）
        return self.__age
    def set_age(self, value):
        if 16 < value <= 30:
            self.__age = value
        else:
            raise Exception("我不要")
    age = property(get_age, set_age)
w01 = Wife("双儿", 20)
#print(w01.name)
#w01.age = 30
#print(w01.age)
