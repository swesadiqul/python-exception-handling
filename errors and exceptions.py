"""
Errors are the problems in a program due to which the program will stop the execution. 
On the other hand, exceptions are raised when some internal events occur which changes 
the normal flow of the program. 
Two types of Error occurs in python. 
"""

# Syntax errors
# Logical errors (Exceptions) 
 
 

# Syntax errors
"""
When the proper syntax of the language is not followed then a syntax error is thrown.
"""
# Example 
 


# initialize the amount variable
amount = 10000
  
# check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount>2999)
    print("You are eligible to purchase Dsa Self Paced")

"""
It returns a syntax error message because after the if statement a colon: is missing. 
We can fix this by writing the correct syntax."""



# logical errors(Exception)

"""
When in the runtime an error that occurs after passing the syntax test is called exception or logical type.
For example, when we divide any number by zero then the ZeroDivisionError exception is raised, or 
when we import a module that does not exist then ImportError is raised.
"""

# Example 1: 
 


# initialize the amount variable
marks = 10000
  
# perform division with 0
a = marks / 0
print(a)


"""In the above example the ZeroDivisionError as we are trying to divide a number by 0."""

# Example 2: When indentation is not correct. 
 


if(a<3):
print("gfg")
     