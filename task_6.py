from tabulate import tabulate

account = int(input("Enter account number: "))
header = ("Amount","Transaction Type")
transactions = []
transaction_type = {1:"credit", 2:"debit"}

while True:
    print("1. Credit\n"
          "2. Debit\n"
          "3. Exit\n"
          )
    ask = int(input())
    if ask == 3:
        break
    elif ask > 3:
        print("Enter a valid value\n")

    amt = int(input("Enter amount: "))
    transactions.append((amt, transaction_type[ask]))

print(f"Transaction history for account no. {account} :")
print(tabulate(transactions, headers = header, tablefmt = "psql"))