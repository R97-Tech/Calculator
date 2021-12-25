def add():
	answer = first_number + second_number
	print(first_number, "+", second_number, "=", answer)

def subtract():
	answer = first_number - second_number
	print(first_number, "-", second_number, "=", answer)

def multiply():
	answer = first_number * second_number 
	print(first_number, "*", second_number, "=", answer)

def divide():
	answer = first_number / second_number
	print(first_number, "/", second_number, "=", answer)

print("Welcome to Simple Calculator v1.0")
print("Press A for Addition")
print("Press S for Subtraction")
print("Press M for Multiplication")
print("Press D for Division")

while True:
	user_choice = input("Enter Choice: ")

	if user_choice in ('a', 's', 'm', 'd'):
		first_number = float(input("Please Enter the first number: "))
		second_number = float(input("Please Enter the second number: "))

	if user_choice == 'a':
		add()

	elif user_choice == 's':
		subtract()

	elif user_choice == 'm':
		multiply()

	elif user_choice == 'd':
		divide()

	else:
		print(user_choice,"is not a valid Choice")

	next_calc = input("Do you want to do a another calculation? (y/n) ")

	if next_calc == "n":
		break