#%%
'''
##### Lecture 22: Timing your code #####
'''
import timeit

# For loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
