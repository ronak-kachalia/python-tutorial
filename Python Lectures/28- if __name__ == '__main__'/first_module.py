'''
__name__ is a python reserved variable that stores name of the current module.
if the current module is the one which is run directly by Python then __name__ = '__main__'
else, if it is not run directly by python, then __name__ = '{Name of the Module}'
'''

# print(f'First module\'s name: {__name__}')
print('This is always going to run')

#%%

def main():
    print(f'First module\'s name: {__name__}')

if __name__ == '__main__':
    main()
else:
    print('Run from Import')