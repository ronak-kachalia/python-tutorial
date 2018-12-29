# =============================================================================
##### Strings and String Formatting #####
# =============================================================================


# =============================================================================
# NOTE: When applying methods to strings, always store it into other variables 
# since Strings are immutable and thus effects will not be shown
# example, 
# s = 'Ronak Kachalia'
# s.capitalize() # Incorrect
# s = s.capitalize() # Correct
# =============================================================================
#%%
# We can also use a function called len() to check the length of a string!
my_name = 'Ronak Kachalia'
len(my_name)
# String Indexing
print(my_name[4])
#%%
# =============================================================================
# Slicing:

# [start index : end index : step]
# Negative numbers denote reverse indexing
# [:] blank index indicates ALL elements
# =============================================================================
#%%
print(my_name[1:])
print(my_name[::-1])
print(my_name[1:4:2])
print(my_name[::])
#%%
# =============================================================================
# STRINGS ARE IMMUTABLE
# But se can reassign string completely though!
# =============================================================================
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
# =============================================================================
# Formatting
# =============================================================================
s = 'Ronak'
s.center(20,'-')
#%%
# =============================================================================
# is check methods
# =============================================================================
s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.isspace())
print(s.islower())
print(s.isupper())
print(s.endswith('o'))