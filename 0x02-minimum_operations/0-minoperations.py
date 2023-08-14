#!/usr/bin/python3
'''
In a text file, there is a single character H.

Your text editor can execute only two operations in this file: Copy All and Paste. 
Given a number n, write a method that calculates the fewest number of operations 
needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    ''' returns min operations to get n Hs '''

    operations = 0
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        ''' check if n could be broken into smaller part '''
        while n % i == 0:
            ''' reduce n into a smaller part '''
            n = n / i
            ''' if so add the nbr of smaller parts '''
            operations += i
    return operations
