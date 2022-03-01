from case.cala_case import Cala
import pytest
import yaml


class Test_cala(object):
    # 全局变量 指定测试数据
    # 加减法共用一套测试数据 加法成功的数据case 减法则失败
    add_subtraction_yaml = yaml.load(open('../data/add_subtraction_cala.yml'), Loader=yaml.Loader)

    # 乘除法共用一套测试数据 乘法成功的数据case 除法则失败
    division_ride_yaml = yaml.load(open('../data/division_ride_cala.yml'), Loader=yaml.Loader)

    # 初始化
    @pytest.fixture(autouse=True)
    def initialization(self):
        self.cala = Cala()

    # c参数代表期望结果
    # 调用方法返回的result代表实际结果
    @pytest.mark.parametrize('a, b, c', add_subtraction_yaml)
    def test_add(self, a, b, c):
        result = self.cala.add(a, b)
        assert result == c

    @pytest.mark.parametrize('a, b, c', add_subtraction_yaml)
    def test_subtraction(self, a, b, c):
        result = self.cala.subtraction(a, b)
        assert result == c

    @pytest.mark.parametrize('a, b, c', division_ride_yaml)
    def test_ride(self, a, b, c):
        result = self.cala.ride(a, b)
        assert result == c

    @pytest.mark.parametrize('a, b, c', division_ride_yaml)
    def test_division(self, a, b, c):
        result = self.cala.division(a, b)
        assert result == c


if __name__ == '__main__':
    pytest.main(['-vs'])
