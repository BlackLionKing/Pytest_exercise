"""
    测试用例执行顺序
        pytest
            按照文件 从上到下依次执行
        unittest
            根据方法名的ascii码排序执行

    改变pytest执行顺序
        安装插件：pytest-ordering
        在方法/函数上指定装饰器 order参数代表排序的值(先后顺序)
            @pytest.mark.run(order=)
"""
import pytest


class Test_cala(object):

    @pytest.mark.run(order=3)
    def test_add(self):
        print('test_add')

    @pytest.mark.run(order=2)
    def test_subtraction(self):
        print('test_subtraction')

    @pytest.mark.run(order=4)
    def test_ride(self):
        print('test_ride')

    @pytest.mark.run(order=1)
    def test_division(self):
        print('test_division')


if __name__ == '__main__':
    pytest.main(['vs'])
