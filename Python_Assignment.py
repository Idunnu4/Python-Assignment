# step 1: Ask the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).

num1 = float(input("enter the first number:"))

# step 2: Ask the user to input the second number

num2 = float(input("enter the second number:"))

# step 3: Ask the user to input an operation symbol

operations = input("Enter an operator (+, *, /, %): ")

# step 4: use if.elif.else to perform the operation

if operations == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operations == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operations == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operations == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")

elif operations == "/":
    if num2 !=0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("error: cannot divide by zero")

else:
    print("invalid operations. Please use (+, *, /, %)")      
