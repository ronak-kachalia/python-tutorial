'''
##### Lecture 25: OS Module #####
'''
#%%
import os
print(dir(os)) # Prints all the methods available in the OS module
#%%
print(os.getcwd()) # Prints location of current directory
#%%
os.chdir('/Users/ronak/Desktop') # to change the current directory
print(os.getcwd())
#%%
print(os.listdir()) # prints all the files and folders in the current directory
#%%
os.mkdir('new-folder') # for only one level directory creation
#%%
os.makedirs('new-folder/sub-folder/done-folder') # for multiple level of directory creation
#%%
os.rmdir('new-folder') # remove one level of directory
#%%
os.removedirs('new-folder/sub-folder/done-folder') # remove multiple level of directories
#%%
os.rename('new-folder','old-folder') # rename files and folders
#%%
from datetime import datetime
os.stat('old-folder')
mod_time = os.stat('old-folder').st_mtime
print(datetime.fromtimestamp(mod_time))
#%%
# os.walk() # used to get information of all directories and files inside them
# it is a three valued tuple

for (dirpath, dirnames, filenames) in os.walk('/Users/ronak/Desktop'):
    print('Current path', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
#%%
os.environ.get('HOME') # get environment variables
#%%
# os.path # important
os.path.exists('/Users/ronak/Desktop')

# os.path.isdir() to check if its a directory
# os.path.isfilr() to check if its a file
#%%
os.path.splitext('/Users/ronak/Desktop/IdCard.pdf') # to split file name and extension
#%%
print(dir(os.path))
