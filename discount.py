def calculate_discount(total_past_spending, current_order_value):
    if total_past_spending >= 50000000:
        return 0.1  # Giảm 10%
    return 0.0