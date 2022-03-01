from case.cala_case import Cala
import pytest
import yaml

"""
    pytest命令参数
        -k  包含
            举例
                pytest -k 'add or ride' 03_test_cala.py 表示只运行包含add或者ride的测试用例
        
        --collect-only 表示查看当前文件内有多少测试用例(每条测试数据为一条) 只收集 而不执行
            举例
                pytest --collect-only 03_test_cala.py
    
        --junit-xml 生成一个执行结果(测试设备/失败成功用例条数等详细信息)的xml文件
            举例
                # 指定目录及文件名
                pytest --junit-xml=./result.xml 03_test_cala.py


"""


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
