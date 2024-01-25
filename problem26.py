"""
Problem 26: Reciprocal Cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5 1/3 = 0.(3) 1/4 = 0.25 1/5 = 0.2 1/6 = 0.1(6) 1/7 = 0.(142857) 1/8 = 0.125 1/9 = 0.(1) 1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


from time import perf_counter as p

start = p()

#biggest reciprocal cycle can be provided by a denominator which is both a safe prime and a reptend prime.
# a prime number p which is both safe and reptend prime gives a cyclic number in length of p-1 digits.

#using sieve of eratosthenes to find all primes below 1000. 
def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False

    d = 2
    while d*d < n:
        if primes[d]:
            for i in range(2*d,n,d):
                primes[i] = False

        d += 1

    return [i for i in range(2,n) if primes[i]]

#checks a number if it is a prime.
def isPrime(x):              
    for i in range(2,x):     
        if x % i == 0:       
            return False
        
    return True



#creating a list of primes below 1000.
limit = 1000
listOfPrimes = sieve(1000)

#safe prime, a prime number p is a Sophie Germain prime if 2p + 1 is also prime.
#The number 2p + 1 is called a safe prime. 
# example 11 is a Sophie Germain prime, 23 is a safe prime.
# a reptend prime p is,a prime that base ten system, can divide the term (10**(p-1) - 1) evenly.



safePrimes = [i for i in listOfPrimes if isPrime((i-1)//2)]
reptendPrimes = [i for i in safePrimes if (10**(i-1) - 1) % i == 0]


#timer irrelevant to the problem, just to measure how many seconds it lasted
stop = p()

print(max(reptendPrimes))
print("Problem solved in", str(round(stop-start,5)) ,"seconds.")