from main import add_numbers, subtract_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2


# This test is intentionally wrong so you can see what happens when it failss
def test_fail_example():
    assert add_numbers(1, 1) == 32
