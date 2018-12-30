#!/bin/python3
# Task 
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer, n.

# Constraints
# 1<=n<=100

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.

# Sample Input 0

# n=3
# Sample Output 0

# Weird
# Explanation 0

 
# n is odd and odd numbers are weird, so we print Weird.

# Sample Input 1

# n=24
# Sample Output 1

# Not Weird
# Explanation 1

 
# n=24, n>20 and n is even, so it isn't weird. Thus, we print Not Weird.




N = int(input())

if N % 2 != 0:
    print('Weird')
elif N % 2 == 0 and N in range(2,6):
    print('Not Weird')
elif N % 2 == 0 and N in range(6,21):
    print('Weird')
elif N % 2 == 0 and N > 20:
    print('Not Weird')


