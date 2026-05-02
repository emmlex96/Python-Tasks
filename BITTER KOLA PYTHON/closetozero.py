a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

    if abs(a) < abs(b):
        print(f"(a) is closer to zero")
    elif abs(b) < abs(a):
        print(f"(b) is closer to zero")
    else:
        print("Both are equally close to zero")
