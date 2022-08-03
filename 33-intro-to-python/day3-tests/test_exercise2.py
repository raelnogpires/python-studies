from exercise2 import find_phone_number_by_phrase


def test_func_coding_into_phone_number():
    assert find_phone_number_by_phrase("HOME-SWEET-HOME") == "4663-79338-4663"


def still_test_func_coding_into_phone_number():
    assert find_phone_number_by_phrase("HEAVEN-KNOWS") == "432836-56697"


def passed_only_numbers_returns_just_the_numbers():
    assert find_phone_number_by_phrase("123456789") == "123456789"
