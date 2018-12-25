#%%
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('/Users/ronak/Desktop/python-workspace/python-tutorial/Python Lectures/employee.log')

logger.addHandler(fileHandler)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(lineno)d:%(name)s:%(message)s')
fileHandler.setFormatter(formatter)

#%%

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
        logger.info(f'Created Employee: {self.first} {self.last}')
    
    @property
    def first_name(self):
        return f'First name: {self.first}'
    @property
    def lasr_name(self):
        return f'First name: {self.last}'
    
x = Employee('Ronak','Kachalia')
y = Employee('Rahul','Gupta')
z = Employee('Yash','Jain')
    
#%%