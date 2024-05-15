from bean.Account import Account

class CurrentAccount(Account):
    def __init__(self, customer, overdraft_limit, account_balance):
        super().__init__("Current", account_balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.account_balance + self.overdraft_limit:
            print("Insufficient funds!")
        else:
            self.account_balance -= amount
            print("Withdrawal successful!")