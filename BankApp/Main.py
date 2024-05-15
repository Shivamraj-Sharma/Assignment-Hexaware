from service.BankServiceProviderImpl import BankServiceProviderImpl
from bean.Customer import Customer

class BankApp:
    @staticmethod
    def start():
        bank = BankServiceProviderImpl("My Bank", "123 Main St")
        
        while True:
            print("\nWelcome to the bank!")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. List Accounts")
            print("7. Calculate Interest")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                acc_type = input("Enter account type (Savings, Current, ZeroBalance): ")
                customer_id = input("Enter customer ID: ")
                customer_name = input("Enter customer name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                balance = float(input("Enter initial balance: "))
                accNo = input("Enter account number: ")
                customer = Customer(customer_id, *customer_name.split(), email, phone_number, address)
                account = bank.create_account(customer, acc_type, accNo, balance)

                if account:
                    print(f"Account created successfully. Account number: {account.account_number}")

            elif choice == "2":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to deposit: "))
                balance = bank.deposit(account_number, amount)
                if balance is not None:
                    print(f"Deposit successful. New balance: {balance}")

            elif choice == "3":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to withdraw: "))
                balance = bank.withdraw(account_number, amount)
                if balance is not None:
                    print(f"Withdrawal successful. New balance: {balance}")

            elif choice == "4":
                from_account_number = int(input("Enter source account number: "))
                to_account_number = int(input("Enter destination account number: "))
                amount = float(input("Enter amount to transfer: "))
                balance = bank.transfer(from_account_number, to_account_number, amount)
                if balance is not None:
                    print(f"Transfer successful. New balance: {balance}")

            elif choice == "5":
                account_number = int(input("Enter account number: "))
                account_details = bank.get_account_details(account_number)
                if account_details:
                    print("Account details:")
                    print(f"Account Number: {account_details.account_number}")
                    print(f"Account Type: {account_details.account_type}")
                    print(f"Account Balance: {account_details.account_balance}")
                    print(f"Customer: {account_details.customer.first_name} {account_details.customer.last_name}")
                    print(f"Customer ID: {account_details.customer.customer_id}")
                    print(f"Customer Email: {account_details.customer.email}")
                    print(f"Customer Phone Number: {account_details.customer.phone_number}")
                    print(f"Customer Address: {account_details.customer.address}")

            elif choice == "6":
                accounts = bank.list_accounts()
                if accounts:
                    print("List of accounts:")
                    for acc in accounts:
                        print(f"Account Number: {acc.account_number}, Type: {acc.account_type}, Balance: {acc.account_balance}")

            elif choice == "7":
                bank.calculate_interest()

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

BankApp.start()