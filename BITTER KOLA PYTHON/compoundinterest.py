balance = float(input("Enter bank balance (₦): "))
rate = float(input("Enter annual interest rate (%): ")) / 100

for year in range(1, 4):
    balance_after = balance * ((1 + rate) ** year)
    print(f"After (year) year(s): ₦(balance_after:,.2f))")
