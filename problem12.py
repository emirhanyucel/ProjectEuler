'''
Problem 12: Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import math
#  generates the nth triangular number
def generator(n):
    num = n * (n + 1) * 0.5
    return num
# gets factor number of a number, starting from two to its square root.
# for example 28 as a triangular number, its square root is between 5 and 6
# it has 3 (1,2,4) divisors until its square root, starting from itself it has also another three divisor 28 14 and 7
# that's why we search its divisors until its square root then we multiply it by two with this function.
def factorFind(n):
    factorNumber = 1
    for i in range (2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            factorNumber += 1
    return factorNumber * 2
    

# this function searches through triangular numbers until its factor number exceeds 500
def factor500Finder():
    
    n = 1
    while True:
        if (factorFind(generator(n))) <= 500:
            n += 1
        else:
            print(n)
            return int(generator(n))
        
print(factor500Finder())


        










