run = float(input("enter take-off speed run (m/s): "))
way = float(input("enter acceleration way (m/s * 2): "))

length = (run ** 2) / (2 * way)
print(f"minimum runway length needed: (length:.2f) meters")
