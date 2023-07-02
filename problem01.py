# Problem 1: Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
i = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
    # this condition block checks if the remainder of number i is divided by 3 or 5 is zero. 
    # if the remainder is zero then it is added to sum and i is incremented by 1. 
        sum += i
        i += 1
    else: 
    # if the remainder is not zero then only i is incremented by 1 to continue to check other numbers until i reaches to 1000.
        i += 1

print(sum)
         
