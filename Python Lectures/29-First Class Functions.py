'''
##### Lecture 29: Firsst Class Functions and Closures. (Also known as High Order Dunctions)#####
'''
'''
In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures.
'''
#%%
# Generally

def square(x):
    return x*x

f = square(5)
print(square)
print(f)
#%%
#%%
# First class functions
'''
# Functions as Variables
'''
def square(x):
    return x*x
# Function stored in a variable
# Later this variable can be accessed as a function
f = square
print(square)
print(f)
print(f(5))
#%%
'''
# Passing a function as an argument
'''
def square(x):
    return x*x
def my_map(func,lst):
    result = []
    for i in lst:
        result.append(func(i))
    return result

squares = my_map(square,[1,2,3,4,5])
print(squares)
#%%
def cube(x):
    return x*x*x

cubes = my_map(cube,[1,2,3,4,5])
print(cubes)
#%%
'''
# Return a function from another function
'''
def log(msg):

    def printmsg():
        print(f'log: {msg}')
    
    return printmsg

l = log('message')
l()
#%%
def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    
    return wrap_text

print_h1 = html_tag('h1') # Parameter for outermost function
print(print_h1) # Will only print address
print(print_h1('Hello')) # Parameter for innter function
#%%
'''
##### Closures #####

A closure is inner function that remembers and has
access to variables in the local scope created even
after the outer function has finished the execution

The criteria that must be met to create closure in Python are summarized in the following points.

We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.

When to use?
Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.
When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.
'''
# In below example, it will print 'message'
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    
    return inner_func()

outer_func()
#%%
# Now, when we remove the paranthesis from the 
# return statement, what we get as output is the 
# function itself

# This is because, we have returned the function 
# and not executed that function as there are 
# no paranthesis

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    
    return inner_func

print(outer_func())
# OR
my_func = outer_func()
print(my_func)

# To run, use paranthesis
my_func()

# Now read the description of Closure above
#%%
# Closure with multiple inner funstions
def outer_func():
    message = 'Hi'
    def inner_func_1(msg):
        print(message)
        print(msg)
    def inner_func_2(msg):
        print(message)
        print(msg)
    
    return inner_func_1,inner_func_2

my_func_1, my_func_2 = outer_func()
my_func_1('Hello')
my_func_2('Bye')