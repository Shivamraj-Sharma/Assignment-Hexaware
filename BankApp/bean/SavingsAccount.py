from bean.Account import Account
class SavingsAccount(Account):
    def __init__(self, customer, interest_rate, account_balance=500):
        super().__init__("Savings", account_balance, customer)
        self.interest_rate = interest_rate