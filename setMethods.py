'''Python Set Methods (With Explanation & Practice)
A set in Python is an unordered collection of unique elements. It doesn’t allow duplicates, and it’s useful when you need to store distinct values.

Let’s go through the most commonly used set methods, one by one, with simple explanations and practice examples.'''

# 1️⃣ Creating a Set
#Syntax:

my_set = {10 , 20 , 30 , 40 , 50} # set with numbers...

words = {"brave" , "cowered" , "unhinged" , "ambush"} # set with strings...

# A set automatically removes duplicates...

integers = { 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 6 , 7 , 7 }

print(integers) # automatically removes duplicates...

# 2️⃣ Adding Elements
# add() – Adds a single element

fruits = {"apple" , "orange" , "cherry"}

fruits.add("mango") # adds orange in the set...
print(fruits)
# if the element is already in the set , nothing happens...

# 3️⃣ Removing Elements
#remove() – Removes a specific item (Raises an error if not found)

fruits.remove("orange") # removes orange in the set
print(fruits)

#fruits.remove("Kela") # throws an error because Kela is not the set.

# discard() – Removes an item just like remove() the only difference is (No error if not found)

fruits.discard("cherry")

print(fruits)


# pop() – Removes and returns a random element

item = fruits.pop()

print(item)

#since sets are unordered, so we don't know which element is removed.