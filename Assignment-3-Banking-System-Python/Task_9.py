from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, customer_name, balance=0):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def __str__(self):
        return f"Account Number: {self.account_number}\nCustomer Name: {self.customer_name}\nBalance: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, customer_name, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount

    def calculate_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest


class CurrentAccount(BankAccount):
    overdraft_limit = 1000  

    def __init__(self, account_number, customer_name, balance=0):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        available_balance = self._balance + self.overdraft_limit
        if amount > available_balance:
            print("Withdrawal amount exceeds available balance and overdraft limit.")
        else:
            self._balance -= amount

    def calculate_interest(self):
        pass


class Bank:
    def __init__(self):
        self.accounts = []

    def display_menu(self):
        print("Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Calculate Interest")
        print("5. Exit")

    def display_account_menu(self):
        print("Account Type:")
        print("1. Savings Account")
        print("2. Current Account")

    def create_account(self, account_type):
        if account_type == '1':
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate: "))
            account = SavingsAccount(account_number, customer_name, initial_balance, interest_rate)
            self.accounts.append(account)
            print("Savings Account created successfully.")
        elif account_type == '2':
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = CurrentAccount(account_number, customer_name, initial_balance)
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
            if account.account_number == account_number:
                return account
        return None

bank = Bank()

while True:
    bank.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        bank.display_account_menu()
        account_type = input("Enter account type: ")
        bank.create_account(account_type)
    elif choice == '2':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(account_number, amount)
    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(account_number, amount)
    elif choice == '4':
        bank.calculate_interest()
    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")