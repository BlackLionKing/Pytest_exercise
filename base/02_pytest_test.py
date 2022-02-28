from case.test_case import Add


# class Test_add(object):
def test_add_case():
    add_test = Add()
    add = add_test.test_add(1, 3)
    print(add)
    assert add == 4

