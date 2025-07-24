"""3. Modifying Class-Level Data

Class methods can modify class-level data 
that is shared across all instances."""

#🌐 Example 2: Modify Class-Level Data

class Counter:
    count = 0  #class level variable.

    @classmethod
    def increment(cls):
        cls.count +=1

Counter.increment()
Counter.increment()
print(Counter.count)