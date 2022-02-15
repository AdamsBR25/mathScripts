import math

# gathers inputs
while True:
    try:
        x1 = float(input("x1: "))
        x2 = float(input("x2: "))
        y1 = float(input("y1: "))
        y2 = float(input("y2: "))
        break
    except:
        print("Enter actual number please")

# uses distance formula to find the distance between the two points
x = x2 - x1
y = y2 - y1
xSquare = x ** 2
ySquare = y ** 2
preSqrt = xSquare + ySquare
distance = math.sqrt(preSqrt)

print(distance)