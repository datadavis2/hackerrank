'''
Consider a staircase of size n = 4:

   #
  ##
 ###
####

Write a program that prints a staircase of size n.

https://www.hackerrank.com/challenges/staircase/problem

'''

def staircase(n):
    for c, value in enumerate(range(n), 1):
        print(' ' * (n-c) + '#' * c)
        
# alternative, without the enumeration
'''
def staircase(n):
    for c in range(n):
        c = c + 1
        print(' ' * (n-c) + '#' * c)
'''
