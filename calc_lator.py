def calculator():
    print(" Simple Calculator")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print(" Cannot divide by zero!")
            return
    else:
        print(" Invalid operator!")
        return

    print(f" Result: {num1} {op} {num2} = {result}")


calculator()
