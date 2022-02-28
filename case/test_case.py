"""
    使用pytest执行此条case时 类名不能以Test开头 否则会单独执行此case

"""


class Add(object):
    def test_add(self, a, b):
        return a + b
