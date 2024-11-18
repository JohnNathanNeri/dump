#operations
add = "addition"
subtract = "subtraction"
divide = "division" 
multiply = "multiplication"

#users input of numbers and operations 
x = int(input("number:"))
y = int(input("number:"))
operation = input("What operation do you want to use? \n(addition, subtraction, division, multiplication):")

#solving 
if operation == add:
    result = x + y 
    print(result)
elif operation == subtract:
    result = x - y
    print(result)
elif operation == divide:
    if y != 0:
     result = x / y
     print(result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == multiply:
    result = x * y
    print(result)
else:
    print("Invalid operation. Please choose from addition, subtraction, division, or multiplication.")


