u = float(input("enter initial velocity (m/s): "))
t = float(input("enter time span (seconds): "))
a = float(input("enter acceleration (m/s*2): "))

distance = u * t * 0.5 * a * t ** 2
print(f"distance covered:(distance:.2f) meters")
