"""
The Fibonacci sequence is defined by the recurrence relation:
Fn = F(n-1) + F(n-2), where F1 = 1 and F2 = 2
Hence the first 12 terms will be:
F1 = 1  F4 = 3 F7 = 13 F10 = 55 
F2 = 1  F5 = 5 F8 = 21 F11 = 89
F3 = 2  F6 = 8 F9 = 34 F12 = 144

The 12th term is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from time import perf_counter as p
start = p()

#starting from the first two fibonacci numbers
a,b = 1, 1
#we are counting the index of b, so starting index counter from 2
indexCounter = 2
#this loop will produce fibonacci series and count the index of second fibonacci number 
#when its digit length reaches to 1000 loop will stop
while True:
    a, b = b, a + b
    indexCounter += 1
    if len(str(b)) == 1000:
        break

print(indexCounter)



#timer irrelevant to the problem, just to measure how many seconds it lasted
stop = p()
print("Problem solved in", str(round(stop-start,5)) ,"seconds.")