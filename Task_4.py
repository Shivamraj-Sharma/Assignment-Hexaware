accounts = {
    101: 1000,
    102: 5000,
    103: 7000,
    104: 12000,
    105: 500,
    106: 9000,
    107: 8000,
    108: 4000,
    109: 2000,
    110: 1000,
    111: 3500,
    112: 55000
}

while True:
    account = int(input("Enter Your account number: "))

    if account in accounts:
        print(f"Available balance: {accounts[account]}")
        break
    else:
        print("Emter a valid account number...\n")