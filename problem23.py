"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, 
the sum of the proper divisors of 28 would be 1+2+4+7+14=28 which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n nd it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6=16,the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from time import perf_counter as p
import math
start = p()

#getting proper divisor sum
def divisorSum(num):
    sum = 1
    d = 2
    while d <= math.sqrt(num):
        if num % d == 0:
            sum += d
            if d != num // d:
                sum += num // d
        d += 1
    return sum

#checking if a number is abundant
def isAbundant(num):
    return divisorSum(num) > num
     
#creating an abundant numbers list
abundants = list()
for i in range(1,28124):
    if isAbundant(i):
        abundants.append(i)

#creating a list that contains 28124 0s, then we will replace zeros with abundant number sums that less than 28123
sumOfAbundants = [0]*28124

for i in range(len(abundants)):
    for j in range(i,len(abundants)):
        if abundants[i] + abundants[j] <= 28123:
            if sumOfAbundants[abundants[i] + abundants[j]] == 0:
                sumOfAbundants[abundants[i] + abundants[j]] = abundants[i] + abundants[j]

#if a number can not be represented by a sum of two abundant number its index will stay zero,
#therefore we should add the indices of 0s
result = 0
for i in range(len(sumOfAbundants)):
    if sumOfAbundants[i] == 0:
        result += i

print(result)

#timer irrelevant to the problem, just to measure how many seconds it lasted
stop = p()
print("Problem solved in", str(round(stop-start,5)) ,"seconds.")







