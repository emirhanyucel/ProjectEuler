# Problem 4: Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


palindromes = []
for i in range (100,1000):
    for j in range(100,1000):
        number = i*j  
        # this two for loops will produce every 3 digit number pair multiplication as variable "number".
        stringNumber = str(number)  
        # this turns the number variable to string type so every digit of it will be recognized as letters in a string. 
        if stringNumber == stringNumber[::-1]: #  <-- this line checks if the number string and the reverted version of it is the same.
            palindromes.append(number)
            

print(max(palindromes))
