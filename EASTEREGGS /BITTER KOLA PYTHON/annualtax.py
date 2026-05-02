monthly_salary = float(input("Enter monthly salary (₦): "))
annual_salary = monthly_salary * 12

    if annual_salary <= 300000:
        tax = 0
    elif annual_salary <= 600000:
        tax = (annual_salary - 300000) * 0.15
    else:
        tax = (300000 * 0.15) + (annual_salary - 600000) * 0.25

    print(f"Annual salary: ₦{annual_salary:,2f}")
    print(f"Annual tax owed: ₦{tax:,2f}")
