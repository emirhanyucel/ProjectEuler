'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14=53
, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714
.

What is the total of all the name scores in the file?
'''

#This opens the text file
filehandle = open('0022_names.txt')

#This will split words individually by the ' "," ' between them.
for line in filehandle:
    names = line.split('","')

#First name and last name still have ' " ' attached to them we should remove them.
names[0] = names[0].replace('"','')
names[-1] = names[-1].replace('"','')
#This will sort the names alphabetically
names = sorted(names)


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#We are getting a dictionary for letters with their corresponding points, A:1 B:2 and so on...
points = dict()
for i in alphabet:
    points[i] = alphabet.index(i) + 1 

#This function returns sum of the letter points of a name
def namePoint(name):
    sum = 0
    for letter in name:
        sum += points[letter]

    return sum

#This calculates the total points of all names with sum of their letters and their ordinal number.
result = 0
for name in names:
    result += namePoint(name) * (names.index(name) + 1)

print(result)





