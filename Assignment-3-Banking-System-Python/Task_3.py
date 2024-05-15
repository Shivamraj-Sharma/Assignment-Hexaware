initial_balance = int(input("Enter initial balance: "))
annual_interest_rate = int(input("Enter annual interest rate: "))
number_of_years = int(input("Enter number of years: "))

future_balance = round(initial_balance * (1 + annual_interest_rate/100)**number_of_years,2)

print(f"Your balance after {number_of_years} will be {future_balance}")