# ## Simple Calculator
print("Welcome to the simple calculator!")
print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Ask the user to choose an operation and clean the input
operation = input("Enter the number corresponding to your choice (1/2/3/4): ").strip()

# Get input numbers from the user
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print('*' * 30)

# Perform the chosen operation
if operation == '1':
    result = first + second
    print("The result of addition is:", result)
elif operation == '2':
    result = first - second
    print("The result of subtraction is:", result)
elif operation == '3':
    result = first * second
    print("The result of multiplication is:", result)
elif operation == '4':
    if second != 0:
        result = first / second
        print("The result of division is:", round(result, 2))
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid input. Please select a valid operation.")

print('*' * 30)
