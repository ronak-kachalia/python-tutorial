# =============================================================================
##### Nested Statements and Scope #####
# =============================================================================

# =============================================================================
# LEGB Rule:

# L: Local — Names assigned in any way within a function (def or lambda), 
# and not declared global in that function.

# E: Enclosing function locals — Names in the local scope of any and all 
# enclosing functions (def or lambda), from inner to outer.

# G: Global (module) — Names assigned at the top-level of a module file, or 
# declared global in a def within the file.

# B: Built-in (Python) — Names preassigned in the built-in names module : open, 
# range, SyntaxError,...

# NOTE:
# use the globals() and locals() functions to check what are your current local 
# and global variables.

# global/nonlocal variables
# =============================================================================

x = 'global x'

def test():
    y = 'local y'
    print(y)
    global x
    print(x)
    def t2():
        z = 'local z'
        print(z)
        nonlocal y # refers to the enclosing function i.e test().y
        print(y)
        def t3():
            nonlocal y
            print(y)
        t3()
    t2()
    
test()