import pytest
from dates import check_date
from datetime import date


def test_check_true():
    assert check_date(date(1998, 11, 15)), "WORKS WRONG"


def test_check_false():
    assert not check_date(date(3000, 11, 15)), "WORKS WRONG"


if __name__ == "__main__":
    pytest.main()
    # print(check_date(date(1998, 11, 15)))
