salary = float(input("Enter salary (₦): "))

if salary <= 50000:
    deduction = 0
    rate = "0%"
elif salary <= 150000:
    deduction = salary * 0.05
    rate = "5%"
elif salary <= 500000:
    deduction = salary * 0.075
    rate = "7.5%"
else:
    deduction = salary * 0.10
    rate = "10%"

print(f"Salary: ₦(salary:,.2f)")
print(f"Rate applied: (rate)")
print(f"Social insurance deduction: ₦(deduction:,.2f)")
