print("Separating Digits")
number = int(input("Enter a 5-digit integer: "))
original = number
# Pick off digits from left to right
divisor = 10000
print("Digits (left to right):", end=" ")
while divisor >= 1:
    digit = number // divisor
    print(digit, end=" ")
    number %= divisor
    divisor //= 10
print()
