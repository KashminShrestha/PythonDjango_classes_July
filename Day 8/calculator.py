start = True

while start:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # print("Select operation[ +, -, *, /]: ")
    # operation = input()

    operation = input("Select operation (+, -, *, /): ")

    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected. Please choose from +, -, *, /.")
    start = (
        input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        == "yes"
    )
else:
    print("Calculator has been closed.")
