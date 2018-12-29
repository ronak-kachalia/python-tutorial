# =============================================================================
##### Dictionary and Sets #####
# =============================================================================

# =============================================================================
# A Python dictionary consists of a key and then an associated value. 
# That value can be almost any Python object.

# NOTE: For keys, we can use Strings, numbers, tuplesn Booleans and None.
# Dictionaries allow duplicate keys but withh show warning. Also, it will print 
# the value of the duplicate key of last entered value for that key
# LISTS CANNOT BE USED AS KEYS
# =============================================================================
#%%
# keys can be either String or Number
my_dict = {'key':'value', 'list':[1,'two',['three',4]], 1: 'Correct', 0.7: 'false'}
# Nesting with Dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])
#%%
# =============================================================================
# Dictionary methods:
# =============================================================================
d.keys()
d.get('key')
d.items() # All key-value pairs
d.values() # All values
#%%
# =============================================================================
# Sets:

# Sets contain only unique keys
# Duplicates are treated as one
# set(iterable): takes only one argument - iterable
# =============================================================================
#%%
lst = [1,2,3,4,4]
s = set(lst)

x = set()
x.add(1)
x.add('friends')
#%%
# =============================================================================
# Advanced Sets:
# =============================================================================

# =============================================================================
# copy:

# returns a copy of the set. Note it is a copy, so changes to the original 
# don't effect the copy.
# =============================================================================
s = set()
s.add(1)
s.add(2)
s.add(3)
sc = s.copy()
s.add(4)
print(s)
print(sc)
#%%
# =============================================================================
# difference:

# difference returns the difference of two or more sets. The syntax is:
# =============================================================================
print(s.difference(sc))
#%%
# =============================================================================
# difference_update:

# difference_update syntax is:
# set1.difference_update(set2)
# the method returns set1 after removing elements found in set2
# =============================================================================
s1 = {1,2,3}
s2 = {1,4,5}
print(s1.difference_update(s2))
print(s1)
#%%
# =============================================================================
# intersection and intersection_update:

# Returns the intersection of two or more sets as a new set.(i.e. elements that 
# are common to all of the sets.)
# =============================================================================
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
print(s1)

# =============================================================================
# intersection_update will update a set with the intersection of itself and 
# another.
# =============================================================================
print(s1.intersection_update(s2))
print(s1)
#%%
# =============================================================================
# union:

# Returns the union of two sets (i.e. all elements that are in either set.)
# =============================================================================
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.union(s2))
print(s1)
#%%
# =============================================================================
# discard:

# Removes an element from a set if it is a member. If the element is not a 
# member, do nothing.
# =============================================================================
s1 = {1,2,3}
s2 = {1,2,4}
s1.discard(2)
print(s1)
#%%
# =============================================================================
# update:

# Update a set with the union of itself and others
# =============================================================================

s1.update(s2)
print(s1)
#%%
# =============================================================================
# Also,
#     isdisjoint
#     issubset
#     issuperset
# =============================================================================