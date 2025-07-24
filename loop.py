#loop

'''What is a Loop?

A loop is like a robot doing the same thing again and again until you tell it to stop.

Example in Real Life:

Imagine you are clapping. You can clap once, but what if I say:
"Clap 5 times!"
You will clap 1, 2, 3, 4, 5 and then stop.

A loop in Python does the same thing,it repeats something until we tell it to stop.


---

Types of Loops in Python:

1. for loop → When we know how many times to repeat.


2. while loop → When we keep repeating until a condition is false.




---'''

#1️⃣ for loop (Counting Loops)

'''It’s like saying, "Clap 5 times!"'''

# for i in range(5):  # Loop runs 5 times
#     print("Clap!")


# '''What happens?

# The loop runs 5 times because range(5) means "count from 0 to 4" (5 times).

# Each time, it prints "Clap!"


# Output:

# Clap!  
# Clap!  
# Clap!  
# Clap!  
# Clap!


# ---'''

# for apple in range(7):
#     print("I pick an apple!") # it prints it 7 times.


# for sock in range(4):
#     print("I Folded a sock")


# for balloons in range(6):
#     print("I Blewj Up a Balloon!")


# for cookie in range(5):
#     print("I baked a cookie!")


# for count in range(5 , 0 , -1):
#     print("Seconds left!")


for count in range(1, 5, +1):
    print(f"{count} ready!, {count} set!, {count} go!, {count} run!, {count} done!")


'''2️⃣ while loop (Condition Loops)

This is like "Keep eating until you're full!"

hungry = True  

while hungry:  
    print("Eating...")  
    hungry = False  # We stop eating after one time

What happens?

The loop keeps running as long as hungry is True.

Once we set hungry = False, it stops.


Output:

Eating...


---

🚨 Warning: Infinite Loop!

If we forget to stop the loop, it never ends. That’s called an infinite loop.

Bad example:

while True:  
    print("Help! I'm stuck in a loop!")  # This never stops

👆 This will go on forever! Always make sure to have a condition to stop the loop.


---

👶 Practice Task for You!

1. Write a for loop to print your name 3 times.


2. Write a while loop that prints "Learning Python!" until a variable learning becomes False.



Try them out and tell me if you get stuck!'''