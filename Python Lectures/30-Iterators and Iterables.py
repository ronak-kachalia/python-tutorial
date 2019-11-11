#=============================================================================
##### Iterators and Iterables #####
#=============================================================================

#=============================================================================
# Iterables:

# Something that can be looped over
# Example: A List is a literable since it can be looped
#=============================================================================
#%%
nums = [1,2,3,4]
for i in nums:
    print(i)
#%%
#=============================================================================
# How to check if an object is iterable or not?
# __iter__() method defines iterables
# use dir() to check whether it comtaine __iter__ method
# __iter__() has a state that knows where it is during iteration and they now
# which is the next value to be called with the help of __next__
# since List doesn't have __next__ method, it is not iterator
# next(nums) - next method uses __next__ for iteration
#=============================================================================
#%%
print(dir(nums))
#%%
i_nums = nums.__iter__()
i_nums = iter(nums) # same as above

print(i_nums)
print(dir(i_nums))
# NOTE: __iter__ also has __iter__ in it but it returns 'self'
#%%
# now i_nums has __next__ method. Let's use that and check whether we 
# get next value
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums)) # Error. since it doesn't have more values
#%%
while True:
    try:
        print(next(i_nums))
    except StopIteration:
        break
# NOTE: iterators can only go forward, they cannot go backward

#=============================================================================
# Creating your own iterators
#=============================================================================
#%%
class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)

#%%
for num in nums:
    print(num)

#%%
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

#%%
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
a = PowTwo(4)
i = iter(a)
#%%
next(i)
#%%
#=============================================================================
# Iterators with Generators
#=============================================================================
def my_range(start,end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1,10)

for i in nums:
    print(i)
    print('Yield')
#%%
# Infinite Iterator
# The built-in function iter() can be called with two arguments where the first 
# argument must be a callable object (function) and second is the sentinel. 
# The iterator calls this function until the returned value is equal to the 
# sentinel.
int()
float()
bool()
list()
dict()
inf = iter(int,1)
next(inf)
