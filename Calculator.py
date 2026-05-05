num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choice = input("Enter operation (+, -, *, /): ")

if choice == '+':
    print("Your choice is Addition. Result:", num1 + num2)

elif choice == '-':
    print("Your choice is Subtraction. Result:", num1 - num2)

elif choice == '*':
    print("Your choice is Multiplication. Result:", num1 * num2)

elif choice == '/':
    if num2 != 0:
        print("Your choice is Division. Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operation")
