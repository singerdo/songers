"""
查找列表[4,3,5,57,67,8]中最小元素
    核心思想：
        假设第一个就是最小值
        使用假设的和第二个进行比较,如果发现更小的,则替换假设的
        使用假设的和第三个进行比较,如果发现更小的,则替换假设的
        使用假设的和第...个进行比较,如果发现更小的,则替换假设的
        最后，假设的就是最小的.
"""
list01 = [4, 3, 5, 57, 67, 8]

min_value = list01[0]
for i in range(1, len(list01)):
    if min_value > list01[i]:
        min_value = list01[i]

print(min_value)
