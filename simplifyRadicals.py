# This scipt should be able to simplify any root n of radicand x
import math

def inputs():
    """Takes in and returns user inputs

    Returns:
        int: index of radical
        float: radicand of radical (number inside)
    """
    while True:
        try:
            index = int(input("Index of the radical: "))
            radicand = float(input("Radicand: "))
            break
        except:
            print("Please enter valid values")
    return index, radicand
        
def root(index, radicand):
    """Simplifies the index root of radicand

    Args:
        index (int): index of the radical
        radicand (float): radicand of the radical to be simplified

    Returns:
        int or float: simplified version of the radical
        string: if 
    """    
      
    # calculates the index root of radicand using a rational exponent
    ans = radicand ** (1/index)
    
    # first check if it is a perfect root
    if ans.is_integer():
        return int(ans)
    
    # now iterate through to simplify
    for i in range(2, math.ceil(radicand)):
        # gets quotient and remainder of radicand divided by i ** index
        div, mod = divmod(radicand, i**index)
        
        if mod == 0:
            n1, n2 = root(index, div)
            return (i * n1, n2)
        if div == 0:
            break
    return (1, radicand)
    
def simplifyRoot():
    """Calls root() with inputs()"""
    index, radicand = inputs()
    
    result = root(index, radicand)
    if isinstance(result, int):
        print(result)
    else:
        print(f"{result[0]} times {index} root of {int(result[1])}")

simplifyRoot()