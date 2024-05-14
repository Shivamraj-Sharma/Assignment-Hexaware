credit_score = int(input("Enter ypur credit score: "))
annual_income = int(input("Enter your annual income: "))

if credit_score > 700 and annual_income >= 50_000:
    print("You are eligible for a loan ")
else:
    print("You are not eligible for a loan ")