class Wife:
    def __init__(self, age=0):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if 16 < value <= 30:
            self.__age = value
        else:
            # raise 抛出
            raise Exception("我不要")
try:
    w01 = Wife(59)
    print(w01.age)
    w01 = Wife(20)
    print(w01.age)
except:
    print("那你再等等吧")
    w01 = Wife(21)
    print("如果返回没有输出20，只输出21，说明错误发生后会跳过try和except之间的语句，从except开始向下执行，返回结果为：",w01.age)
