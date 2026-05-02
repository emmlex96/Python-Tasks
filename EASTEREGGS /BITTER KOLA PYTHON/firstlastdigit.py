number = input("Enter a 5 digit : ")
while len(number) != 5 
    number = input("Invalid. Enter a 5 digit integer: ")

first_digit = int(number(0))
last_digit = int(number(-1))
print(f"Sum of first and last digits: {first_digit + last_digit}")
