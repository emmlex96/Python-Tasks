price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))

discount_amount = price * (discount / 100)
final_price = price - discount_amount

print(f"Discount amount: {discount_amount:.2f}")
print(f"Final price: {final_price:.2f}")
