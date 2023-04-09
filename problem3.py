# Problem 3: Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def prime_factors(n):
    pf = []
    i = 2                          # <- 2 is the smallest and only even prime number.
    while i <= n:                  
        if n % i == 0:             # <- it starts dividing number by two, if remainder is 0, then two is counted as its prime factor.
            pf.append(i)           # and will be added to "pf" prime factors list. then number will be divided by that number, 
            n /= i                 # it will be divided againg by this number until remainder is not 0. this will prevent 
        else:                      # the dividing of our number by numbers which are not prime like 4 and 6.* 
            i += 1                 
    # if remainder is not zero i is incremented. *if a number can be divided by 4 or 6 , also it can be divided by their factors 2 and 3 etc. 

    return pf ,max(pf), n          # <- eventually our number will be shrinked to 1.


print(prime_factors(600851475143))



    





