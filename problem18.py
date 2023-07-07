'''Problem 18: Maximum Path Sum I
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3

Find the maximum total from top to bottom of the triangle below:


''' 

triangle = '''75
95 64
17 47 82
18 35 87 10
20 4 82 47 65
19 1 23 75 3 34
88 2 77 73 7 63 67
99 65 4 28 6 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 4 68 89 53 67 30 73 16 69 87 40 31
4 62 98 27 23 9 70 98 73 93 38 53 60 4 23'''

rows = triangle.split('\n')
list1 = list()
for row in rows:
    numbers = row.split(" ")
    list1.append(numbers)

for i in range(0,len(list1)):
    for j in range(0,i + 1):
        list1[i][j] = int(list1[i][j])

for i in range(len(list1)-1,-1,-1):
    for j in range(0,i):
        list1[i-1][j] += max(list1[i][j],list1[i][j+1])

print(list1[0][0])

