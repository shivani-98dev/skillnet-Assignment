num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator")