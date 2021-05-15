
# Defining blue print for a living entity called Dog

# State: represented by the attributes of an object.
# Behavior: represented by the methods of an object.

class Dog():

    name= "Bruno"
    age= "3 months"

    def display(self):
        print("Printing Name of the Dog: ", self.name)
        print("Printing age of the Dog: ", self.age)
        print("Bie")


# Creating an living entity as copy of the blue print with actual values: instantiating a class as object.

dog1 = Dog()
print(dog1.name)
print(dog1.age)
print()
dog1.display()
