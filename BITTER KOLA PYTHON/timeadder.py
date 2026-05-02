hours1 = int(input("Enter hours for time 1: "))
minutes1 = int(input("Enter minutes for time 1: "))

hours2 = int(input("Enter hours for time 2: "))
minutes2 = int(input("Enter minutes for time 2: "))

total_minutes = minutes1 + minutes2
extra_hours = total_minutes // 60
remaining_minutes = total_minutes % 60
total_hours = hours1 + hours2 + extra_hours

print(f"Total time: {total_hours:02}:{remaining_minutes:02}")
