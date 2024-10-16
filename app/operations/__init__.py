import math
from typing import Union

# Define a type alias for numbers (both int and float)

Number = Union[int, float]

# addition function 
def addition(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns their sum.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    
    This function adheres to the Single Responsibility Principle (SRP) as it performs only one task: addition.
    
    Example:
    >>> addition(3, 4)
    7
    """
    return a + b  # Return the sum of a and b

# subtraction function
def subtraction(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns the result of subtracting b from a.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    
    This function also adheres to SRP by focusing on the single task of subtraction.
    
    Example:
    >>> subtraction(10, 4)
    6
    """
    return a - b  # Return the result of a minus b

def multiplication(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns their product.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    
    Like the other functions, this follows SRP by handling only multiplication.
    
    Example:
    >>> multiplication(2, 5)
    10
    """
    return a * b  # Return the product of a and b

def division(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns the result of dividing a by b.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    
    It is important to handle division by zero here to avoid runtime errors.
    A common way to handle this would be by catching ZeroDivisionError when used in a broader context.
    
    Example:
    >>> division(10, 2)
    5.0
    
    Potential Error:
    If b is 0, a ZeroDivisionError will occur. This could be handled using EAFP (Easier to Ask Forgiveness than Permission)
    where you try the operation and handle the exception if it occurs.
    """
    return a / b  # Return the result of a divided by b
def modulus(a: float, b: float) -> float:
    """
    This function takes two numbers (a and b) and returns the remainder (a % b).
    """
    return a % b

def power(a: float, b: float) -> float:
    """
    This function takes two numbers (a and b) and returns the result of a raised to the power of b (a ** b).
    """
    if a == 0 and b < 0:
        raise ValueError("Zero can not be rasied by negative power")
    return a ** b

def logarithm(a: float, b: float = math.e) -> float:
    """
    This function takes a number (a) and a base for the logarithm calculation.
    If ther is no base typed, the natural logarithm (base e) is used.
    Raises a ValueError if (a) is less than or equal to zero. 
    """
    if a <= 0:
        raise ValueError("Logarithm input must greater than or equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm input must greater than or equal to 1.")
    if b == 10:
        return math.log10(a)
    else:
        return math.log(a, b)
