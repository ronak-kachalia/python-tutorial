#%%
'''
##### Lecture 18: Exception Handling #####
'''
'''
try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 
'''

try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError as e:
    # This will only check for an IOError exception and then execute this print statement
    print(e)
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

#%%
# Finally block will be executed anyway
    
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
finally:
    print("Finally, I executed!")