day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

is_leap = (year % 4 == 0 and year % 100 != 0) 
    days_in_month[2] = 29

if 1 <= month <= 12 and 1 <= day <= days_in_month[month] and year > 0:
    print("Valid date")
else:
    print("Invalid date")
