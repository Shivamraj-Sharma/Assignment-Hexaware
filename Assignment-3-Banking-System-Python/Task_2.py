curr_bal = int(input("Enter your current balance: "))
while True:
    print(
        "Choose what you would like to do\n"
        "1. check balance\n"
        "2. withdrawl\n"
        "3. deposit\n"
        "4. Exit")
    ask  = int(input("Enter a value: "))

    if ask == 1:
        print(f"Your current balance is ${curr_bal}\n")
    elif ask == 2:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= curr_bal and amt%100 == 0:
            curr_bal -= amt
            print("Transaction Successful!!\n")
        elif amt > curr_bal:
            print("Insufficient Balance!!\n")
        else:
            print("Enter amount in multiples of 100 or 500\n")
    elif ask == 3:
        amt = int(input("Enter amount to be deposited: "))
        curr_bal += amt
        print("Transaction Successful!!")
        print(f"Current balance: {curr_bal}\n")
    elif ask == 4:
        break
    else:
        print("Please enter a valid value\n")