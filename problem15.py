'''Problem 15: Lattice paths

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
'''


def factorial(n):
    num = 1
    for i in range(n,1,-1):
        num *= i

    return num

# there are 20 steps for down, 20 steps for right direction. total 40 different steps right and down steps are repetitive so,
# 40!/(20!*20!)


def gridWays(x,y):
    return factorial(x+y)/(factorial(x)*factorial(y))

print(gridWays(20,20))