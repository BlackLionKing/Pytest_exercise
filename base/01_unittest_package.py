
"""
    在命令行运行此文件 会报错
        ModuleNotFoundError: No module named 'case'

    需手动加上路径 让python去查找上个目录下的文件
        sys.path.append('..') ..代表上个目录
        sys需要写在文件最上面

"""

import sys
sys.path.append('..')
from case.unittest_case import Test_unittest

# 初始化对象
test = Test_unittest()
# 传参 接收返回
add = test.test_add(1, 3)
print(add)
