import math

n = int(input("Enter a positive integer: "))
root = math.isqrt(n)

if root * root == n:
    print(f"{n} is a perfect square (√{n} = {root})")
else:
    print(f"{n} is NOT a perfect square")
