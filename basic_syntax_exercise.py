# Python Basic Syntax

# 1. Variables: You can store values in variables.

# On the next line store the number '10' in the variable 'x'.
x= 10

# On the next line, store the number '20.5' in the variable 'y'.
y= 20.5

# On the next line, store the string 'Hello, World!' in the variable 'z'.
z= 'Hello, World!'

# On the next line, store the boolean 'True' in the variable 'a'.
a= True

# On the next line, store the boolean 'False' in the variable 'b'.
b= False

# Use the print statement and the variable 'x' to display the message:
    # "10, is an integer variable."
print(f'{x}, is an integer variable.')
# Use the print statement and the variable 'y' to display the message: 
    # "20.5, is a float variable."
print(f'{y}, is a float variable.')
# Use the print statement and the variable 'z' to display the message: 
    # " 'Hello, World!' is a string variable."
print(f'{z}, is a string variable.')
# Use the print statement and the variable 'a' to display the message:
    # " 'True', is a boolean variable."
print(f'{a}, is a boolean variable.')
# Use the print statement and the variable 'b' to display the message:
    # " 'False', is a boolean variable.
print(f'{b}, is a boolean variable.')


# 2. Data Types: Python has several built-in data types.
    # Use the `type()` function to identify the data types of your variables.
    # Usage example: 
        # h = 13
        # print(type(h)) will display <class 'int'>

# Edit the code below to print:
    # "10 belongs to <class 'int'>: meaning it is an integer."
print(f'{x} belongs to {type(x)}: meaning it is an integer.')


# Edit the code below to print:
    # " 20.5 belongs to <class 'float'>: meaning it is a float."
print(f'{y} belongs to {type(y)}: meaning it is a float.')


# Edit the code below to print:
    # " 'Hello, World!', belongs to <class 'str'>: meaning it is a string."
print(f'{z} belongs to {type(z)}: meaning it is a string.')


# Edit the code below to print:
    # "'True', belongs to <class 'bool'>: meaning it is a boolean."
print(f'{a} belongs to {type(a)}: meaning it is a boolean.')


# Edit the code below to print:
    # "'False', belongs to <class 'bool'>: meaning it is a boolean.
print(f'{b} belongs to {type(b)}: meaning it is a boolean.')


# 3. Basic Operators: 
    # Python supports various operators for performing operations on data.
# Arithmetic Operators

# Addition: print the sum of 'x' and 'y'.
print(x+y)


# Subtraction: print the difference between 'x' and 'y'.



# Multiplication: print the product of 'x' and 'y'.
print(x*y)

# Division: print the answer when you divide 'x' by 'y'.
print(x/y)

# Modulus (remainder of the division): print the remainder after dividing 'x' by 'y'.
print(x%y)



# 4. Indentation: 
    # Python uses indentation to indicate the beginning and end of code blocks.
# Complete the for loop below to print numbers 0 to 5    

for number in range(6):
    print(number)  # This line is part of the for loop and it must be indented.
