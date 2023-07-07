'''Problem 20: Factorial Digit Sum
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(n):
    num = 1
    for i in range(n,1,-1):
        num *= i

    return num



factorial100 = str(factorial(100))
sum = 0

for i in range(len(factorial100)):
    sum += int(factorial100[i])

print(sum) 