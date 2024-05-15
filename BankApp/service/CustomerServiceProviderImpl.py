from service.ICustomerServiceProvider import ICustomerServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].account_balance
        else:
            print("Account not found.")
            return None
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].account_balance += amount
            return self.accounts[account_number].account_balance
        else:
            print("Account not found.")
            return None
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.account_balance >= amount:
                account.account_balance -= amount
                return account.account_balance
            else:
                print("Insufficient funds.")
                return None
        else:
            print("Account not found.")
            return None
    
    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_account = self.accounts[from_account_number]
            to_account = self.accounts[to_account_number]
            if from_account.account_balance >= amount:
                from_account.account_balance -= amount
                to_account.account_balance += amount
                return from_account.account_balance
            else:
                print("Insufficient funds.")
                return None
        else:
            print("One or both accounts not found.")
            return None
    
    def get_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account
        else:
            print("Account not found.")
            return None