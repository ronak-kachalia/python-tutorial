# =============================================================================
##### Underscores #####
# =============================================================================

# =============================================================================
# 1. Single Leading Underscore: _var

# Single underscores are a Python naming convention indicating a name is 
# meant for internal use. It is generally not enforced by the Python interpreter 
# and meant as a hint to the programmer only.

# Now if you use a wildcard import to import all names from the module, Python will 
# not import names with a leading underscore (unless the module defines an __all__ 
# list that overrides this behavior):
# =============================================================================
# This is my_module.py:
def external_func():
    return 23

def _internal_func():
    return 42

from my_module import *
external_func()
23
_internal_func()
NameError: "name '_internal_func' is not defined"

#%%
# Unlike wildcard imports, regular imports are not affected by the leading single 
# underscore naming convention:

import my_module
my_module.external_func()
23
my_module._internal_func()
42
#%%
# =============================================================================
# 2. Single Trailing Underscore: var_

# a single trailing underscore (postfix) is used by convention to avoid naming 
# conflicts with Python keywords
# example:
#     we cannot use 'type' as variable.
#     but we can use 'type_' as variable to avoid conflicts
# =============================================================================
#%%
# =============================================================================
# 3. Double Leading Underscore: __var

# A double underscore prefix causes the Python interpreter to rewrite the 
# attribute name in order to avoid naming conflicts in subclasses.

# This is also called name mangling—the interpreter changes the name of the 
# variable in a way that makes it harder to create collisions when the class is 
# extended later.
# =============================================================================
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
print(Test()._Test__baz)

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
# =============================================================================
# Mangled Method
# =============================================================================
class Test:
    def __init__(self):
        pass
    def __mymethod(self):
        print('Mangled method call successful!')

x = Test()
# print(x.__mymethod()) # Erroe
print(x._Test__mymethod()) # Correct
#%%
# Double underscore name mangling is fully transparent to the programmer. Take 
# a look at the following example that will confirm this:

class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

>>> ManglingTest().get_mangled()
'hello'
>>> ManglingTest().__mangled
AttributeError: "'ManglingTest' object has no attribute '__mangled'"
#%%
# =============================================================================
# What’s a “dunder” in Python?

# Double underscores are often referred to as “dunders” in the Python community.
# For example, you’d pronounce __baz as “dunder baz”. Likewise __init__ would be 
# pronounced as “dunder init”, even though one might think it should be “dunder 
# init dunder.” But that’s just yet another quirk in the naming convention. 

# Dunder methods are also referred to as 'Magic methods'

# Magic Methods:
# The so-called magic methods have nothing to do with wizardry. You have already 
# seen them in previous chapters of our tutorial. They are special methods with 
# fixed names. They are the methods with this clumsy syntax, i.e. the double 
# underscores at the beginning and the end. They are also hard to talk about. How 
# do you pronounce or say a method name like __init__? "Underscore underscore init 
# underscore underscore" sounds horrible and is nearly a tongue twister. "Double 
# underscore init double underscore" is a lot better, but the ideal way is "dunder 
# init dunder"1 That's why magic methods methods are sometimes called dunder 
# methods! 

# So what's magic about the __init__ method? The answer is, you don't have to 
# invoke it directly. The invocation is realized behind the scenes. When you create 
# an instance x of a class A with the statement "x = A()", Python will do the 
# necessary calls to __new__ and __init__. 
# =============================================================================
#%%
# =============================================================================
# 4. Double Leading and Trailing Underscore: __var__

# names that have both leading and trailing double underscores are reserved for 
# special use in the language. This rule covers things like __init__ for object 
# constructors, or __call__ to make an object callable.
# =============================================================================
#%%
# =============================================================================
# 5. Single Underscore: _

# Per convention, a single standalone underscore is sometimes used as a name to 
# indicate that a variable is temporary or insignificant.

# For example, in the following loop we don’t need access to the running index 
# and we can use “_” to indicate that it is just a temporary value:
# =============================================================================
for _ in range(10):
    print('Hello')
#%%
for _ in range(10):
    print(_)
#%%
a, _, b = 1,2,3
print(f'{a},{_},{b}')
#%%
# =============================================================================
# Besides its use as a temporary variable, “_” is a special variable in most 
# Python REPLs that represents the result of the last expression evaluated by 
# the interpreter.
# =============================================================================
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