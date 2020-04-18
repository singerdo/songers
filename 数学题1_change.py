'''
列表内的数字每一位都等于前两位之和+1，问类表内任意数量的数字之和是否可能相等
'''
list1=[1,2,4,7]
list2=[]
for i in range(4):
    for l in range(i+1,5):
        list2.append(list1[i]+list1[l])
for i in range(3):
    for l in range(i+1,4):
        for m in range(l+1,5):
            list2.append(list1[i]+list1[l]+list1[m])
for i in range(5):
    r=list1.pop(0)
    print(sum(list1))
    list2.append(sum(list1))
    list1.append(r)
print(list2)
list2.sort()
print(list2)