a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

numbers = sorted([a, b, c], reverse=True)
print(f"Descending order: (numbers(0)), (numbers(1)), (numbers(2))")
