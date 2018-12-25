#%%
'''
##### Lecture 14: OOP #####
'''
# CLASS
class Sample:
    pass

x = Sample()

type(x)
#%%
'''
An attribute is a characteristic of an object. 
A method is an operation we can perform with the object.
'''
# Attributes
'''
The syntax for creating an attribute is:
    self.attribute = something
    
There is a special method called:
    __init__()
This method is used to initialize the attributes of an object
'''
class Dog:
    def __init__(self,breed):
        self.breed = breed

sam = Dog('sam')
ham = Dog('ham')

print(sam)
print(ham)
print(sam.breed)
print(ham.breed)

'''
Lets break down what we have above.The special method

    __init__() 

is called automatically right after the object has been created:
    def __init__(self, breed):
    
Each attribute in a class definition begins with a reference to the instance 
object. It is by convention named self. The breed is the argument. The value 
is passed during the class instantiation.

    self.breed = breed
'''
#%%
'''
In Python there are also class object attributes. These Class Object 
Attributes are the same for any instance of the class. For example, we could 
create the attribute species for the Dog class. Dogs, regardless of their 
breed, name, or other attributes, will always be mammals. We apply this logic 
in the following manner:
'''
class Dog:
    species = 'mammal'
    def __init__(self,breed):
        self.breed = breed

sam = Dog('sam')
ham = Dog('ham')
print(sam.species)
print(ham.species)
#%%
# Methods
'''
Methods are functions defined inside the body of a class. They are used to 
perform operations with the attributes of our objects. Methods are a key 
concept of the OOP paradigm. They are essential to dividing responsibilities 
in programming, especially in large applications.
'''
class Circle:
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = self.radius ** 2 * Circle.pi
    def setRadius(self,radius):
        self.radius = radius
        self.area = self.radius ** 2 * self.pi
    def getCircumference(self):
        return self.radius * self.pi * 2

x = Circle()
print(x.radius)
print(x.area)
print(x.getCircumference())

x.setRadius(2)
print(x.radius)
print(x.area)
print(x.getCircumference())
#%%
# Special Methods
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book
#%%
'''
self variables are necessary if they are to be used by other methods
Also, check below example
'''
class Vehicle:
    sound = 'Vroom'
    def __init__(self,name):
        self.name = name
    def __str__(self):
        # return f'Name: {name}' # NameError: name 'name' is not defined
        return f'Name: {self.name}'
    def variableWithoutSelf(self):
        self.age = 20
    def print_(self,age):
        print(age)

x = Vehicle('Car')
print(x)
x.print_(30)
y = Vehicle('bike')
y.print_(20)
# print(x.age) # since variabke is not defined self, error will occur
print(x.name)
#%%
# Inheritance

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

x = Animal()
y = Dog()
print(y.eat())
#%%
# Polymorphism


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())
#%%
# Class variables
class someClass():
    var = 1

x = someClass()
print(x.var)
print(someClass().var)
y = someClass()
print(y.var)

'''
var is a static class variable of someClass.

When you reach out to get x.var, y.var or some_other_instance.var, 
you are accessing the same variable, not an instance derived one (as long as 
you didn't specifically assigned it to the instance as a property).
'''
x.var = 2
print(someClass().var)
print(x.var) # now var acts as property for x
print(y.var)
#%%
# Instance, Class and Static Methods

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
#%%
'''
Instance Methods
The first method on MyClass, called method, is a regular instance method. 
That’s the basic, no-frills method type you’ll use most of the time. You can 
see the method takes one parameter, self, which points to an instance of 
MyClass when the method is called (but of course instance methods can accept 
more than just one parameter).

Through the self parameter, instance methods can freely access attributes and 
other methods on the same object. This gives them a lot of power when it comes 
to modifying an object’s state.

Not only can they modify object state, instance methods can also access the 
class itself through the self.__class__ attribute. This means instance methods 
can also modify class state.
'''
#%%
'''
N O T E:
    python doesn’t support method overloading like C++ or Java 
'''
#%%
# Class Methods and Static Methods
'''
Class Methods

The @classmethod decorator, is a builtin function decorator that is an 
expression that gets evaluated after your function is defined. The result of 
that evaluation shadows your function definition.
A class method receives the class as implicit first argument, just like an 
instance method receives the instance

@classmethod
    def fun(cls, arg1, arg2, ...):
        
A class method is a method which is bound to the class and not the object of 
the class.
They have the access to the state of the class as it takes a class parameter 
that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the 
class. For example it can modify a class variable that will be applicable to 
all the instances.

N O T E: class methods can be used as an alternative to create instance of 
objects
'''

'''
Static Methods

A static method does not receive an implicit first argument.

@staticmethod
    def fun(arg1, arg2, ...):

A static method is also a method which is bound to the class and not the 
object of the class.
A static method can’t access or modify class state.
It is present in a class because it makes sense for the method to be 
present in class.


When to use what?

We generally use class method to create factory methods. Factory methods 
    return class object ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
'''
#%%
# CLass methods
class Test:
    raise_amount = 1000
    def __init__(self):
        pass
    @classmethod
    def classmeth(cls,amount):
        cls.raise_amount = amount

x = Test()
print(x.raise_amount)
Test.classmeth(2000)
print(x.raise_amount)
#%%
# Class methods to create instance
'''
Suppose we get input as String and need to convert that into an instance of the class:
    'Name-age-salary'
'''
class Test:
    def __init__(self,name,age,salary):
        self.age = age
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls,emp_str):
        name,age,salary = emp_str.split('-')
        return cls(name,age,salary)

x = Test('name','age','salary')
y = Test.from_string('name-age-salary')
#%%
# Static methods

class Test:
    def __init__(self,name,age,salary):
        self.age = age
        self.name = name
        self.salary = salary
    @staticmethod
    def is_workday(day):
        if(1 <= day >= 5):
            print('true')
        else:
            print('false')

Test.is_workday(5)
#%%
'''
Factory method

We may not always know what kind of objects we want to create in advance.
Some objects can be created only at execution time after a user requests so.

Examples when you may use a factory method:

A user may click on a certain button that creates an object.
A user may create several new documents of different types.
If a user starts a webbrowser, the browser does not know in advance how many 
tabs (where every tab is an object) will be opened.
'''