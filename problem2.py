# Problem 2: Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def fibonacci_even(max):
    x, y = 1, 2               # <- fibonacci sequence stars with 1 and 2 
    sum = 0                   # <- sum is set to zero initially 
    while y <= max:           # <- this will check if the second number is below our max value
        if y % 2 == 0:        # <- every even valued number is divided by two evenly. so if the remainder is zero when number is
            sum += y          # divided by two we will add it to the sum.
        x, y = y, x + y       # <- as it is the definition of the fibonacci series we will change our two numbers by making the 
    print(sum)                # second number as the sum of previous two number. 

fibonacci_even(4000000)
