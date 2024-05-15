class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_email(self, email):
        if self.validate_email(email):
            self.email = email
        else:
            print("Invalid email address")
    
    def set_phone_number(self, phone_number):
        if self.validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            print("Invalid phone number")
    
    def set_address(self, address):
        self.address = address
    
   
    def print_all_info(self):
        print("Customer ID:", self.customer_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email Address:", self.email)
        print("Phone Number:", self.phone_number)
        print("Address:", self.address)
    
    def validate_email(self, email):
       
        if '@' in email:
            return True
        else:
            return False
    
    
    def validate_phone_number(self, phone_number):
       
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        else:
            return False

customer1 = Customer()

customer1.set_customer_id(1)
customer1.set_first_name("Raj")
customer1.set_last_name("Kumar")
customer1.set_email("rajkumar@gmail.com")
customer1.set_phone_number("1234567890")
customer1.set_address("India")


class Account:
    def __init__(self, account_number=None, account_type=None, account_balance=0, customer=None):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance
        self.customer = customer
    
    def get_account_number(self):
        return self.account_number
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_balance(self):
        return self.account_balance
    
    def get_customer(self):
        return self.customer
    
    def set_account_number(self, account_number):
        self.account_number = account_number
    
    def set_account_type(self, account_type):
        self.account_type = account_type
    
    def set_account_balance(self, account_balance):
        self.account_balance = account_balance
    
    def set_customer(self, customer):
        self.customer = customer
    
    
    def print_all_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.account_balance)
        print("Customer:")
        if self.customer:
            self.customer.print_all_info()
        else:
            print("No customer assigned to this account.")

account1 = Account()
account1.set_account_number("ACC123456")
account1.set_account_type("Savings")
account1.set_account_balance(1000)
account1.set_customer(customer1)

account1.print_all_info()

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001
    
    def create_account(self, customer, acc_type, balance):
        account_number = self.next_account_number
        self.next_account_number += 1
        account = Account(account_number, acc_type, balance, customer)
        self.accounts[account_number] = account
        return account_number
    
    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_account_balance()
        else:
            return None
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].set_account_balance(
                self.accounts[account_number].get_account_balance() + amount)
            return self.accounts[account_number].get_account_balance()
        else:
            return None
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            current_balance = self.accounts[account_number].get_account_balance()
            if current_balance >= amount:
                self.accounts[account_number].set_account_balance(current_balance - amount)
                return self.accounts[account_number].get_account_balance()
            else:
                return "Insufficient balance"
        else:
            return None
    
    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.withdraw(from_account_number, amount) != "Insufficient balance":
                self.deposit(to_account_number, amount)
                return "Transfer successful"
            else:
                return "Transfer failed due to insufficient balance"
        else:
            return "One or both account numbers are invalid"
    
    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None


class BankApp:
    @staticmethod
    def start():
        bank = Bank()
        while True:
            print("\nWelcome to the Bank App")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nCreating Account...")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email address: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                customer = Customer(None, first_name, last_name, email, phone_number, address)
                print("Select Account Type:")
                print("1. Savings")
                print("2. Current")
                acc_type = input("Enter your choice: ")
                acc_type = "Savings" if acc_type == '1' else "Current"
                balance = float(input("Enter initial balance: "))
                account_number = bank.create_account(customer, acc_type, balance)
                print("Account created successfully. Your account number is:", account_number)

            elif choice == '2':
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to deposit: "))
                balance = bank.deposit(account_number, amount)
                if balance is not None:
                    print("Deposit successful. Current balance:", balance)
                else:
                    print("Invalid account number")

            elif choice == '3':
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to withdraw: "))
                result = bank.withdraw(account_number, amount)
                if result == "Insufficient balance":
                    print("Insufficient balance")
                elif result is not None:
                    print("Withdrawal successful. Current balance:", result)
                else:
                    print("Invalid account number")

            elif choice == '4':
                from_account_number = int(input("Enter your account number: "))
                to_account_number = int(input("Enter recipient's account number: "))
                amount = float(input("Enter amount to transfer: "))
                result = bank.transfer(from_account_number, to_account_number, amount)
                print(result)

            elif choice == '5':
                account_number = int(input("Enter account number: "))
                account = bank.get_account_details(account_number)
                if account is not None:
                    print("\nAccount Details:")
                    account.print_all_info()
                else:
                    print("Invalid account number")

            elif choice == '6':
                print("Thank you for using the Bank App. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

BankApp.start()