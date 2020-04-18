"""
multiprocessing 模块创建进程示例

步骤:
1. 编写进程函数
2. 实例化进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep
a = 1
# 进程函数
def fun():
    global a
    a = 1000
    print("结束一个进程")
if __name__ == '__main__':
    # 创建进程对象
    p = mp.Process(target=fun)
    # 启动进程 (进程产生,自动执行 fun函数 作为一个进程的执行内容)
    p.start()
    # 回收进程
    p.join()

    print("a =",a)







