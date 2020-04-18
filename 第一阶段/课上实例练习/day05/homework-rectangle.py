#length=int(input("请输入组成矩形的边长："))
#length_line="*"*length 不长的放在下面算式里一起算
#print(length_line)#如果数量多，
#d=" "*(length-2)
#for i in range(length-2):
#    print("*%s*" % d)
#print(length_line)

#改进
number=int(input("请输入边长:"))
for i in range(number):
    if i==0 or i==(number-1):#就用if语句放在for循环里，独辟蹊径的作用
        print("*"*number)
    else:
        print("*"+" "*(number-2)+"*")


