# =============================================================================
# ##### Numbers and Variables #####
# =============================================================================

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

# =============================================================================
# Exponentials:
# The function pow() takes two arguments, equivalent to x^y. With three 
# arguments it is equivalent to (x^y)%z, but may be more efficient for 
# long integers.
# =============================================================================
print(pow(3,4))
print(pow(3,4,5))
#%%
# =============================================================================
# Variables:

# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter 
# oh), or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"
# =============================================================================

# =============================================================================
# Dynamic Typing:

# Python uses dynamic typing, meaning you can reassign variables to different 
# data types. this makes Python very flexible in assigning data types; it 
# differs from other languages that are statically typed.
# =============================================================================
#%%
my_var = 2
print(my_var)

my_var = ['dogs','cats']
print(my_var)
#%%

# =============================================================================
# Pros and Cons of Dynamic Typing:

# Pros of Dynamic Typing
# 1. very easy to work with
# 2. faster development time
# Cons of Dynamic Typing
# 1. may result in unexpected bugs!
# 2. you need to be aware of type()
# =============================================================================

# =============================================================================
# Determining variable type with type():

# You can check what type of object is assigned to a variable using Python's 
# built-in type() function. Common data types include:
# int (for integer)
# float
# str (for string)
# list
# tuple
# dict (for dictionary)
# set
# bool (for Boolean True/False)
# =============================================================================