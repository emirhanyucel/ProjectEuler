'''Problem 9: Special Pythagorean triplet'''
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

n = 1000
p = None
# in a triangle c < a + b, thus upper limit is n//2, and c is bigger than
# a and b, c>b>a, lower limit for the range is n//3.
for c in range(n//3 , n//2):
    # c > b so upper limit for b is c itself. 
    # and the lower limit is at least half of the 1000 - c, since b > a.
    
    for b in range((n - c)//2, c):
        a = n - c - b
        if (c**2) == (a**2) + (b**2):
            p = a * b * c
            break
    if p:
        break

print(p)
print(a,b,c)
