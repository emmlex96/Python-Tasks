"""
INPUT principal
FOR year FROM 1 TO 30:
principal = principal * 1.07
PRINT year, principal

"""

print("7% Investment Return")
principal = float(input("Enter initial investment ($): "))
print(f"\n{'Year':>6}{'Amount':>14}")
for year in range(1, 31):
    principal *= 1.07
    print(f"{year:>6}{principal:>14,.2f}")
