import pytest
import addition

class TestAddition:
    def test_addition(self):
        assert addition.add(1, 2) == 3
    def test_subtraction(self):
        assert addition.add(1, -2) == -1
    def test_zero(self):
        assert addition.add(0, 0) == 0
    def test_float(self):
        assert addition.add(1.1,1.1) == 2.2
    def test_int_flot(self):
        assert addition.add(1,2.1) == 3.1

    def test_addition_int_string(self):
        with pytest.raises(TypeError):
            addition.add(1,"1")

if __name__ == '__main__':
    pytest.main()

# Both pytest and unittest looks very similar