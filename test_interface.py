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

@pytest.mark.parametrize("level, expected", [
    (120, "Normal"),
    (150, "Borderline High"),
    (185, "High"),
    (240, "Very High")
])
def test_check_LDL(level, expected):
    from interface import check_LDL

    answer = check_LDL(level)
    assert answer == expected   