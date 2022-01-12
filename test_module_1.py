from module_1 import StringCalculator


def test_two_one_number_as_argument_addition():
    calculator = StringCalculator('2').addition()
    assert calculator == 2


def test_addition_of_two_one_digit_numbers():
    calculator = StringCalculator('1,2').addition()
    assert calculator == 3


def test_addition_of_two_two_digit_numbers():
    calculator = StringCalculator('14,20').addition()
    assert calculator == 34


def test_addition_of_two_one_digit_numbers_one_negative_addition():
    calculator = StringCalculator('2, -1').addition()
    assert calculator == 1
