# Simple calculator for addition and subtraction

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter choice (1 or 2): ")

    if choice in ['1', '2']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result of addition is: {num1 + num2}")
        elif choice == '2':
            print(f"The result of subtraction is: {num1 - num2}")
    else:
        print("Invalid input. Please choose 1 or 2.")

# Run the calculator
calculator()
