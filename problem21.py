'''Problem 21: Amicable Numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
amicableNumbers = []

def properDivSum(n):
    pd = 0
    i = 1
    while i <= n/2:
        if n % i == 0:
            pd += i
            i += 1
        else:
            i += 1
    return pd

i = 0
while i < 10000:
    if i == properDivSum(properDivSum(i)) and i != properDivSum(i):
        amicableNumbers.append(i)
        i += 1
    i+= 1

sum = 0
for number in amicableNumbers:
    sum += number

print(sum)


    


