def calculate_tip(bill, percent):
    """Calculate and return the tip amount."""
    if bill < 0 or percent < 0:
        raise ValueError("bill and tip percentage must not be negative")
    return bill * (percent / 100)


bill_amount = float(input("what was your bill?"))
tip_percent = float(input("what percentage do you want to tip?"))

tip = calculate_tip(bill_amount, tip_percent)
total = bill_amount + tip
print(f"tip amount: ${tip:.2f}")
print(f"total to pay: ${total:.2f}")

