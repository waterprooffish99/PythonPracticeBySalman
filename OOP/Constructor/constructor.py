# __init__ Function. It is called Constructor.
# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Creating a class
# class Student:
#     name = "Karan Kumrar"
#     def __init__(self):                             #whenever we run an object or class this __init__ is always called/ invoke.
#         print(self)                                 # this will print "<__main__.Student object at 0x000001F3E59CD610>"
#         print("Adding New Student To The Class.")   # this will print "Adding new...."

# s1 = Student()
class Student:
    collegeName = "ABC College" #  This is called class Attributes, it is written one time and it is for all the students because all are studying in the same college.
    def __init__(self, name, marks):
        self.name = name        #  This is called Object Attributes
        self.marks = marks      #  This is called Object Attributes
        

# Creating an object....

s1 = Student("karan kumar", 65)
print(s1.name , s1.marks)

s2 = Student("arjun", 87)
print(s2.name , s2.marks)

s3 = Student("ram lal", 62)
print(s3.name , s3.marks)

s4 = Student("naresh kumar", 56)
print(s4.name, s4.marks)

s5 = Student("Pallavi", 98)
print(s5.name, s5.marks)

s6 = Student("Poorvi", 76)
print(s6.name, s6.marks)