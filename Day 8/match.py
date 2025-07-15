num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Select operation (+, -, *, /,%): ")

match operation:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "%":
        print(f"{num1} % {num2} = {num1 % num2}")
    case "/":

        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation selected. Please choose from +, -, *, /, %.")