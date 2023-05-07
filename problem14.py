'''Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above one million.
'''

from time import time

s = time()

longestChain = 0
answer = 0
# to prevent to recalculate the steps already calculated, creating an index which contains number and its steps count to 1.
values = {1: 1}

def countChain(n):
    if n in values:
        return values[n]
    if n % 2 == 0:
        # if number is even, we have to divide it by two and continue process with its half,
        # to save one more step we can directly jump to its half and add 1.
        values[n] = 1 + countChain(n/2)
    else: 
        # if number is odd, then 3n + 1 is even, we can save two steps from here by treating the same way we did to even numbers.
        values[n] = 2 + countChain((3*n + 1)/2)

    return values[n]


# if number is even , number becomes number/2 therefore collatz(number) = 1 + collat(number/2), therefore collatz(2k) > collatz(k)
# due to this we can start the loop from maxValue/ 2 which is 1000000/2 = 500000
for i in range(500000,10**6):
    if countChain(i) > longestChain:
        longestChain = countChain(i)
        answer = i



print(answer, time() - s)
