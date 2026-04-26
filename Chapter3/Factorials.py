"""
PSEUDOCODE:
INPUT non-negative integer n
SET factorial = 1
FOR i FROM 1 TO n:
factorial *= i
PRINT factorial
"""
def exercise_3_13():
print("\n=== 3.13 Factorial ===")
n = int(input("Enter a non-negative integer: "))
factorial = 1
for i in range(1, n + 1):
factorial *= i
print(f"{n}! = {factorial}")
