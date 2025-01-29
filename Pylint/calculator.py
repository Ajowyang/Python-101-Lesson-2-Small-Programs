import json

with open('calc_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'==> {message}')

def invalid_num(num_str):
    try:
        float(num_str)
    except ValueError:
        return True
    return False

LANG = 'es'

prompt(messages('welcome', LANG))

while True:
    OUTPUT = None
    prompt(messages('first_number', LANG))
    num1 = input()
    while invalid_num(num1):
        prompt(messages('invalid_number', LANG))
        num1 = input()

    prompt(messages('second_number', LANG))
    num2 = input()
    while invalid_num(num2):
        prompt(messages('invalid_number', LANG))
        num2 = input()

    prompt(messages('operation', LANG))
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(messages('invalid_operation', LANG))
        operation = input()

    match operation :
        case '1':
            OUTPUT = float(num1) + float(num2)
        case '2':
            OUTPUT = float(num1) - float(num2)
        case '3':
            OUTPUT = float(num1) * float(num2)
        case '4':
            OUTPUT = float(num1) / float(num2)
    prompt(messages('result', LANG).format(result=OUTPUT))

    keep_going = input(messages("another_calc", LANG))
    while keep_going.lower() not in ['y', 'n']:
        prompt(messages('y_or_n', LANG))
        keep_going = input()
    if keep_going.lower() == 'n':
        break
