"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from time import perf_counter as p
from itertools import permutations 

start = p()

digits = '0123456789'
#using permutations from itertools will give us ordered list of permutations of given digits easily.
lexicographical = list(permutations(digits))

#we will express them as a number by adding them as a string 
result = ''.join(lexicographical[999999])

print(result)

#timer irrelevant to the problem, just to measure how many seconds it lasted
stop = p()
print("Problem solved in", str(round(stop-start,5)) ,"seconds.")