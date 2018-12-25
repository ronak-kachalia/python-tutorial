#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
##### Numbers and Variables #####
'''
#%%
# Addition - Subtraction - Multiplication - Division - Floor Division - Modulo
print(2+3)
print(5-3)
print(5*8)
print(10/3)
print(10//3)
print(3%5)
# Powers and Roots
print(4**2)
print(16**0.5)

#Round
print(round(3.1212121212,2))

# Exponentials
'''
The function pow() takes two arguments, equivalent to x^y. With three 
arguments it is equivalent to (x^y)%z, but may be more efficient for 
long integers.
'''
print(pow(3,4))
print(pow(3,4,5))
#%%
# Variables 
'''
The names you use when creating these labels need to follow a few rules:
1. Names can not start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
4. It's considered best practice (PEP8) that names are lowercase.
5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter 
oh), or 'I' (uppercase letter eye) as single character variable names.
6. Avoid using words that have special meaning in Python like "list" and "str"
'''
# Dynamic Typing
'''
Python uses dynamic typing, meaning you can reassign variables to different 
data types. this makes Python very flexible in assigning data types; it 
differs from other languages that are statically typed.
'''
#%%
my_var = 2
print(my_var)

my_var = ['dogs','cats']
print(my_var)
#%%
'''
Pros and Cons of Dynamic Typing

Pros of Dynamic Typing
very easy to work with
faster development time
Cons of Dynamic Typing
may result in unexpected bugs!
you need to be aware of type()
'''

'''
Determining variable type with type()
You can check what type of object is assigned to a variable using Python's 
built-in type() function. Common data types include:

int (for integer)
float
str (for string)
list
tuple
dict (for dictionary)
set
bool (for Boolean True/False)
'''
#%%
'''
##### Strings #####
'''
'''
NOTE: When applying methods to strings, always store it into other variables 
since Strings are immutable and thus effects will not be shown
example, 
s = 'Ronak Kachalia'
s.capitalize() # Incorrect
s = s.capitalize() # Correct
'''
#%%
# We can also use a function called len() to check the length of a string!
my_name = 'Ronak Kachalia'
len(my_name)
# String Indexing
print(my_name[4])
#%%
# Slicing
'''
[start index : end index : step]
Negative numbers denote reverse indexing
[:] blank index indicates ALL elements
'''
#%%
print(my_name[1:])
print(my_name[-1:])
print(my_name[1:4:2])
print(my_name[::])
#%%
'''
# STRINGS ARE IMMUTABLE
# But se can reassign string completely though!
'''
#%%
s = 'Ronak'
s[0] = 'r' #ERROR
s = s + ' Kachalia'
print(s)
#%%
# Built-In String Methods
name = 'Ronak Kachalia'
print(name.upper())
print(name.lower())
print(name.split()) # By blank spaces
print(name.split('K')) 
#%%
'''
##### Formatting #####
'''
s = 'Ronak'
s.center(20,'-')
#%%
'''
##### is check methods #####
'''
s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.isspace())
print(s.islower())
print(s.isupper())
print(s.endswith('o'))
#%%
'''
##### Print Formatting #####
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
#%%
'''
##### Lists and Tuples #####
'''
'''
Lists can be thought of the most general version of a sequence in Python. 
Unlike strings, they are mutable, meaning the elements inside a list can be 
changed!

NOTE: for iterating lists with values and index, use enumerate()
'''
#%%
my_list = [1,'two',['three',4]]
print(my_list[2][0])
#%%
# Indexing and Slicing
'''
Indexing and slicing work just like in strings
'''
#%%
# Basic List operations
my_list.append()
my_list.pop()
my_list.pop(1)
my_list.sort()
my_list.reverse()
my_list.remove()
my_list.remove('two')
#%%
# List Comprehensions
'''
Python has an advanced feature called list comprehensions. 
They allow for quick construction of lists.
'''
#%%
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
matrix = [lst_1,lst_2,lst_3]
first_col = [row[0] for row in matrix]
#%%
# Tuples
'''
Tuples are similar to Lists but immutable
'''
#%%
t = (1,2,3,'four')
#%%
'''
##### Dictionaries and Sets #####
'''
'''
A Python dictionary consists of a key and then an associated value. 
That value can be almost any Python object.

NOTE: For keys, we can use Strings, numbers, tuplesn Booleans and None.
Dictionaries allow duplicate keys but withh show warning. Also, it will print 
the value of the duplicate key of last entered value for that key
LISTS CANNOT BE USED AS KEYS
'''
#%%
# keys can be either String or Number
my_dict = {'key':'value', 'list':[1,'two',['three',4]], 1: 'Correct', 0.7: 'false'}
# Nesting with Dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])
#%%
# Dictionary methods
d.keys()
d.get('key')
d.items() # All key-value pairs
d.values() # All values
#%%
# Sets
'''
Sets contain only unique keys
Duplicates are treated as one

set(iterable): takes only one argument - iterable
'''
#%%
lst = [1,2,3,4,4]
s = set(lst)

x = set()
x.add(1)
x.add('friends')
#%%
'''
Advanced Sets
'''
'''
copy
returns a copy of the set. Note it is a copy, so changes to the original don't effect the copy.
'''
s = set()
s.add(1)
s.add(2)
s.add(3)
sc = s.copy()
s.add(4)
print(s)
print(sc)
#%%
'''
difference
difference returns the difference of two or more sets. The syntax is:
'''
print(s.difference(sc))
#%%
'''
difference_update
difference_update syntax is:

set1.difference_update(set2)
the method returns set1 after removing elements found in set2
'''
s1 = {1,2,3}
s2 = {1,4,5}
print(s1.difference_update(s2))
print(s1)
#%%
'''
intersection and intersection_update
Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
'''
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
print(s1)

'''
intersection_update will update a set with the intersection of itself and another.
'''
print(s1.intersection_update(s2))
print(s1)
#%%
'''
union
Returns the union of two sets (i.e. all elements that are in either set.)
'''
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.union(s2))
print(s1)
#%%
'''
discard
Removes an element from a set if it is a member. If the element is not a member, do nothing.
'''
s1 = {1,2,3}
s2 = {1,2,4}
s1.discard(2)
print(s1)
#%%
'''
update
Update a set with the union of itself and others
'''

s1.update(s2)
print(s1)
#%%
'''
Also,
    isdisjoint
    issubset
    issuperset
'''
#%%
'''
##### Chained Comparisons #####
'''
'''
An interesting feature of Python is the ability to chain multiple comparisons 
to perform a more complex test.
Using and and or
'''
#%%
print(1 < 2 < 3)
print(1<2 and 2<3)
print(1 < 3 > 2)
print(1==2 or 2<3)
#%%
'''
##### Python Statements #####
'''
#%%
x = 2
if x == 3:
    print('It\'s three')
elif x == 4:
    print('It\'s four')
else:
    print('oops')
#%%
# Ternary Operator

a,b,c=2,3,4
print('a is greater than be' if a >b else 'b is greater than a')
print('a is greater than be' if a >b else 'b is greater than a and c' if b > c else 'c is the greatest')
#%%   
# LOOPS
# FOR LOOP
my_list = [1,2,'three',['four',5]]
for items in my_list:
    print(items) 
#%%
my_dict = {'key':'value','key 2':'value'}
for k,v in my_dict.items():
    print(k)
    print(v)  
#%%
list2 = [(2,4),(6,8),(10,12)]
for (t1,t2) in list2:
    print(t2)
#%%   
for i in range(len(my_list)):
    print(i)
#%%
for i,j in zip(my_dict,my_list):
    print(i)
    print(j)
#%%   
# WHILE LOOP   
x = 10

while x > 0:
    print(x)
    x-=1
else:
    print('done')
#%%
'''
##### Useful Operators #####
'''
# Range
'''
The range function allows you to quickly generate a list of integers, this 
comes in handy a lot, so take note of how to use it! There are 3 parameters 
you can pass, a start, a stop, and a step size.
'''
#%%
print(range(0,10,2))
print(list(range(0,10,2)))
#%%
# Enumerate
'''
enumerate is a very useful function to use with FOR loops.
'''
#%%
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

l1 = ["eat","sleep","repeat"] 

for ele in enumerate(l1): 
    print(ele)

for count,ele in enumerate(l1,100): 
    print(count,ele )
    
print(enumerate(l1))
#%%
# Zip
mylist1=[1,2,3]
mylist2=[4,5,6]
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
#%%
# in operator
'x' in ['x','y','z']
'x' in [1,2,3]
#%%
# min and max
mylist = [10,20,30,40,100]
min(mylist)
max(mylist)
#%%
# Random
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)

from random import randint
# Return random integer in range [a, b], including both end points.
randint(0,100)
#%%
# Input
x = input('Enter')
print(x)
#%%
'''
##### List Comprehensions #####
'''
#%%
lst = [x for x in 'word']
lst
#%%
lst = [x**2 for x in range(0,11)]
lst
#%%
lst = [x for x in range(11) if x % 2 == 0]
lst
#%%
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
fahrenheit
#%%
lst = [ x**2 for x in [x**2 for x in range(11)]]
lst
#%%
lst=[[1,2],[2,3],[3,4]]
x = [items[0] for items in lst]
#%%
'''
##### Collections #####

The collections module is a built-in module that implements specialized 
container data types providing alternatives to Python’s general purpose 
built-in containers.
'''
#%%
'''
Counter

Counter is a dict subclass which helps count hashable objects. Inside of it 
elements are stored as dictionary keys and the counts of the objects are 
stored as the value.
'''

from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(lst))

print(Counter('aabsbsbsbhshhbbsbs'))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print(Counter(words))
#%%
'''
Methods with Counter()

Common patterns when using the Counter() object

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''
s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

c = Counter(words)

c.most_common(2)
#%%
'''
defaultdict

defaultdict is a dictionary-like object which provides all methods provided 
by a dictionary but takes a first argument (default_factory) as a default data 
type for the dictionary. Using defaultdict is faster than doing the same using 
dict.set_default method.
'''

from collections import defaultdict

# Normal
d = {}
# d['one'] # KeyError: 'one'

# defaultdict
d  = defaultdict(object)
print(d['one'])
print(d['four'])

for item in d:
    print(item)

'''
Can also initialize with default values:
'''
d = defaultdict(lambda: 0)
print(d['one'])
#%%
'''
OrderedDict

An OrderedDict is a dictionary subclass that remembers the order in which its 
contents are added.
'''

print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)


from collections import OrderedDict

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
#%%
'''
Equality with an Ordered Dictionary

A regular dict looks at its contents when testing for equality. An 
OrderedDict also considers the order the items were added.
'''

print('Dictionaries are equal?')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)

from collections import OrderedDict

print('Dictionaries are equal?')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)
#%%
'''
namedtuple

The arguments are the name of the new class and a string containing the names 
of the elements.
'''
from collections import namedtuple

D = namedtuple('Dog','age breed name')

sam = D(age=2,breed='Lab',name='Sammy')

frank = D(age=2,breed='Shepard',name="Frankie")

print(sam)
print(frank)
print(sam.breed)
print(sam[1])
#%%
'''
##### Methods #####
'''
'''
Methods are essentially functions built into objects.
Methods perform specific actions on an object and can also take arguments, 
just like a function.

Methods are in the form:
object.method(arg1,arg2,etc...)

Example:
For lists,
append, count, sort, pop, etc are the methods.
'''
#%%
lst = [1,2,3,4,5]
lst.sort(reverse=True)
lst
#%%
'''
##### Functions #####
'''
'''
Formally, a function is a useful device that groups together a set of 
statements so they can be run more than once. They can also let us specify 
parameters that can serve as inputs to the functions.

On a more fundamental level, functions allow us to not have to repeatedly 
write the same code again and again. 
'''
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
'''
##### Functions within functions #####
'''
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
'''
##### Returning Functions #####
'''
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
'''
##### Functions as Arguments #####
'''
def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello)
#%%
'''
##### Lambda Expressions, Map and Filter #####
'''
# MAPS
'''
The map function allows you to "map" a function to an iterable object. 
That is to say you can quickly call the same function to every item in an 
iterable, such as a list.
'''
#%%
# Map for Lists
def _square(x):
    return x*x;

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
# Filter
'''
The filter function returns an iterator yielding those items of iterable for 
which function(item) is true. Meaning you need to filter by a function that 
returns either True or False. Then passing that into filter (along with your 
iterable) and you will get back only the results that would return True when 
passed to the function.
'''
#%%
def _checkEven(v):
    return v%2 == 0

lst = [0,1,2,3,4,5,6,7,8,9]

print(list(filter(_checkEven,lst)))
#%%
# Lambda Expression
'''
One of Pythons most useful (and for beginners, confusing) tools is the 
lambda expression. lambda expressions allow us to create "anonymous" 
functions. This basically means we can quickly make ad-hoc functions 
without needing to properly define a function using def.

Function objects returned by running lambda expressions work exactly the same 
as those created and assigned by defs.
'''
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
#%%
'''
##### reduce() #####

Many times students have difficulty understanding reduce() so pay careful 
attention to this lecture. The function reduce(function, sequence) continually 
applies the function to the sequence. It then returns a single value.

If seq = [ s1, s2, s3, ... , sn ], calling reduce(function, sequence) works 
like this:

At first the first two elements of seq will be applied to function, i.e. 
func(s1,s2)
The list on which reduce() works looks now like this: [ function(s1, s2), 
s3, ... , sn ]
In the next step the function will be applied on the previous result and the 
third element of the list, i.e. function(function(s1, s2),s3)
The list looks like this now: [ function(function(s1, s2),s3), ... , sn ]
It continues like this until just one element is left and return this element 
as the result of reduce()
'''

from functools import reduce

lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)
#%%
'''
##### Nested Statements and Scope #####
'''
'''
LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), 
and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all 
enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or 
declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, 
range, SyntaxError,...

NOTE:
use the globals() and locals() functions to check what are your current local 
and global variables.

global/nonlocal variables
'''

x = 'global x'

def test():
    y = 'local y'
    print(y)
    global x
    print(x)
    def t2():
        z = 'local z'
        print(z)
        nonlocal y # refers to the enclosing function i.e test().y
        print(y)
    t2()
    
test()
#%%
'''
##### *args and **kwargs #####
'''
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

myfunc(40,60,20)
#%%
'''
*args

When a function parameter starts with an asterisk, it allows for an arbitrary 
number of arguments, and the function takes them in as a tuple of values. 
Rewriting the above function:
'''
def myfunc(*args):
    return sum(args)*.05
myfunc(40,60,20)

def myfunc(*spam):
    return sum(spam)*.05
myfunc(40,60,20)
#%%
'''
**kwargs

Similarly, Python offers a way to handle arbitrary numbers of keyworded 
arguments. Instead of creating a tuple of values, **kwargs builds a dictionary 
of key/value pairs. For example:
'''
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')
#%%
'''
*args and **kwargs combined

You can pass *args and **kwargs into the same function, but *args have to 
appear before **kwargs
'''
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')
#%%
'''
##### Duck typing #####
'''

# GENERALLY
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')
        
def quack_and_fly(thing):
    if(isinstance(thing,duck)):
        thing.quack()
        thing.fly()
    if(isinstance(thing,person)):
        thing.quack()
        thing.fly()
        
d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p)

# DUCK TYPING
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')
        
def quack_and_fly(thing):
    thing.quack()
    thing.fly()

d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p)
#%%
'''
##### Asking Forgiveness #####
'''
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

def quack_and_fly(thing):
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing,'fly'):
        if callable(thing.fly):
            thing.fly()

d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p)  
#%%
'''
Not Permission

EAFP: Easier to Ask Forgiveness than Permission

LBYL: Look Befor You Leap
'''  

# EAFP
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')
       
    def quack_and_fly(thing):
        try:
            thing.quack()
            thing.fly()
        except AttributeError as e:
            print(e)
        
d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p) 
#%%
'''
LBYL vs EAFP
'''
my_dict = {'name':'ronak','age':22}

#LBYL
if 'name' in my_dict and 'age' in my_dict:
    print(f'{my_dict["name"]} - {my_dict["age"]}')
else:
    print('Some keys are missing')
    
#EAFP
try:
    print(f'{my_dict["name"]} - {my_dict["age"]}')
except KeyError as e:
    print(e)

#%%
'''
##### OOP #####
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
#%%
'''
##### Decorators #####

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
#%%
'''
##### Iterators and Generators #####
'''
'''
Generators allow us to generate as we go along, instead of holding everything 
in memory.
Generator functions allow us to write a function that can send back a value 
and then later resume to pick up where it left off. This type of function is a 
generator in Python, allowing us to generate a sequence of values over time. 
The main difference in syntax will be the use of a yield statement.

In most aspects, a generator function will appear very similar to a normal 
function. The main difference is when a generator function is compiled they 
become an object that supports an iteration protocol. That means when they are 
called in your code they don't actually return a value and then exit. Instead, 
generator functions will automatically suspend and resume their execution and 
state around the last point of value generation. The main advantage here is 
that instead of having to compute an entire series of values up front, the 
generator computes one value and then suspends its activity awaiting the next 
instruction. This feature is known as state suspension.
'''
def gencubes(n):
    for num in range(n):
        print('Inside generator')
        yield num**3

for x in gencubes(10):
    print('Inside loop')
    print(x)

'''
NOTE: Notice that if we call some huge value of n (like 100000) the second 
function will have to keep track of every single result, when in our case we 
actually only care about the previous result to generate the next one!
'''
#%%
'''
next() and iter() built-in functions
'''
def simple_gen():
    for x in range(3):
        yield x
        
g = simple_gen()
print(next(g))


s = 'hello'
s_iter = iter(s)
next(s_iter)
#%%
'''
##### Underscores #####
'''
# 1. Single Leading Underscore: _var
'''
Single underscores are a Python naming convention indicating a name is 
meant for internal use. It is generally not enforced by the Python interpreter 
and meant as a hint to the programmer only.
'''
#%%
# 2. Single Trailing Underscore: var_
'''
a single trailing underscore (postfix) is used by convention to avoid naming 
conflicts with Python keywords
example:
    we cannot use 'type' as variable.
    but we can use 'type_' as variable to avoid conflicts
'''
#%%
# 3. Double Leading Underscore: __var
'''
A double underscore prefix causes the Python interpreter to rewrite the 
attribute name in order to avoid naming conflicts in subclasses.

This is also called name mangling—the interpreter changes the name of the 
variable in a way that makes it harder to create collisions when the class is 
extended later.
'''
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

x = Test()
print(dir(x))
print(x.foo)
print(x._bar)
# print(x.__baz) # ERROR
print(x._Test__baz) # CORRECT

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
#%%
x = ExtendedTest()
print(dir(x))
print(x.foo)
print(x._bar)
# print(x.__baz) # ERROR
print(x._ExtendedTest__baz) # CORRECT
#%%
# Mangled Method
class Test:
    def __init__(self):
        pass
    def __mymethod(self):
        print('Mangled method call successful!')

x = Test()
# print(x.__mymethod()) # Erroe
print(x._Test__mymethod()) # Correct
#%%
'''
What’s a “dunder” in Python?

Double underscores are often referred to as “dunders” in the Python community.
For example, you’d pronounce __baz as “dunder baz”. Likewise __init__ would be 
pronounced as “dunder init”, even though one might think it should be “dunder 
init dunder.” But that’s just yet another quirk in the naming convention. 
'''
#%%

# 4. Double Leading and Trailing Underscore: __var__
'''
names that have both leading and trailing double underscores are reserved for 
special use in the language. This rule covers things like __init__ for object 
constructors, or __call__ to make an object callable.
'''
#%%
# 5. Single Underscore: _
'''
Per convention, a single standalone underscore is sometimes used as a name to 
indicate that a variable is temporary or insignificant.

For example, in the following loop we don’t need access to the running index 
and we can use “_” to indicate that it is just a temporary value:
'''
for _ in range(10):
    print('Hello')
#%%
for _ in range(10):
    print(_)
#%%
a, _, b = 1,2,3
print(f'{a},{_},{b}')
#%%
'''
Besides its use as a temporary variable, “_” is a special variable in most 
Python REPLs that represents the result of the last expression evaluated by 
the interpreter.
'''
'''
>>> 20 + 3
23
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]
'''
#%%
'''
##### Exception Handling #####
'''
'''
try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 
'''

try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError as e:
    # This will only check for an IOError exception and then execute this print statement
    print(e)
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

#%%
    
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
finally:
    print("Finally, I executed!")
#%%
'''
any() vs all()
'''
lst = [True,True,False,True]

print(all(lst))

print(any(lst))
#%%
'''
complex()
'''
print(complex(2,3))

'''
N O T E: 
    If the first parameter is a string, it will be interpreted as a complex 
    number and the function must be called without a second parameter.
'''

print(complex('2+5j'))
#%%
'''
##### Files #####
'''
my_file = open('test.txt','w+')
#%%
'''
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

Opening a file with 'w' or 'w+' truncates the original, meaning that anything 
that was in the original file is deleted!
'''
my_file.write('Hello. This is my first line.')
#%%
# Seek to the start of file (index 0)
my_file.seek(0)
my_file.read()
#%%
my_file.write('\nSo how was your day?')
#%%
my_file.seek(0)
my_file.readlines()
#%%
my_file.close()
#%%
'''
Appending
'''
my_file = open('test.txt','a+')
#%%
my_file.write('\nHello World')
#%%
my_file.seek(0)
my_file.read()
my_file.seek(0)
my_file.readlines()
#%%
my_file.seek(0)
my_file.write('Have I become the first line?\n')
#%%
my_file.seek(0)
my_file.readlines()
#%%
'''
Printing single lines at a time
'''
# Pertaining to the first point above
for asdf in open('test.txt'):
    print(asdf)
#%%
'''
##### DateTime #####
'''
import datetime
# Time
# datetime.time(hour,minute,second,microsecond)

t = datetime.time(4,20,1)
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

#%%
# Dates
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

d1 = datetime.date(2018,12,24)
d2 = datetime.date(2017,12,24)
print(d1)
print(d2)
print(d1-d2)
#%%
'''
##### Timing your code #####
'''
import timeit

# For loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
#%%
'''
##### StringIO Objects and the io Module #####

Text data is stored in a StringIO object, while binary data would be stored in 
a BytesIO object. This object can then be used as input or output to most 
functions that would expect a standard file object.
'''
import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

f.read()

f.write(' Second line written to file like object')

# Reset cursor just like you would a file
f.seek(0)

# Read again
f.read()

f.close()
#%%
'''
##### Modules and Packages #####
'''
# Ronak duplicate update