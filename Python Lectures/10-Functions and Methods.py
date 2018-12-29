# =============================================================================
##### Functions and Methods #####
# =============================================================================

# =============================================================================
# Methods:

# Methods are essentially functions built into objects.
# Methods perform specific actions on an object and can also take arguments, 
# just like a function.

# Methods are in the form:
# object.method(arg1,arg2,etc...)

# Example:
# For lists,
# append, count, sort, pop, etc are the methods.
# =============================================================================
#%%
lst = [1,2,3,4,5]
lst.sort(reverse=True)
lst
#%%
# =============================================================================
# Functions:

# Formally, a function is a useful device that groups together a set of 
# statements so they can be run more than once. They can also let us specify 
# parameters that can serve as inputs to the functions.

# On a more fundamental level, functions allow us to not have to repeatedly 
# write the same code again and again. 
# =============================================================================
#%%
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (docstring) goes
    '''
    # Do stuff here
    # Return desired result
    
def add_numbers(num1,num2):
    pass # The pass statement is a null operation; nothing happens when 
         # it executes.   
#%%
# =============================================================================
# Functions within functions
# =============================================================================
def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()
welcome() # Error
#%%
# =============================================================================
# Returning Functions
# =============================================================================
def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()
x
print(x())
#%%
# =============================================================================
# Functions as Arguments
# =============================================================================
def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello)