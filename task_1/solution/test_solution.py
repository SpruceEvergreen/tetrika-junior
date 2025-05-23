from solution import sum_two, say_hello
import pytest

def test_sum_two():
    result = sum_two(3, 4)
    assert result == 7, "3 + 4 should be 7. Both ints, test passed"

def test_sum_two_invalid_type():
    # with pytest.raises(TypeError, match="4.3 is not of the type <class 'int'>"):
    with pytest.raises(TypeError):
        sum_two(3, 4.3)
        sum_two(3, True)
        sum_two(3, "4.3")

def test_say_hello():
    result = say_hello("John", "Doe")
    assert result == "Hello, John Doe!", "Both str, test passed"

def test_say_hello_invalid_types():
    with pytest.raises(TypeError):
        say_hello("John", 5)
        say_hello("John", False)
        say_hello("John", 5.3)


