# 定义函数, 删除列表中相同元素(只保留一个)
# list01 = [6, 54, 65, 677, 6, 65, 6, 65]

# 更节省内存
# def delete_duplicates(list_target):
#     for r in range(len(list_target) - 1, 0, -1):
#         for c in range(r):
#             if list_target[r] == list_target[c]:
#                 del list_target[r]
#                 break
#
# # 测试
# list01 = [6, 54, 65, 677, 6, 65, 6, 65]
# delete_all(list01)
# print(list01)

# 更简单
#def delete_duplicates(list_target):
#    return set(list_target)

# 测试
list01 = [6, 54, 65, 677, 6, 65, 6, 65]
#list01 = delete_duplicates(list01)
#print(list01)

for i in range(len(list01)-1,-1,-1):
    if list01.pop(i) not in list01:
        list01.append(list01.pop(i))
print(list01)
