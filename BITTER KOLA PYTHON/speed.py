speed = float(input("Enter speed in km/h: "))

if speed == 0:
    print("Stationary")
elif speed <= 40:
    print("Slow")
elif speed <= 80:
    print("Moderate")
elif speed <= 120:
    print("Fast")
else:
    print("Dangerously Fast")
