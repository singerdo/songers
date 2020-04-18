import random
list_bigo=[]
for i in range(6):
    list_bigo.append(random.randint(1,33))
    while list_bigo[i] not in list_bigo[:i]:
        list_bigo[i]=random.randint(1,33)
list_bigo.append(random.randint(1,16))
while list_bigo[6] in list_bigo[:6]:
    list_bigo[6]=random.randint(1,16)
print(list_bigo)

list_guess=[]
for i in range(6):
    list_guess.append(int(input("请输入你选择的第%s个号码（在1-33之间选择，且每次选择的的数字不能重复）：" %(i+1) )))
    print(list_guess)
    while list_guess[i] in list_guess[:i] or list_guess[i]>33 or list_guess[i]<1:
        print("号码与之前的号码重复或者不在规定范围内，请重新选择")
        list_guess[i]=(int(input("请输入你选择的第%s个号码（在1-33之间选择，且每次选择的的数字不能重复）：" %(i+1))))
list_guess.append(int(input("请输入你选择的第7个号码（在1-16之间选择，且每次选择的的数字不能重复）：")))
while list_guess[6] in list_guess[:6] or list_guess[6]>16 or list_guess[6]<1:
        print("号码与之前的号码重复或者不在规定范围内，请重新选择")
        list_guess[6]=(int(input("请输入你选择的第7个号码（在1-16之间选择，且每次选择的的数字不能重复）：")))
print(list_guess)