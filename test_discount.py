from discount import calculate_discount

def test_tc01():
    assert calculate_discount(60000000, 20000000) == 0.1

def test_tc02():
    assert calculate_discount(30000000, 20000000) == 0.0

def test_tc03():
    assert calculate_discount(49000000, 20000000) == 0.1