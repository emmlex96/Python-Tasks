a = int(input("Enter the first digit : "))
b = int(input("Enter the second digit: "))

if b != 0 and a % b == 0:
    print(f"(a) is a multiple of (b)")
else:
    print(f"(a) is NOT a multiple of (b)")
