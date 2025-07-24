# try:
#     num = int(input("Enter a positive number: "))

#     if num < 0:
#         raise ValueError("only positive numbers are allowed")
#     else:
#         print(f"Great! You entered: {num}")

# except ValueError as e:
#     print(f"Error: {e}")

try: 
    age = int(input("Enter Your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print(f"Your age is: {age} years!")
except ValueError as e:
    print(f"Error: {e}")