import pytest


class Cala(object):
    def add(self, a, b):
        # 返回实际结果
        return a + b

    def subtraction(self, a, b):
        return a - b

    def ride(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            pytest.raises(ZeroDivisionError, match='除数不可为0')
        return a / b
