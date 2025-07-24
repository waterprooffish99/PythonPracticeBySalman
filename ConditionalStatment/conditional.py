# Conditional statements help your code make decisions based on conditions. In simple words, they allow your program to choose between different actions.

# if #elif else

# 1. if Statement (Basic Condition)

# It checks if a condition is True and executes code if it is:

age = 20

if age >= 18:

    print("You can apply for the driving license.")

else:
    print("You are not old enough to apply for the driving license.")


marks = 75

if marks >= 90:

    print("A1 Grade.")

elif marks >= 80:

    print("A Grade.")

elif marks >= 70:

    print("B Grade.")

elif marks >=  60:

    print("C Grade.")

else:

    print("D Grade.")

# 4. Nested if (Condition Inside a Condition)
"""You can put one if inside another."""

# age = 19

# has_ID = True

# if age >= 20:
#     if has_ID:
#         print("You can Enter the Club.")
#     else:
#         print("You are too Young to Enter.")


# """5. Using and, or, not (Multiple Conditions)
# These help you check more than one condition.

# and (Both conditions must be True)"""


# age = 18

# has_ID = True
# if age >= 18 or has_ID:

#     print("You can Enter the Club.")

# else: 
#     print("Please Get Back")


# number = 7

# if number % 2 == 0:
#     print("The number is even.")

# else:
#     print("The number is odd.")

# 

# age = int(input("Enter your age: "))

# if age < 5:
#     print("You're Ticket is Free!")
# elif age >= 5 and age <= 12:
#     print("You're Ticket is 300 Rupees!")
# elif age >=13 and age <= 17:
#     print("You're Ticket is 500 Rupees!")
# else:
#     print("You're Ticket is 700 Rupees!")

# marks = 50

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 80:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 50:
#     print("Grade D")
# else:
#     print("Work Hard and Try Again!")


marks_input = input("Enter your marks (0-100):")

if marks_input.isdigit():
    marks = int(marks_input)

    if marks < 0 or marks > 100:
        print("Please enter a number between 0 and 100.")
    else:

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
           grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "F"

        if marks >= 60:
            print(f"Grade: {grade} - You Passed! ")
        else:
            print(f"Grade: {grade} - You Failed!")


