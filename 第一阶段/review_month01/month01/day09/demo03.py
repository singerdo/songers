"""
    函数参数
        函数实参
"""


# 默认形参：当实参不传递时，使用默认值
def func01(p1=0, p2=None, p3=0):
    print(p1)  # 1
    print(p2)  # 2
    print(p3)  # 3


# 1.  位置实参： 根据位置(顺序)传递
# 作用：函数调用者给函数定义者 传递信息的最常用方式
# 适用性：需要传递全部参数
func01(1, 2, 3)

# 2.    序列实参：将序列拆分后按位置传递           【拆】
# 作用： 使用容器思想封装参数
list01 = [1, 2, 3]
func01(*list01)

# 3. 关键字实参: 根据关键字(形参名称)传递
# 作用： 通过名称指定形参(可以更有针对性传递,不用全部传递)
# 适用性：需要传递部分参数
# func01(p2=2, p3=3, p1=1)
func01(p3=3)  #

# 4.   字典实参：将字典拆分后按关键字传递         【拆】
# 作用： 使用容器思想封装参数
dict01 = {"p3": 3, "p1": 1, "p2": 2}
func01(**dict01)

