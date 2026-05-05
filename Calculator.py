def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    choice = input("Enter operation (+, -, *, /): ")

    if choice == '+':
        result = num1 + num2
        print("Addition Result:", result)

    elif choice == '-':
        result = num1 - num2
        print("Subtraction Result:", result)

    elif choice == '*':
        result = num1 * num2
        print("Multiplication Result:", result)

    elif choice == '/':
        if num2 != 0:
            result = num1 / num2
            print("Division Result:", result)
        else:
            print("Error: Division by zero is not allowed")

    else:
        print("Invalid operation")

# Run program
calculator()
