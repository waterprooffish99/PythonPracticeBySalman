# try:
#     print("I am ging to try dividing 5 by 0...")
#     result = 5/0
# except ZeroDivisionError:
#     print("Oops! You can not divide any number by O")

# try:
#     user_input = input("Enter a Number: ")
#     number = int(user_input)
#     print( f"You entered the number: {number}")
# except ValueError:
#     print("Oops! That was not a valid number. Please Enter a number: ")

# try:
#     num1 = int(input("Enter a Number: "))
#     num2 = int(input("Enter a Number: "))
#     result = num1 + num2
#     print(f"The sum of num1 and num2 is: {result}")
# except ValueError:
#     print("Oops! That was not a valid number. Please Enter a number")

try:
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    operation = input("Enter Operation (+, -, *, /)")

    if operation == "+" :
        result = num1 + num2
    elif operation == "-" :
        result = num1 - num2
    elif operation == "*" :
        result = num1 * num2
    elif operation == "/" :
        result = int(num1 / num2)
    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print(f"The result of {num1} {operation} {num2} is: {result}")
except ValueError:
        print("Oops! Please Enter a number")
except ZeroMultiplyError:
       print("Oops! Multiplication by zero is not allowed")
except ZeroDivisionError:
        print("Oops! Division by zero is not allowed")