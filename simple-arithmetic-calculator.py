#simple-arethmatic-calculater

#function to add two numbers
def add(x, y):
	return x + y

#function to subtract two numbers
def subtract(x, y):
	return x - y

#function to multiply two numbers
def multiply(x, y):
	return x * y

#function to divide two numbers
def divide(x, y):
	return x / y

#statements of choices
print("Select an operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#writing a while loop
while True:
	#receive input from the user
	option = input("Enter your choice 1, 2, 3 or 4: ")

	#check if the option is one of the choices
	if option in ('1', '2', '3', '4'):
		num_1 = float(input("Enter the first number: "))
		num_2 = float(input("Enter the second number: "))

		if option == '1':
			print(num_1, "+", num_2, "=", add(num_1, num_2))

		elif option == '2':
			print(num_1, "-", num_2, "=", subtract(num_1, num_2))

		elif option == '3':
			print(num_1, "*", num_2, "=", multiply(num_1, num_2))

		elif option == '4':
			print(num_1, "/", num_2, "=", divide(num_1, num_2))

		#check if the user wants another calculation
		#break if the answer is no
		my_next_calculation = input("Want to make another calculation? (yes/no): ")
		if my_next_calculation == "no":
			break

	else:
		print("Invalid input, please select a valid option!!!")
