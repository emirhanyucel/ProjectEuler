'''Problem 17: Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

def letterCount(n):

    numberWordsCounts = {
        0: 0,
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6,
        100: 7,
        1000: 8
    }

    if n <= 20:
        return numberWordsCounts[n]
    elif n < 100:
        tens = (n // 10) * 10
        ones = n % 10
        return numberWordsCounts[tens] + numberWordsCounts[ones]
    
    elif n < 1000:
        hundreds = n // 100
        tens = n % 100
        if tens == 0:
            return numberWordsCounts[hundreds] + numberWordsCounts[100]
        else: 
            return numberWordsCounts[hundreds] + numberWordsCounts[100] + len("and") + letterCount(tens)
    
    elif n == 1000:
        return numberWordsCounts[1] + numberWordsCounts[1000]
    
totalLetterCount = 0
for i in range (1,1001):
    totalLetterCount += letterCount(i)

print(totalLetterCount)