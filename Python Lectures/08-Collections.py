#%%
'''
##### Lecture 8: Collections #####

The collections module is a built-in module that implements specialized 
container data types providing alternatives to Python’s general purpose 
built-in containers.
'''
#%%
'''
Counter

Counter is a dict subclass which helps count hashable objects. Inside of it 
elements are stored as dictionary keys and the counts of the objects are 
stored as the value.
'''

from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(lst))

print(Counter('aabsbsbsbhshhbbsbs'))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print(Counter(words))
#%%
'''
Methods with Counter()

Common patterns when using the Counter() object

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''
s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

c = Counter(words)

c.most_common(2)
#%%
'''
defaultdict

defaultdict is a dictionary-like object which provides all methods provided 
by a dictionary but takes a first argument (default_factory) as a default data 
type for the dictionary. Using defaultdict is faster than doing the same using 
dict.set_default method.
'''

from collections import defaultdict

# Normal
d = {}
# d['one'] # KeyError: 'one'

# defaultdict
d  = defaultdict(object)
print(d['one'])
print(d['four'])

for item in d:
    print(item)

'''
Can also initialize with default values:
'''
d = defaultdict(lambda: 0)
print(d['one'])
#%%
'''
OrderedDict

An OrderedDict is a dictionary subclass that remembers the order in which its 
contents are added.
'''

print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)


from collections import OrderedDict

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
#%%
'''
Equality with an Ordered Dictionary

A regular dict looks at its contents when testing for equality. An 
OrderedDict also considers the order the items were added.
'''

print('Dictionaries are equal?')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)

from collections import OrderedDict

print('Dictionaries are equal?')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)
#%%
'''
namedtuple

The arguments are the name of the new class and a string containing the names 
of the elements.
'''
from collections import namedtuple

D = namedtuple('Dog','age breed name')

sam = D(age=2,breed='Lab',name='Sammy')

frank = D(age=2,breed='Shepard',name="Frankie")

print(sam)
print(frank)
print(sam.breed)
print(sam[1])
print(dir(sam))