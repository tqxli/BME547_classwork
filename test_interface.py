import pytest 

@pytest.mark.parametrize("level, expected", [
    (85, "Normal"),
    (45, "Borderline Low"),
    (20, "Low"),
])
def test_check_HDL(level, expected):
    from interface import check_HDL

    answer = check_HDL(level)
    assert answer == expected  