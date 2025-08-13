# Simple Calculator Program

def simple_calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return  # Just exit the function
        result = num1 / num2
    else:
        print("Error: Invalid operation! Please use +, -, *, or /")
        return  # Just exit the function

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator
simple_calculator()