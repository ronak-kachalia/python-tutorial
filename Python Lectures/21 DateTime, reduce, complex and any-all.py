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

