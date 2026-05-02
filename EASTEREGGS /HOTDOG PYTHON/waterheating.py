mass float(input("enter amount of water in kilogram: "))
initial_temp = float(input("Enter inital temperature (c): "))
final_temp = float(input("enter final temperature(c): "))

q = mass * (final_temp - initial_temp) *4184
print(f"energy needed to heat water: (q:2f) joules")
