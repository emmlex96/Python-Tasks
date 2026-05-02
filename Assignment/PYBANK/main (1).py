from pybank import *

message = """1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """

while True:
    user_input = input(message)
    match user_input:
        case "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Registration successful")
            else:
                print("Registration failed")
                
        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Login successful")
            else:
                print("Login failed")
                
        case "3":
            transactions = []
            amount = float(input("Enter amount or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter amount or 0 to stop: "))
            total_transactions = calculate_balance(transactions)
            print("Your balance is ", total_transactions)
            
            
             case "4":
        try:
            balance = float(input("Enter current balance: "))
            rate = float(input("Enter annual interest rate (e.g. 0.05 for 5%): "))
            years = float(input("Enter number of years: "))
            result = apply_interest(balance, rate, years)
            print(f"Balance after {years} year(s) at {rate * 100}% interest: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    case "5":
        transactions = []
        print("Enter transactions (type 'done' to finish):")
        while True:
            transaction_type = input("  Type (credit/debit): ").strip().lower()
            if transaction_type == "done":
                break
            if transaction_type not in ("credit", "debit"):
                print("  Please enter 'credit' or 'debit'.")
                continue
            amount = float(input("  Amount: "))
            transactions.append([transaction_type, amount])

        if transactions:
            summary = get_transaction_summary(transactions)
            print("\n--- Transaction Summary ---")
            for item in summary:
                print(f"  {item[0]}: {item[1]}")
        else:
            print("No transactions entered.")

    case "6":
        print("exit!")
        break

            
   
