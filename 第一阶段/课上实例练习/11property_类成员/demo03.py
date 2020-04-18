"""
    封装行为
        私有成员
            成员的命名以双下划线开头即可
"""

"""
class MyCalss:
    def __init__(self):
        self.a = 10

    def func01(self):
        pass

# 赤裸
mc01 = MyCalss()
mc01.a = 20
print(mc01.a)

mc01.func01()
"""

class MyClass:
    
    @classmethod
    def Sum1(cls):
        print("你好")

    def __init__(self,a):
        self.__a = a

    def __func01(self):
        pass

# 隐藏：
#     手段：命名以双下划线开头
#     本质：障眼法
#          你看见的是房子,实际他是猴子.
#          你看见的是__a,实际他是_MyCalss__a

mc01 = MyClass(20)
MyClass.Sum1


#print(mc01.__dict__)
#print(MyCalss.__dict__)
# mc01.a = 20# 创建了新实例变量
# print(mc01.a)

# mc01.func01()

# print(mc01.__a)
#print(mc01._MyCalss__a)

#mc01._MyCalss__func01()
