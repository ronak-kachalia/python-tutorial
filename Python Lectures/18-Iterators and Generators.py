# =============================================================================
##### Iterators and Generators #####
# =============================================================================

# =============================================================================
# Generators allow us to generate as we go along, instead of holding everything 
# in memory.
# Generator functions allow us to write a function that can send back a value 
# and then later resume to pick up where it left off. This type of function is a 
# generator in Python, allowing us to generate a sequence of values over time. 
# The main difference in syntax will be the use of a yield statement.

# In most aspects, a generator function will appear very similar to a normal 
# function. The main difference is when a generator function is compiled they 
# become an object that supports an iteration protocol. That means when they are 
# called in your code they don't actually return a value and then exit. Instead, 
# generator functions will automatically suspend and resume their execution and 
# state around the last point of value generation. The main advantage here is 
# that instead of having to compute an entire series of values up front, the 
# generator computes one value and then suspends its activity awaiting the next 
# instruction. This feature is known as state suspension.
# =============================================================================
def gencubes(n):
    for num in range(n):
        print('Inside generator')
        yield num**3

for x in gencubes(10):
    print('Inside loop')
    print(x)

# =============================================================================
# NOTE: Notice that if we call some huge value of n (like 100000) the second 
# function will have to keep track of every single result, when in our case we 
# actually only care about the previous result to generate the next one!
# =============================================================================
#%%
# =============================================================================
next() and iter() built-in functions (For String)
# =============================================================================
def simple_gen():
    for x in range(3):
        yield x
        
g = simple_gen()
print(next(g))


s = 'hello'
s_iter = iter(s)
next(s_iter)