# =============================================================================
##### Lambda Expressions, Map and Filter #####
# =============================================================================

# =============================================================================
# MAPS:

# The map function allows you to "map" a function to an iterable object. 
# That is to say you can quickly call the same function to every item in an 
# iterable, such as a list.
# =============================================================================
#%%
# Map for Lists
def _square(x):
    return x*x

lst = [1,2,3,4]

result = map(_square,lst)

print(list(result))
#%%
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
    
mynames = ['John','Cindy','Sarah','Kelly','Mike']

list(map(splicer,mynames))
#%%
# Map for Dictionary
def _cube(v1,v2):
    return(v1+v2)

dic = {0:1,1:5,2:87,3:99}

print(list(map(_cube,dic.values(),dic.values())))
#%%
# =============================================================================
# Filter:

# The filter function returns an iterator yielding those items of iterable for 
# which function(item) is true. Meaning you need to filter by a function that 
# returns either True or False. Then passing that into filter (along with your 
# iterable) and you will get back only the results that would return True when 
# passed to the function.
# =============================================================================
#%%
def _checkEven(v):
    return v%2 == 0

lst = [0,1,2,3,4,5,6,7,8,9]

print(list(filter(_checkEven,lst)))
#%%
# =============================================================================
# Lambda Expression:

# One of Pythons most useful (and for beginners, confusing) tools is the 
# lambda expression. lambda expressions allow us to create "anonymous" 
# functions. This basically means we can quickly make ad-hoc functions 
# without needing to properly define a function using def.

# Function objects returned by running lambda expressions work exactly the same 
# as those created and assigned by defs.
# =============================================================================
#%%
# keep in mind that not every function can be translated into a lambda expression.
#%%
# Function
def square(num): return num**2

# Lambda
lambda num: num ** 2

lst = [1,2,3,4,5]

print(list(map(lambda num: num ** 2, lst)))

print(list(filter(lambda n: n % 2 == 0,lst)))

#%%

s = 'Ronak Kachalia'

s[:-5:-1]

#%%
lambda s: s[0]
#%%
lamb = lambda s: s[::-1]
print(lamb('Ronak Kachalia'))
#%%
lambda x,y : x + y