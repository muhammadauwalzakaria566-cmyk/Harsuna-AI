operator = input ("choose your operator (+, -, *, /): ")
numb1 = float (input ("enter your first number: "))
numb2 = float (input ("enter your first number: "))

if operator == "+":
    result = numb1 + numb2
    print(round(result, 3))
elif operator == "-":
    result = numb1 - numb2
    print(round(result, 3))
elif operator == "*":
    result = numb1 * numb2
    print(round(result, 3))
elif  operator == "/":
    result = numb1 / numb2
    print(round(result, 3))
else:
    print(operator + " is not valid")