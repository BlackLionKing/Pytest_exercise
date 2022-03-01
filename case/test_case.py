"""
    使用pytest执行此条case时 类名不能以Test开头 否则会单独执行此case

"""


class Add(object):
    """
        type hints类型提示
            表示该方法参数 a, b为int类型 返回也为int类型
            只在ide里做提示作用 python并不会为该方法指定int类型

    """
    def test_add(self, a: int, b: int) -> int:
        return a + b
