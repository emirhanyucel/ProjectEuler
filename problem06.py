# Problem 6: Sum square difference

# The sum of the squares of the first ten natural numbers is, 385

# The square of the sum of the first ten natural numbers is, 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquare(n):
    sum1 = 0
    i = 1
    while i <= n:
        sum1 += i * i       # <- this function gives the sum of squares of numbers from 1 to n.
        i += 1
    return sum1

def squareOfSum(n):
    sum2 = 0
    i = 1
    while i <= n:
        sum2 += i           # <- this function gives the square of the sum of numbers from 1 to n.
        i += 1
    
    sum3 = sum2 * sum2
    return sum3 

def difference(n):
    return  squareOfSum(n) - sumOfSquare(n)  # <- this function gives the difference between two functions.


print(sumOfSquare(10))
print(squareOfSum(10))
print(difference(10))

print(sumOfSquare(100))
print(squareOfSum(100))
print(difference(100))


