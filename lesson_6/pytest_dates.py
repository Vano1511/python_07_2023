import pytest
from datetime import date


MIN_DATE = date(1, 1, 1)
MAX_DATE = date(2025, 12, 31)


def check_date(dat: date) -> bool:
    if MIN_DATE <= dat <= MAX_DATE:
        return True
    else:
        return False


def test_check_true():
    assert check_date(date(1998, 11, 15)), "WORKS WRONG"


def test_check_false():
    assert not check_date(date(3000, 11, 15)), "WORKS WRONG"


if __name__ == "__main__":
    pytest.main()
    # print(check_date(date(1998, 11, 15)))
