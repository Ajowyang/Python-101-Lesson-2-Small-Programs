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

lang = 'es'


prompt(messages('welcome', lang))

while True:
    output = None
    prompt(messages('first_number', lang))
    num1 = input()
    while invalid_num(num1):
        prompt(messages('invalid_number', lang))
        num1 = input()

    prompt(messages('second_number', lang))
    num2 = input()
    while invalid_num(num2):    
        prompt(messages('invalid_number', lang))
        num2 = input()

    prompt(messages('operation', lang))
    operation = input()
    while operation not in ['1', '2', '3', '4']:    
        prompt(messages('invalid_operation', lang))
        operation = input()

    match operation :
        case '1':
            output = float(num1) + float(num2)
            
        case '2':
            output = float(num1) - float(num2)
            
        case '3':
            output = float(num1) * float(num2)
            
        case '4':
            output = float(num1) / float(num2)
    
    prompt(messages('result', lang).format(result=output))    

    keep_going = input(messages("another_calc", lang))
    while keep_going.lower() not in ['y', 'n']:    
        prompt(messages('y_or_n', lang))
        keep_going = input()
    if keep_going.lower() == 'n':
        break
   
