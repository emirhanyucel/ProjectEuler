# Problem 5: Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def checkDivisible1to20(num):  # <- this function tests if our number is evenly divisible by numbers ranging from 11 to 20.
    for i in range (11,21):    # numbers from 1 to 10 is excluded because they are already found as factors in numbers from 11 to 20.
        if num % i != 0:       # for example if a number is divisible by 15 it is also divisible by 3 and 5. 
            return False
    
    return True

num = 20                       # <- our desired number must be a multiple of 20 so we initiate from 20.
while True:
    if checkDivisible1to20(num):
        break
    num += 20                  # <- and because of that we increment by 20 if our number is not divisible by numbers from 11 to 20.

print(num)