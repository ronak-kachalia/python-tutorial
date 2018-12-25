#%%
'''
##### Lecture 15: Decorators #####

Decorators can be thought of as functions which modify the functionality of 
another function. They help to make your code shorter and more "Pythonic".
'''
#%%
'''
##### Creating Decorator #####
'''
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()
# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
#%%
'''
##### Creating Decorator using '@' #####
'''
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()
#%%
'''
GETTERS AND SETTERS (Mutator Methods)

Property

property(fget=None, fset=None, fdel=None, doc=None)

where, fget is function to get value of the attribute, fset is function to 
set value of the attribute, fdel is function to delete the attribute and doc 
is a string (like a comment). As seen from the implementation, these function 
arguments are optional.
'''
class Temperature:
    def __init__(self, temperature = 0):
        self.temperature = temperature
        
    def get_temperature(self):
        return self._temperature
        
    def set_temperature(self,temperature):
        self._temperature = temperature
        
        
    temperature = property(get_temperature, set_temperature)

x = Temperature()
x.temperature = 10
print(x.temperature)
#%%
'''
A property object has three methods, getter(), setter(), and deleter() to 
specify fget, fset and fdel at a later point. This means, the line
'''
class Temperature:
    def __init__(self, temperature = 0):
        self.temperature = temperature
        
    def get_temperature(self):
        return self._temperature
        
    def set_temperature(self,temperature):
        self._temperature = temperature
    # make empty property
    temperature = property()
    # assign fget
    temperature = temperature.getter(get_temperature)
    # assign fset
    temperature = temperature.setter(set_temperature)
#%%
'''
@Property decorator
'''
class P:
    def __init__(self,x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

y = P(20)
print(y.x)
y.x = 30
print(y.x)
#%%
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

t = Celsius()
t.temperature = 30
print(t.temperature)
print(t._temperature)
print(t.to_fahrenheit())
t.temperature = 50
print(t.temperature)
print(t._temperature)
print(t.to_fahrenheit())
#%%
class Person:
    def __init__(self,name):
        self.first_name = name
    
    @property
    def first(self):
        return self.first_name
    @first.setter
    def first(self,value):
        self.first_name = value

x = Person('ronak')
print(x.first)
x.first = 'rahul'
print(x.first)