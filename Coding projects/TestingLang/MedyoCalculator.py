#operations
add = ("addition", "ADDITION", "Addition", "add", "Add", "plus", "Plus", "+")
subtrac = ("subtraction", "Subtraction", "SUBTRACTION", "Subtract", "subtract", "minus", "Minus", "-")
divide = ("division", "Division", "Divide", "divide", "/")
multiply = ("multiplication", "Multiplication", "Multiply", "multiply", "x", "*", "X")

#users input of numbers adn operations 
x = int(input("number:"))
y = int(input("number:"))
operation = input("What operation do you want to use?\n")

#solving 
if operation in add:
    result = x + y 
    print(result)
elif operation in subtrac:
    result = x - y
    print(result)
elif operation in divide:
    if y != 0:
     result = x / y
     print(result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation in multiply:
    result = x * y
    print("{x}{result}")
else:
    print("Invalid operation. Please choose from addition, subtraction, division, or multiplication.")

