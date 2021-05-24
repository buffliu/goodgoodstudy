import pytest


class Test:
    @pytest.mark.parametrize('a,b', [(1, 1), (1, 2)])
    def test_01(self, a, b):
        try:
            assert a == b
        except Exception as err:
            raise err

    @pytest.mark.parametrize('c,d', [(1, 1), (1, 2)])
    def test_02(self, c, d):
        assert c== d
if __name__ == '__main__':
    pytest.main('testtry.py')
