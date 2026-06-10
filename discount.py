def calculate_discount(total_past_spending, current_order_value):
    # Khách hàng thân thiết có tổng mua hàng từ 50 triệu trở lên trong năm
    # Cố tình viết thiếu logic cộng dồn đơn hàng mới để tạo bug theo yêu cầu bài lab
    if total_past_spending >= 50000000:
        return 0.1  # Giảm 10%
    return 0.0