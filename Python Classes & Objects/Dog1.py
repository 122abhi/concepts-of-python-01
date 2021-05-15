# A Class is blueprint fora n entity while instance/object is a copy of the class with actual values

# State: Defines attributes for an object
# Behaviours: Defines possible behaviours of an object.

# class variables: unique to a class, shared among all objects. Defined in the class.
# instance attributes: Not unique to a class, each object have it's own actual values, Defined in __init__ constructor
# or methods of the class

# self is used to refer an object/instance itself in it's methods. It need not be passed but is taken automatically taken by python
# while calling the function. Writing self/any-other-name is compulsory as 1st parameter while defining a method.

class Dog():

    # Class Variable
    animal= "Dog"

    # creating instance variable using __init__ constructor
    def __init__(self,breed):
        self.breed= breed

    # creating instance variable using a method constructor
    def setColor(self, color):
        self.color= color

    def getColor(self):
        return self.color


# Driver code

Rodger= Dog("Labrador")
Rodger.setColor("Golden Brown")
print(Rodger.getColor())


# https://medium.com/python-features/class-vs-instance-variables-8d452e9abcbd