#%%
'''
##### Lecture 17: Underscores #####
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

Dunder methods are also referred to as 'Magic methods'
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