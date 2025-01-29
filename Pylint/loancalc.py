def invalid_input(numstr):
    try:
        number = float(numstr)
        if number < 0:
            raise ValueError(f"number must be > 0: {numstr}")
    except ValueError:
        return True
    return False

def prompt(message):
     print(f"==> {message}")
   
prompt("Welcome to Loan Calculator!")

while True:
    loan_amount = input("What is the loan amount in USD? ")
    while invalid_input(loan_amount):
        prompt("Enter a valid amount in USD")
        loan_amount = input()
    loan_amount = float(loan_amount)

    apr = input("What is the Annual Percentage Rate(APR)? ")
    while invalid_input(apr):
        prompt("Enter a valid APR")
        apr = input()
    apr = float(apr) * 0.01

    duration = input("What is the loan duration in years? ")
    while invalid_input(duration):
        prompt("Enter a valid number of years")
        duration = input()
    duration = float(duration)

    monthly_interest_rate = apr / 12.0
    loan_duration_months = duration * 12

    monthly_amount = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))) if monthly_interest_rate != 0 else loan_amount / loan_duration_months
    prompt(f'The loan payment every month is ${monthly_amount:.2f}')

    prompt("Perform another calculation? Y/N ")
    another_calc = input()
    while another_calc.lower() not in['y', 'n']:
        prompt("Please enter 'Y' or 'N' ")
        another_calc = input()

    if another_calc.lower() == 'n':
        break