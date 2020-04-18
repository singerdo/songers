import random
sum=0
for count in range(5):
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=int(input("%d+%d=："%(a,b)))
    if c==(a+b):
        print("答对了，好棒")
        sum+=10
    else:
        print("很遗憾，打错了")
        sum-=5
print("满分50分，你的总分为%d分"% sum)