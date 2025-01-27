# Welcome user to calculator.
# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Check which operation user inputted
# Perform the operation on the two numbers.
# Print the result to the terminal.

print("Welcome to calculator!")
num1 = float(input("What's the first number? "))
num2 = float(input("What's the second number? "))
operation = input('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide ')

match operation:
	case '1':
		print(f"The result is: {num1 + num2}")
	case '2':
		print(f"The result is: {num1 - num2}")
	case '3':
		print(f"The result is: {num1 * num2}")
	case '4':
		print(f"The result is: {num1 / num2}")

