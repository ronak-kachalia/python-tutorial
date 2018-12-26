#%%
'''
##### Lecture 4: Lists and Tuples #####
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
my_list.append('seven')
my_list.pop()
my_list.pop(1) # index
my_list.sort()
my_list.reverse()
my_list.remove()
my_list.remove('two') # value
other_list = my_list.copy() # new copy with different reference
other_list.append('eight') # only other_list changes
print(other_list)
print(my_list)
#%%
# Tuples
'''
Tuples are similar to Lists but immutable
'''
#%%
t = (1,2,3,'four')
t.count('four')
t.index('four')
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
'''
##### List Comprehensions #####
'''
#%%
lst = [x for x in 'word']
lst
#%%
lst = [x**2 for x in range(11)]
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