'''
##### Lecture 14: Modules and Packages #####
'''
#%%
import sys
print(sys.path)
sys.path.insert(0, "/Users/ronak/Desktop/python-workspace")
#%%
'''
When we import modules, it gets executed.
Thus, each and every statement will be executed as soon as we import it
'''
import my_module as mm

lst = [1,2,'three',4,True]

mm.printList(lst)
print(mm.test)

#%%
from my_module import printList as pl, test as t

lst = [1,2,'three',4,True]
print(t)
pl(lst)