import math

def inputs():
    """Gets a, b, and c values from input"""

    try:
        a = float(input("Enter 'a' value: "))
        b = float(input("Enter 'b' value: "))
        c = float(input("Enter 'c' value: "))
        
        return (a, b, c)
    
    except:
        print("Please enter valid decimal")
        inputs()
        
def quadraticFormula():
    """runs quadratic formula on inputs from inputs() function"""
    
    vars = inputs()
    a, b, c = vars
    
    # b**2 - 4ac
    discriminator = b**2 - 4 * a * c
    if discriminator < 0:
        return "result 1 is imaginary", "result 2 is imaginary"
    
    # quadratic formula is x = (-b +- sqrt(b^2 - 4ac)) / 2a
    try:
        result1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        result2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    except:
        return "math error", "math error"
    
    return result1, result2

result = quadraticFormula()
resultout = f"{result[0], result[1]}"

print(resultout)