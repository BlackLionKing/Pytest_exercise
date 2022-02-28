
"""
    在命令行运行此文件 会报错
        ModuleNotFoundError: No module named 'case'

    需手动加上路径 让python去查找上个目录下的文件
        sys.path.append('..') ..代表上个目录
        sys需要写在文件最上面

"""

import sys
import unittest

sys.path.append('..')
from case.test_case import Add


class Test_unit(unittest.TestCase):
    def test_add(self):
        # 初始化对象
        self.test = Add()
        # 传参 接收返回
        self.add = self.test.test_add(1, 3)
        print(self.add)
        self.assertEqual(self.add, 4)


if __name__ == '__main__':
    unittest.main()
