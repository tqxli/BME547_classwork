def test_get_value_on_line():
    from line import get_value_on_line

    answer = get_value_on_line((1, 1), (3, 3), 2)
    expected = 2
    assert answer == expected