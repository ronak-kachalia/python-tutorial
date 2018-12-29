# =============================================================================
##### Useful Operators #####
# =============================================================================

# =============================================================================
# Range:

# The range function allows you to quickly generate a list of integers, this 
# comes in handy a lot, so take note of how to use it! There are 3 parameters 
# you can pass, a start, a stop, and a step size.
# =============================================================================
#%%
print(range(0,10,2))
print(list(range(0,10,2)))
#%%
# =============================================================================
# Enumerate:

# enumerate is a very useful function to use with FOR loops.
# =============================================================================
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
# =============================================================================
# Zip:
# =============================================================================
mylist1=[1,2,3]
mylist2=[4,5,6]
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
#%%
# =============================================================================
# in operator:
# =============================================================================
'x' in ['x','y','z']
'x' in [1,2,3]
#%%
# =============================================================================
# min and max:
# =============================================================================
mylist = [10,20,30,40,100]
min(mylist)
max(mylist)
#%%
# =============================================================================
# Random:
# =============================================================================
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)

from random import randint
# Return random integer in range [a, b], including both end points.
randint(0,100)
#%%
# =============================================================================
# Input:
# =============================================================================
x = input('Enter')
print(x)
