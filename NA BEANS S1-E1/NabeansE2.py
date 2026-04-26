principal = int(input("enter the principalamount"))
duration = int(input("enter the durationof the loan"))
annualrate = int("enter the annual duration"))

monthlyrate = annualrate / 100 / 12
months = duration * 12 
montage = (principal*monthlyrate(1+ monthlyrate)**months)/(((1+ monthlyrate)**months)-1)

print(montage)
