#%%
'''
##### Lecture 3: Print Formatting #####
'''
# String Formatting
'''
String formatting lets you inject items into a string rather than trying to 
chain items together using commas or string concatenation. As a quick 
comparison, consider:
'''
#%%
player = 'Thomas'
points = 33
print('Last night, '+player+' scored '+str(points)+' points.') # concatenation
print(f'Last night, {player} scored {points} points.') # string formatting
#%%
'''
There are three ways to perform string formatting.
1. The oldest method involves placeholders using the modulo % character.
2. An improved technique uses the .format() string method.
3. The newest method, introduced with Python 3.6, uses formatted string 
literals, called f-strings.
'''
#%%
# Using Module % character
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))
x = 1
print('here is x: %s' %(x))
#%%
'''
Format conversion methods.

It should be noted that two methods %s and %r convert any python object to a 
string using two separate methods: str() and repr(). We will learn more about 
these functions later on in the course, but you should note that %r and repr() 
deliver the string representation of the object, including quotation marks and 
any escape characters.
'''
#%%
print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')

print('I once caught a fish %s.' %'this \tbig')
print('I once caught a fish %r.' %'this \tbig')
#%%
# str vs repr
'''
str() is used for creating output for end user while repr() is mainly used for 
debugging and development. repr’s goal is to be unambiguous and str’s is to be 
readable. For example, if we suspect a float has a small rounding error, repr 
will show us while str may not.repr() compute the “official” string 
representation of an object (a representation that has all information about 
the abject) and str() is used to compute the “informal” string representation 
of an object (a representation that is useful for printing the object).The 
print statement and str() built-in function uses __str__ to display the string 
representation of the object while the repr() built-in function uses __repr__ 
to display the object.
'''
# %s vs %d
'''
The %s operator converts whatever it sees into a string, including integers 
and floats. The %d operator converts numbers to integers first, without 
rounding. Note the difference below:
'''
#%%
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)
#%%
# Floating Numbers
'''
Padding and Precision of Floating Point Numbers
Floating point numbers use the format %5.2f. Here, 5 would be the minimum 
number of characters the string should contain; these may be padded with 
whitespace if the entire number does not have this many digits. Next to this, 
.2f stands for how many numbers to show past the decimal point.
'''
#%%
print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %25.2f' %(13.144))
#%%
# Formatting with the .format() method
print('This is a string with an {}'.format('insert'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
#%%
# Formatted String Literals (f-strings)
name = 'Ronak'
print(f"He said his name is {name}.")
#%%
# Float formatting follows "result: {value:{width}.{precision}}"
'''
Where with the .format() method you might see {value:10.4f}, 
with f-strings this can become {value:{10}.{6}}
'''
#%%
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
#%%
'''
Note that with f-strings, precision refers to the total number of digits, 
not just those following the decimal. This fits more closely with scientific 
notation and statistical analysis. Unfortunately, f-strings do not pad to the 
right of the decimal, even if precision allows it:
'''
#%%
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

