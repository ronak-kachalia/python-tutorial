# =============================================================================
##### Decorators #####
# =============================================================================

# =============================================================================
# Decorators can be thought of as functions which modify the functionality of 
# another function. They help to make your code shorter and more "Pythonic".
# =============================================================================
#%%
# As seen in closure
def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function

# Now here, instead of printing message
# we'll be acception a function as an argument
# and execute the function
#%%
# Decorator
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran!')

decorated_display = decorator_function(display)
decorated_display()

# =============================================================================
# Decorating our function allows us to easily add
# functionality to our existing functions by adding
# that functionality inside our wrapper
# =============================================================================
#%%
# @Decorator
def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed before')
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran!')

# =============================================================================
# Using @decorator is same as using
# display = decorator_function(display)
# =============================================================================
display()
#%%
@decorator_function
def display_info(name,age):
    print(f'{name}:{age}')

display_info('Ronak',22) # ERROR. Since our wrapper doesnt accept any arguments

# Lets modify it

#%%
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed before')
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name,age):
    print(f'{name}:{age}')

display_info('Ronak',22)
#%%

# =============================================================================
# Class as a Decorator 
# =============================================================================
#%%
class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self,*args,**kwargs): # Behaves like wrapper function
        print('call method executed before')
        return self.original_function(*args,**kwargs)
    
@decorator_class
def display_info(name,age):
    print(f'{name}:{age}')

display_info('Ronak',22)
#%%
# =============================================================================
# The __call__ method

# The __call__ method can be used to turn the instances of the class into 
# callables. Functions are callable objects. A callable object is an object 
# which can be used and behaves like a function but might not be a function. 
# By using the __call__ method it is possible to define classes in a way that 
# the instances will be callable objects. The __call__ method is called, if the 
# instance is called "like a function", i.e. using brackets. The following 
# example defines a class with which we can create abitrary polynomial functions:
# =============================================================================
class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
        
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res

# a constant function
p1 = Polynomial(42)

# a straight Line
p2 = Polynomial(0.75, 2)

# a third degree Polynomial
p3 = Polynomial(1, -0.5, 0.75, 2)

for i in range(1, 10):
    print(i, p1(i), p2(i), p3(i))
#%%
# =============================================================================
# Practical Example:
#     Logging function
# =============================================================================
#%%
# =============================================================================
# Wraps

# wraps is used to get correct name of the method called
# otherwise, __name__ will return the name of the wrapper function
# =============================================================================
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)