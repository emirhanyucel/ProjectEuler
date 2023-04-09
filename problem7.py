# Problem 7: 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def isPrime(x):              # <- a prime number has only two factors: 1 and itself.
    for i in range(2,x):     # in this function it tests if the numbers is divisible by any number between 1 and itself.
        if x % i == 0:       # if it is, then it is not a prime number.
            return False
        
    return True

def nth_prime(nth):            
    num = 3                    # <- second prime number is three, so if the second prime number is asked from function it gives 3.
    primeOrder = 2           
    if nth == 1:               # <- first prime numer is 2. so when function is asked for first prime it gives 2.         
        return 2             
    while primeOrder< nth:          
        num += 2               # <- except for 2, every prime number is odd so function keeps incrementing num by 2. (3,5,7,...)
        if isPrime(num):       # but 9 is not a prime number so this where our helper function isPrime will get involved. so it will keep incrementing num
            primeOrder += 1    # by 2 until primeOrder is reached to desired nth parameter.
    return num

ans = nth_prime(10001)
print(ans)
print(f"Is the number {ans} a prime number? : {isPrime(ans)}")


