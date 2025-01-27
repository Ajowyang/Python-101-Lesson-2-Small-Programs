def prompt(message):
    print(f'==> {message}')

def invalid_num(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    return False

prompt("Welcome to calculator!")

prompt("What's the first number? ")
num1 = input()
while invalid_num(num1):
    prompt("Hmm.. doesn't look like valid number")
    num1 = input()

prompt("What's the second number? ")
num2 = input()
while invalid_num(num2):
    prompt("Hmm.. doesn't look like valid number")
    num2 = input()

prompt('What operation would you like to perform?\n1) Add 2) Subtract 3) Multi\
    ply 4) Divide ')
operation = input()
while operation not in ['1', '2', '3', '4']:
    prompt("Must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case '1':
        prompt(f"The result is: {int(num1) + int(num2)}")
    case '2':
        prompt(f"The result is: {int(num1) - int(num2)}")
    case '3':
        prompt(f"The result is: {int(num1) * int(num2)}")
    case '4':
        prompt(f"The result is: {int(num1) / int(num2)}")