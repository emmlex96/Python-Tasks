a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

if a > 0 and b > 0:
    print(f"Both positive. Sum: (a + b)")
elif a < 0 and b < 0:
    print(f"Both negative. Product: (a * b)")
else:
    print(f"Opposite signs. Difference: (abs(a - b))")
