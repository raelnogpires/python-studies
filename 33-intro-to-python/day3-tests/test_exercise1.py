import pytest
from exercise1 import number_list_or_fizz_buzz

fizz = [1, 2, "Fizz"]
buzz = [1, 2, "Fizz", 4, "Buzz"]
fizz_buzz = [
    1, 2, "Fizz", 4, "Buzz", "Fizz", 7,
    8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"
]


def test_func_when_appear_just_fizz():
    assert number_list_or_fizz_buzz(4) == fizz


def test_func_when_appear_fizz_and_buzz():
    assert number_list_or_fizz_buzz(6) == buzz


def test_func_when_appear_fizz_buzz_and_fizzbuzz():
    assert number_list_or_fizz_buzz(16) == fizz_buzz


def test_if_error_is_thrown_when_param_not_number():
    with pytest.raises(ValueError, match="invalid literal for int()"):
        number_list_or_fizz_buzz("s")
