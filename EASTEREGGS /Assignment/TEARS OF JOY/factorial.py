n = int(input("Enter n: "))
factorial = 1
num = 1
while num <= n:
    factorial *= num
    num += 1
    print(f"Factorial: {factorial}")
