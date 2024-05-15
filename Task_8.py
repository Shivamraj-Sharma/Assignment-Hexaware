class Account:
    def __init__(self, account_number, account_type, account_balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            self.account_balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Invalid deposit amount. Please enter a valid number.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if amount <= self.account_balance:
                self.account_balance -= amount
                print(f"Withdrawn ${amount:.2f} successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please enter a valid number.")

    def print_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance: $", self.account_balance)
    
    def get_account_number(self):
        return self.account_number


account = Account("101", "Savings", 1000_00)
# there is no double datatype in python
# deposit and withdraw using different data types
# account.deposit(500)       # int
# account.withdraw(200.50)   # float
# account.deposit(1000.25)   # float
# account.withdraw(200)      # int


# account.print_account_info()

class SavingsAccount(Account):
    interest_rate = 0.072
 
    def calculate_interest(self):
        interest_amount = self.account_balance * self.interest_rate
        self.account_balance += interest_amount
        return interest_amount
 
 
arjun = SavingsAccount(135, "Arjun", 18_000)
 
# print(arjun.calculate_interest())  # 7.2%

class CurrentAccount(Account):
    overdraft_limit = 1000 

    def __init__(self, account_number, customer_name, balance=0, overdraft_limit=1000):
        super().__init__(account_number, customer_name, balance)
        self._overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self._overdraft_limit

    def set_overdraft_limit(self, value):
        self._overdraft_limit = value

    def withdraw(self, amount):
        available_balance = self._balance + self._overdraft_limit
        if amount > available_balance:
            print("Withdrawal amount exceeds available balance and overdraft limit.")
        else:
            self._balance -= amount

    def __str__(self):
        return super().__str__() + f"\nOverdraft Limit: {self._overdraft_limit}"


class Bank:
    def __init__(self):
        self.accounts = []

    def display_menu(self):
        print("Menu:")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Calculate Interest")
        print("6. Exit")

    def create_account(self, account_type):
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        if account_type.lower() == 'savings':
            account = SavingsAccount(account_number, initial_balance)
            self.accounts.append(account)
            print("Savings Account created successfully.")
        elif account_type.lower() == 'current':
            account = CurrentAccount(account_number, initial_balance)
            self.accounts.append(account)
            print("Current Account created successfully.")
        else:
            print("Invalid account type.")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def calculate_interest(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.calculate_interest()

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

bank = Bank()

while True:
    bank.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        bank.create_account("Savings")
    elif choice == '2':
        bank.create_account("Current")
    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(account_number, amount)
    elif choice == '4':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(account_number, amount)
    elif choice == '5':
        bank.calculate_interest()
    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")