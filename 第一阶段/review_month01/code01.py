"""
    课程一：
        1. Python简介
                执行过程：源代码 -- "编译" --> 字节码 -- 解释 --> 机器码
                                        导入的模块
                            |————1次———|
                        "编译" 目的：提高速度
                        解释 目的：跨平台
        2. pycharm常用快捷键：略(自行查找)
        3. Python语言自动化内存管理机制
             (1) 引用计数:每个对象记录被变量绑定(引用)的数量,当为0时被销毁。
                    缺点：循环引用
             (2) 标记清除：内存全盘扫描,标记不再使用的垃圾对象.
                    缺点：速度慢
             (3) 分代回收：将内存空间划分为多代(0小/1中/2大),新创建的对象都会在0代分配空间.
                   升代：当内存告急时,执行标记清除,将可用数据存入下一代,当代内存清空.
             内存优化：尽少产生垃圾,对象池(字符串/数值/bool...),设置分代回收参数.
                对象池:每当创建对象时,在池中判断是否具有相同对象,
                      如果有返回地址,否则创建新对象.
                      价值：提高内存利用率,避免频繁创建销毁对象
        4. 语句
                循环语句：重复执行
                跳转语句：后续代码不在执行,跳过/跳出/退出

        5. 容器
            (1)各种容器特点：
                字符串：存储字符编码,不可变序列
                元组：存储变量,不可变序列
                列表：存储变量,可变序列
                字典：存储键值对,可变散列
                集合：存储键,可变散列
            (2)基础概念：
                Python语言数据类型：可变、不可变
                    可变：预留空间,可以在原对象基础上修改(如果预留的空间不足也可以扩容)
                    不可变：按需分配,所有改变都会产生新对象.
                序列:有顺序,内存连续.
                     定位灵活(索引、切片),节省内存.
                散列：无顺序,内存不连续.
                     定位迅速(k -> v),占用内存过多.
            (3)基础操作：
                常用功能：详见文档
                索引：定位当个元素
                切片：定位多个元素
        6. 函数：
            设计理念：小而精
            函数参数：
                实际参数：对应
                    位置实参：按照顺序与形参对应
                        序列实参:将序列拆分后,按照顺序与形参对应   【拆】
                    关键字实参：按照名称与形参对应
                        字典实参：将字典拆分后,按照名称与形参对应   【拆】
                形式参数：约束
                    默认形参：可选
                    位置形参：必填
                        星号元组形参：位置实参数量无限  【合】
                    命名关键字形参：必须使用关键字实参
                        双星号字典形参：关键字实参数量无限  【合】

"""


# 6.
def func01(p1, p2, p3):
    pass


func01(1, 2, 3)
func01(*[1, 2, 3])  # 拆


def func02(*args):  # 合  (1,2,3)
    for item in args:  # 使用时不写*
        print(item)


func02()
func02(1, 2, 3)
func02(*[1, 2, 3])


def func03(p1=0, p2=0, p3=0):
    pass


func03(p2=2)

dict01 = {"p1": 1, "p3": 3, "p2": 2}
func03(**dict01)


# 必须使用关键字实参
def func04(*args, p1, p2=0):
    pass


def func05(*, p1, p2=0):
    pass


func04(p1=1)
func05(p1=1, p2=2)
# 关键字参数优势：通过名称指定可以不传其他参数,也可以增加代码可读性
print("双儿", "阿柯", "苏荃", sep="-", end="-")
print("双儿", "阿柯", "苏荃", sep="-")


def func06(**kwargs):# {"a":1,"b":2}
    pass


func06()
func06(a=1, b=2)

# 3.
list01 = []
list02 = []
list01.append(list02)
list02.append(list01)
del list01, list02

# 不要频繁修改不可变对象
str_result = ""
for i in range(10):
    # ""  + "0"  -->  "0"
    # "0"  + "1"  -->  "01"
    # "01"  + "2"  -->  "012"
    str_result = str_result + str(i)
print(str_result)

# 改为可变对象修改,最后再生成不可变对象。
list_result = []
for i in range(10):
    list_result.append(str(i))
print("".join(list_result))

data01 = (123, 32, 4)
data02 = (123, 32, 4)
print(id(data01), id(data02))

# 4.
# 根据条件重复
# while True:
#     # ...
#     if input("输入y退出：") == "y":
#         break
#
#     if input("输入y跳过：") == "y":
#         continue
#     # ...

# 遍历可迭代对象
for item in "我是齐天大圣孙悟空":
    print(item)

# 根据次数重复
for __ in range(5):  # 0 1 2 3 4:
    pass

# 5.
tuple01 = (1, 2, 3, 4)
print(tuple01[0])

list01 = [1, 2, 3]
list02 = [4, 5, 6]
# 切片修改：遍历右侧可迭代对象,依次存储左侧定位的区域.
list01[::-1] = list02
# 切片读取：创建新列表
list03 = list02[::-1]
print(list01)
