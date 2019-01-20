# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format

# A single line containing a string S.

# Constraints
# 0<len(S)<=1000


# Output Format

# Print the modified string S.

# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".
# import pdb

A = 'HackerRank.com presents "Pythonist 2".'
def swap_case(s):
    S = list(s)
    for _ in range(len(S)):
        if S[_] == S[_].lower():
            S[_] = S[_].upper()
        elif S[_] == S[_].upper():
            S[_] = S[_].lower()

    return ''.join(S)

print(swap_case(A))

