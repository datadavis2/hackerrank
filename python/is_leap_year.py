'''
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task 
You are given the year, and you have to write a function to check if the year is leap or not.

https://www.hackerrank.com/challenges/write-a-function/problemhttps://www.hackerrank.com/challenges/write-a-function/problem

'''

def is_leap(year):
    
    all_years = range(10**5)
    leap_years = [x for x in all_years if (x % 100 != 0 and x % 4 == 0) or (x % 100 == 0 and x % 400 == 0)]
    
    leap = year in leap_years
    return leap
    
year = int(input())
print(is_leap(year))
