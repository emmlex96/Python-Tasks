pin = input("Enter a 4-digit PIN: ")

if pin.isdigit() and 1000 <= int(pin) <= 9999:
    print("Valid PIN")
else:
    print("Invalid PIN")
