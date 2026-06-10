from discount import calculate_discount

def test_tc01():
    # TC01: Tổng trước 60M, đơn mới 2M -> Đã đạt từ trước nên được giảm 10% (0.1)
    assert calculate_discount(60000000, 20000000) == 0.1

def test_tc02():
    # TC02: Tổng trước 30M, đơn mới 2M -> Chưa đủ 50M -> Không giảm (0.0)
    assert calculate_discount(30000000, 20000000) == 0.0

def test_tc03():
    # TC03: Tổng trước 49M, đơn mới 2M -> Cộng lại = 51M (Đạt từ 50M trở lên) -> Được giảm 10% (0.1)
    assert calculate_discount(49000000, 20000000) == 0.1