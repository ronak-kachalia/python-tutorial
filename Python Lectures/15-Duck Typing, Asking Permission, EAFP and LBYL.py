# =============================================================================
##### Duck Typing, Asking for Forgiveness, EAFP and LBYL #####
# =============================================================================

# =============================================================================
# Duck typing 
# =============================================================================

# GENERALLY
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')
        
def quack_and_fly(thing):
    if(isinstance(thing,duck)):
        thing.quack()
        thing.fly()
    if(isinstance(thing,person)):
        thing.quack()
        thing.fly()
        
d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p)

# DUCK TYPING
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')
        
def quack_and_fly(thing):
    thing.quack()
    thing.fly()

d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p)
#%%
# =============================================================================
# Asking Permission
# LBYL
# =============================================================================
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

def quack_and_fly(thing):
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing,'fly'):
        if callable(thing.fly):
            thing.fly()

d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p)  
#%%
# =============================================================================
# Not Permission

# EAFP: Easier to Ask Forgiveness than Permission

# LBYL: Look Befor You Leap
# =============================================================================

# EAFP
class duck:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')

class person:
    def quack(self):
        print('I quacked!')
    def fly(self):
        print('I can fly!')
       
    def quack_and_fly(thing):
        try:
            thing.quack()
            thing.fly()
        except AttributeError as e:
            print(e)
        
d = duck()
p = person()

quack_and_fly(d)
quack_and_fly(p) 
#%%
# =============================================================================
# LBYL vs EAFP
# =============================================================================
my_dict = {'name':'ronak','age':22}

#LBYL
if 'name' in my_dict and 'age' in my_dict:
    print(f'{my_dict["name"]} - {my_dict["age"]}')
else:
    print('Some keys are missing')
    
#EAFP
try:
    print(f'{my_dict["name"]} - {my_dict["age"]}')
except KeyError as e:
    print(e)
