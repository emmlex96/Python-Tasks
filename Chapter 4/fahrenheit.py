def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f"{'Celsius':>10} {'Fahrenheit':>12}")
print("-" * 24)
for c in range(101):
    print(f"{c:>10}   {fahrenheit(c):>10.1f}")
