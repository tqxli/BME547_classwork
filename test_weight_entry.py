import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("35.6 kg", 36),
    ("-22 lb", -10),
    ("22 LB", 10),
    ("22 pound", 10),
    # ("ten kg", None),
    ("22", None),
    ("22 lb 50 kg", None),
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0.1, 0.2, 0.3),
])
def test_add_number(a, b, expected):
    from weight_entry import add_number
    answer = add_number(a, b)
    assert answer == pytest.approx(expected)
