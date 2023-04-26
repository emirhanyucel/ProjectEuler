'''Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''


def sumOfAllPrimes(maxVal):
    result = 0

    # Setting a boolean array which is made of True vales from 1 to maximum Value.
    primes = [True for i in range (maxVal+1)]
    
    p = 2
    # looking at the numbers which was set to True from 1 to square root of maxVal.
    while (p * p <= maxVal):
        
        # If primes[p] is not changed to False then it is a prime number.
        
        if (primes[p] == True):

            # Changing all multiples of p to False since they are not prime.
            for i in range (p * p, maxVal+1,p):
                primes[i] = False
        
        p += 1

    for p in range(2,maxVal + 1):
        if primes[p]:
            result += p

    return result

print(sumOfAllPrimes(10))
print(sumOfAllPrimes(2000000))
            









