def test_check_HDL():
    from interface import check_HDL

    answer = check_HDL(85)
    expected = "Normal"
    assert answer == expected

    answer = check_HDL(45)
    expected = "Borderline Low"
    assert answer == expected

    answer = check_HDL(20)
    expected = "Low"
    assert answer == expected    