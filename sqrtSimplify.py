import math

radical = int(input("Enter the number inside the radical: "))


def sqrt_simplify(num):
    """simplifies a square root from a given number from inside the radical"""
    
    # first checks if the number is a perfect square and returns the perfect square
    if math.sqrt(num).is_integer(): 
        return int(math.sqrt(num))
    
    for i in range(2, num):
        div, mod = divmod(num, i*i)
        if mod == 0:
            sq1, sq2 = sqrt_simplify(div)
            return (i * sq1, sq2)
        if div == 0:
            break
    return (1, num)
    
result = sqrt_simplify(radical)
if isinstance(result, int):
    print(f"The result is: {result}")
else:
    print(f"The result is: {result[0]} * sqrt({result[1]})")