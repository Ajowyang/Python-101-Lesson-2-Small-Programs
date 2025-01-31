def invalid_input(numstr):
    try:
        number = float(numstr)
        if number <= 0:
            raise ValueError(f"number must be > 0: {numstr}")
    except ValueError:
        return True
    return False

def prompt(message):
    print(f"==> {message}")

def prompt_and_validate(prompt_message, invalid_message):
    prompt(prompt_message)
    amount = input()
    while invalid_input(amount):
        prompt(invalid_message)
        amount = input()
    return float(amount)

def get_monthly_interest_rate(annual_percentage_rate):
    return annual_percentage_rate / 12

def get_monthly_amount(total_loan_amount, monthly_int_rate, duration_months):
    return (total_loan_amount * (monthly_int_rate /
            (1 - (1 + monthly_int_rate) ** (-duration_months)))
            if monthly_int_rate != 0
            else total_loan_amount / duration_months)

def another_calculation():
    prompt("Perform another calculation? (y/n) ")
    y_or_n = input()
    while y_or_n.lower() not in['y', 'n']:
        prompt("Please enter 'y' or 'n' ")
        y_or_n = input()
    return y_or_n

prompt("Welcome to Loan Calculator!")

while True:
    loan_amount = prompt_and_validate("What is the loan amount in USD? ",
    "Enter a valid amount in USD")
    apr = prompt_and_validate("What is the Annual Percentage Rate(APR)? ",
    "Enter a valid APR")
    apr = float(apr) * 0.01
    duration = prompt_and_validate("What is the loan duration in months? ",
    "Enter a valid number of months")

    monthly_interest_rate = get_monthly_interest_rate(apr)
    monthly_amount = get_monthly_amount(loan_amount, monthly_interest_rate,
                                        duration)
    prompt(f'The loan payment every month is ${monthly_amount:.2f}')

    another_calc = another_calculation()
    if another_calc.lower() == 'n':
        break