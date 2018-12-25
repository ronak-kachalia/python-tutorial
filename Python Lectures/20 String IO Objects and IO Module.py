#%%
'''
##### Lecture 20: StringIO Objects and the io Module #####

Text data is stored in a StringIO object, while binary data would be stored in 
a BytesIO object. This object can then be used as input or output to most 
functions that would expect a standard file object.
'''
import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

f.read()

f.write(' Second line written to file like object')

# Reset cursor just like you would a file
f.seek(0)

# Read again
f.read()

f.close()