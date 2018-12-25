#%%
'''
##### Logging to files, Settings Levels and Formatting #####
'''
'''
Logging levels: It allows us to speciy exactly what we want to log by
separating it into categories:
    5 Levels:
        # DEBUG: Detailed information, typically of interest only when 
                    diognising problems
        # INFO: Confirmation that things are working as expected
        # WARNING: An indication that something unexpected happened OR 
                    indication of problem in near future (eg. disk space low)
        # ERROR: Due to some serious problem, the software was not able to 
                    perform some function
        # CRITICAL: A serious error, that the program may not be able to continue
        
    Default level is set to WARNING
'''
#%%
import logging

#%%
# https://docs.python.org/3/library/logging.html - for format

'''
We can use the basicConfig(**kwargs) method to configure the logging

Some of the commonly used parameters for basicConfig() are the following:

level: The root logger will be set to the specified severity level.
filename: This specifies the file.
filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
format: This is the format of the log message.
'''
logging.basicConfig(filename='test.log', level=logging.DEBUG, \
                    format='%(asctime)s:%(levelname)s:%(lineno)d:%(name)s:%(message)s')

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

n1 = 5
n2 = 10

add_result = add(n1,n2)
logging.debug(f'Result: {n1} + {n2} is {add_result}')
sub_result = subtract(n1,n2)
logging.debug(f'Result: {n1} - {n2} is {sub_result}')
div_result = divide(n1,n2)
logging.debug(f'Result: {n1} / {n2} is {div_result}')
mul_result = multiply(n1,n2)
logging.debug(f'Result: {n1} * {n2} is {mul_result}')
#%%

'''
##### Advanced Logging - Logger, FileHandler, Formatter #####
'''
import logging

import my_module_logging



#%%
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('/Users/ronak/Desktop/python-workspace/python-tutorial/Python Lectures/sample_log.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(lineno)d:%(name)s:%(message)s')
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
#%%
stream_handler = logging.StreamHandler() # to log in to the colsole
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
#%%

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

n1 = 5
n2 = 10

add_result = add(n1,n2)
logger.info(f'Result: {n1} + {n2} is {add_result}')
sub_result = subtract(n1,n2)
logger.debug(f'Result: {n1} - {n2} is {sub_result}')
div_result = divide(n1,n2)
logger.debug(f'Result: {n1} / {n2} is {div_result}')
mul_result = multiply(n1,n2)
logger.debug(f'Result: {n1} * {n2} is {mul_result}')

# logger.exception('some text') # gives traceback to the error

