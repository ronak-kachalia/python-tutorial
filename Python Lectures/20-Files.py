#%%
'''
##### Lecture 19: Files #####
'''
my_file = open('test.txt','w+')
#%%
'''
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

Opening a file with 'w' or 'w+' truncates the original, meaning that anything 
that was in the original file is deleted!
'''
my_file.write('Hello. This is my first line.')
#%%
# Seek to the start of file (index 0)
my_file.seek(0)
my_file.read()
#%%
my_file.write('\nSo how was your day?')
#%%
my_file.seek(0)
my_file.readlines()
#%%
my_file.close()
#%%
'''
Appending
'''
my_file = open('test.txt','a+')
#%%
my_file.write('\nHello World')
#%%
my_file.seek(0)
my_file.read()
my_file.seek(0)
my_file.readlines()
#%%
my_file.seek(0)
my_file.write('Have I become the first line?\n')
#%%
my_file.seek(0)
my_file.readlines()
#%%
'''
Printing single lines at a time
'''
# Pertaining to the first point above
for asdf in open('test.txt'):
    print(asdf)