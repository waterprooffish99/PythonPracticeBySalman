#📜 Python List – Super Simple Explanation
'''A list is like a basket where you can keep many things together! 🧺

Imagine you have a basket of fruits: 🍎🍌🍇
In Python, you can store them in a list like this'''

fruits = ["orange" ,"apple" , "strawberry" ,]

print(fruits) 

cars = ["lamborghini avantedor" , "ferrari 458 italia" , "bugatti chiron"]

print(cars)

#🔹 Features of a List
'''✅ Can store multiple values (like a basket holding many fruits).
✅ Can have different data types (numbers, words, even other lists!).
✅ Uses square brackets [] to store items.
✅ Items are ordered (position matters).
✅ Allows duplicates (you can have two apples).'''

#🔢 List with Numbers

numbers = [1, 2, 3, 4, 5]

print(numbers)

numbers1 = [11.2, 12.3, 13.4, 14.5, 15.6]

print(numbers)

#💡 Accessing List Items (Getting a Specific Item)
'''Each item in the list has a position (index), starting from 0:'''

print(fruits[0]) #prints orange

print(fruits[1]) #prints apple

print(fruits[2]) #prints strawberry

#✍️ Changing List Items
'''Lists are changeable, so you can replace an item:'''

fruits[0] = "grape"

fruits[1] = "banana"

fruits[2] = "mango"

print(fruits[0])

print(fruits[1])

print(fruits[2])

#➕ Adding Items to a List
'''1️⃣ Append (adds at the end):'''

cars.append("Ford Gt 40 ")

print(cars)

cars.append("toyota toms supra")

print(cars)

'''2️⃣ Insert (adds at a specific position):'''

cars.insert(0 , "Viper GTS")

print(cars)

cars.insert(3 , "Mustang Gt")

print(cars)


#❌ Removing Items from a List
'''1️⃣ Remove a specific item'''

numbers.remove(5)

print(numbers)

numbers.remove(3)

print(numbers)

'''2️⃣ Pop (removes by position)'''

cars.pop(4)

print(cars)

cars.pop(1)

print(cars)

'''3️⃣ Clear (removes everything)'''

cars.clear()

print(cars)

numbers.clear()

print(numbers)

fruits.clear()

print(fruits)


for fruit in fruits:

    print(fruit)

#🚀 Summary
'''A list is like a basket that holds multiple items.
Use [] to store multiple values.
Access items using index numbers (starting from 0).
Modify, add, or remove items easily.
Lists are one of the most used data types in Python!'''