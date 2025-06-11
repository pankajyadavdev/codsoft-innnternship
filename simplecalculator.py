print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
option = int(input("Enter your choice: "))
if(option in(1, 2, 3, 4)):
    print("You have selected option", option)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if(option == 1):
        print(f"Result: {num1 + num2}")
    elif(option == 2):
        print(f"Result: {num1 - num2}")
    elif(option == 3):
        print(f"Result: {num1 * num2}")
    elif(option == 4):
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid option.")
    result = 0
    print("The result of the operaton is ",result)
