class Customer:
    def __init__(self,customer_id,first_name,last_name,email,phone,address):
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone=phone
        self.address=address
    
    def display(self):
        print("Customer ID:", self.customer_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email Address:", self.email)
        print("Phone Number:", self.phone)
        print("Address:", self.address)

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

customer=Customer("101","Shivamraj","Sharma","shivam@example.com","1234567890","India")
# customer.display()
# print(customer.get_address())

class Account:
    def __init__(self, account_number=None, account_type=None, account_balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def print_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance: $", self.account_balance)

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                print(f"Withdrawn ${amount:.2f} successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def calculate_interest(self):
        interest_rate = 0.072 
        interest_amount = self.account_balance * interest_rate
        return interest_amount


# Example usage:
account1 = Account("1001", "Savings", 1000_00)
account1.print_account_info()  

account1.deposit(500_00)  
account1.withdraw(200_00)  
account1.print_account_info() 

interest = account1.calculate_interest()
print(f"Interest earned: ${interest:.2f}")

class bank:
    interest_rate=5
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def display_balance(self):
        return f"{self.name} has $ {self.balance} in account"
    def withdraw(self,amount):
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            return f"Success Your balance is {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
    def deposit(self,amount):
        if amount>=0:
            self.balance=self.balance+amount
            return f"Success {self.display_balance()}"
        else:
            return f"Invalid amount {self.display_balance()}"
    
    def calculate_interest(self):
        accumulated_interest_amt = self.balance * bank.interest_rate
        self.balance += accumulated_interest_amt
        return f"Interest received. $ {accumulated_interest_amt}"
 


myaccount = bank(187,"Shivam",50_00_000)
print(myaccount.name,myaccount.acc_no)
print (myaccount.display_balance())
print(myaccount.withdraw(12_00_000))
print (myaccount.display_balance())
print (myaccount.deposit(3_50_000))
print(myaccount.calculate_interest())