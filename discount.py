def calculate_discount(previous_total, current_order):
    if previous_total >= 50000000:
        return 0.1

    if previous_total + current_order >= 50000000:
        return 0.1

    return 0