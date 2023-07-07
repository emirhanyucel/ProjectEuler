'''Problem 19: Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

--> 1 Jan 1900 was a Monday.
--> Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
--> A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

months31 = [1,3,5,7,8,10,12]

day = 1
year = 1900
month = 1
date = 1

sundays = 0

while year < 2001:
    if day == 7 and date == 1 and year > 1900:
        sundays += 1
    
    if day == 7:
        day = 1
    else:
        day+=1
    
    if date == 31 and month == 12:
        year += 1
    if month == 2:
        days_in_month = 29 if leap(year) else 28
    else:
        days_in_month = 31 if month in months31 else 30

    if date == days_in_month:
        if month == 12:
            month = 1
        else:
            month +=1 
        date = 1
    else:
        date += 1

print(sundays)