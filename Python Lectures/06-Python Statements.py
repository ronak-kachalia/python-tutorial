#%%
'''
##### Lecture 6: Python Statements #####
'''
#%%
# if elif and else
x = 2
if x == 3:
    print('It\'s three')
elif x == 4:
    print('It\'s four')
else:
    print('oops')
#%%
# Ternary Operator
# [true] if confition else [false]
a,b,c=2,3,4
print('a is greater than be' if a >b else 'b is greater than a')
print('a is greater than be' if a >b else 'b is greater than a and c' if b > c else 'c is the greatest')
#%%   
# LOOPS
# FOR LOOP
my_list = [1,2,'three',['four',5]]
for items in my_list:
    print(items) 
#%%
my_dict = {'key':'value','key 2':'value'}
for k,v in my_dict.items():
    print(k)
    print(v)  
#%%
list2 = [(2,4),(6,8),(10,12)]
for (t1,t2) in list2:
    print(t2)
#%%   
for i in range(len(my_list)):
    print(i)
#%%
for i,j in zip(my_dict,my_list):
    print(i)
    print(j)
#%%   
# WHILE LOOP   
x = 10

while x > 0:
    print(x)
    x-=1
else:
    print('done')