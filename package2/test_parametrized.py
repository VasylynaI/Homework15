import pytest


@pytest.mark.param
@pytest.mark.parametrize('param', [1, 2, 3])
def test_1_param(param):
    assert isinstance(param, int)


@pytest.mark.param
@pytest.mark.parametrize('value1, value2', [(1, 1), (2, 2), (3, 3)])
def test_2_param(value1, value2):
    assert value1 == value2


@pytest.mark.param
@pytest.mark.parametrize('param_alias', [('foo', 1), ('bar', 2), ('baz', 3)],
                         ids=['first', 'second', 'third'])
def test_3_param(param_alias):
    name, value = param_alias
    assert isinstance(value, int)
