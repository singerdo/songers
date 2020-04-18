"""
    lambda 表达式
        匿名方法
"""
# 1. 有参数有返回值
func01 = lambda p1, p2: p1 + p2
print(func01(1, 2))

# 2. 无参数有返回值
func02 = lambda: 1000
print(func02())

# 3. 有参数无返回值
func03 = lambda p1, p2: print(p1 + p2)
func03(1, 2)

# 4. 无参数无返回值
func04 = lambda: print("中国加油,武汉加油")
func04()

# 5. lambda 表达式不能赋值
def func05(list_target):

#func05 = lambda list_target:list_target[0] = 10 不适用于lambda

# 6.lambda 表达式只能有一句话
def func06():
    for item in range(3):
        print(item)
func06()
# func06 = lambda:for item in range(3): print(item) 不适用与lambda
