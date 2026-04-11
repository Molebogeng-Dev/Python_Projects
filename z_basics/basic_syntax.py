def assign_variables():
    """
    Assigns values to variables and returns their values.

    Returns:
        tuple: A tuple containing the values of variables x, y, z, a, and b.
    """
    # Assign the integer 10 to the variable x.
    x = 10
    # Assign the float 20.5 to the variable y.
    y = 20.5
    # Assign the string 'Hello, World!' to the variable z.
    z = 'Hello, World!'
    # Assign the boolean True to the variable a.
    a = True
    # Assign the boolean False to the variable b.
    b = False
    return x, y, z, a, b # Return the values of x, y, z, a, and b as a tuple.

def get_variable_type(variable):
    """
    Takes a variable as input and returns its data type.

    Args:
        variable: The variable whose data type is to be determined.

    Returns:
        str: A string representing the data type of the input variable.
    """
      # Assign values to x, y, z, a, and b using the assign_variables function.
    variable_type = type(variable).__name__  # Get the data type of the input variable.
    return variable_type # Return the data type as a string.

def get_variable_types():
    """
    Assigns values to variables, gets their data types, and returns the data types.

    Returns:
        tuple: A tuple containing the data types of variables x, y, z, a, and b.
    """
    x, y, z, a, b = assign_variables() # Assign values to x, y, z, a, and b using the assign_variables function.
    type_x = get_variable_type(x)  # Get the data type of x using the get_variable_type function.
    type_y = get_variable_type(y) # Get the data type of y using the get_variable_type function.
    type_z = get_variable_type(z) # Get the data type of z using the get_variable_type function.
    type_a = get_variable_type(a) # Get the data type of a using the get_variable_type function.
    type_b = get_variable_type(b) # Get the data type of b using the get_variable_type function.
    return type_x, type_y, type_z, type_a, type_b # Return the data types as a tuple.

def arithmetic_operations():
    """
    Performs arithmetic operations on variables and returns the results.

    Returns:
        tuple: A tuple containing the results of addition, subtraction, multiplication, division, and modulus operations.
    """
    x, y, z, a, b = assign_variables() # Assign values to x, y, z, a, and b using the assign_variables function.
    sum_result = x + y # Calculate the sum of x and y.
    difference_result = x - y # Calculate the difference between x and y.
    product_result = x * y # Calculate the product of x and y.
    division_result = x / y # Calculate the division of x by y.
    modulus_result = x % y # Calculate the modulus of x and y.
    
    return sum_result, difference_result, product_result, division_result, modulus_result # Return the results as a tuple.

def get_numbers():
    """
    Generates a list of numbers from 0 to 5 and returns the list.

    Returns:
        list: A list containing numbers from 0 to 5.
    """
    numbers = []  # Create an empty list to store numbers.
    for number in range(6):  # Iterate through numbers from 0 to 5.
        numbers.append(number)  # Add each number to the list.
    return numbers  # Return the list of numbers.

if __name__ == "__main":
    x, y, z, a, b = assign_variables()  # Call the assign_variables function and store the values in x, y, z, a, and b.
    print("Variable types:")
    type_x, type_y, type_z, type_a, type_b = get_variable_types()  # Call the get_variable_types function to get data types.
    print(f"'10' belongs to <class '{type_x}'>: meaning it is {type_x}.")
    print(f"'20.5' belongs to <class '{type_y}'>: meaning it is {type_y}.")
    print(f"'Hello, World!' belongs to <class '{type_z}'>: meaning it is {type_z}.")
    print(f"'True' belongs to <class '{type_a}'>: meaning it is {type_a}.")
    print(f"'False' belongs to <class '{type_b}'>: meaning it is {type_b}.")

    print("\nArithmetic operations:")
    sum_result, difference_result, product_result, division_result, modulus_result = arithmetic_operations()  # Call the arithmetic_operations function.
    print(f"The sum of 'x' and 'y' is: {sum_result}")
    print(f"The difference between 'x' and 'y' is: {difference_result}")
    print(f"The product of 'x' and 'y' is: {product_result}")
    print(f"The division of 'x' by 'y' is: {division_result}")
    print(f"The modulus of 'x' and 'y' is: {modulus_result}")

    print("\nNumbers 0 to 5:")
    numbers = get_numbers()  # Call the get_numbers function to get the list of numbers.
    print(numbers)  # Print the list of numbers.
