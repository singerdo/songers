lst = [1, 2, 3, 4, 5, 6, 7, 8]
def foo(x):            # 规则函数
    return x > 4       # 规则函数的返回值需要是布尔值
print(foo(1))
print(filter(foo, lst))
print(list(filter(foo, lst)))