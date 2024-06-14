# Python docstrings are the string literals that appear right after the definition of a 
# function, method, class, or module.

# SYNTAX: 
# def myfunc():
#     <Docstring>
#     <function body>

def  square(n):
    '''Takes in a numbern,returns the
    square of n'''
    print(n**2)

square(5)
print(square.__doc__)

# **IMP:Docstring are not ignore by python interpreter.

# Python Comments v/s Docstring
# Comments are description that helps the programmers to better 
# understand the intent of the program.They are completely ingnored by the python interpreter.
#
# Python docstring are strings used after the definition od a function ,method,class or midule .
# They are use to document our code.
# -------------------------------------------------------------------------------------------------------------------------------


#                            PEP 8 
# Python Enhancement Proposal 
# The Zen of Python