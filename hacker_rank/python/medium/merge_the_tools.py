# Consider the following:

# A string, s, of length n where s=c_0c_1...c_n-1.
# An integer, k, where k is a factor of n.
# We can split s into n/k subsegments where each subsegment, t_i, consists of a contiguous block of k characters in s. Then, use each t_i to create string u_i such that:

# The characters in u_i are a subsequence of the characters in t_i.
# Any repeat occurrence of a character is removed from the string such that each character in u_i occurs exactly once. In other words, if the character at some index j in t_i occurs at a previous index <j in t_i, then do not include the character in string u_i.
# Given s and k, print n/k lines where each line i denotes string u_i.

# Input Format

# The first line contains a single string denoting s. 
# The second line contains an integer, k, denoting the length of each subsegment.

# Constraints

# 1<=n<=10^4, where n is the length of s
# 1<=k<=n
# It is guaranteed that n is a multiple of k.
# Output Format

# Print n/k lines where each line i contains string u_i.

# Sample Input

# AABCAAADA
# 3   
# Sample Output

# AB
# CA
# AD
# Explanation

# String s is split into n/k = 9/3 = 3 equal parts of length k=3. We convert each t_i to u_i by removing any subsequent occurrences non-distinct characters in t_i:
# 1. t_0 = "AAB" --> u_0 = "AB"
# 2. t_1 = "CAA" --> u_1 = "CA"
# 3. t_2 = "ADA" --> u_2 = "AD"
# We then print each u_i on a new line.

from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here

    n = len(string)
    U = [string[i*k:k*(i+1)] for i in range(int(n/k))]
    u = [''.join(OrderedDict.fromkeys(s).keys()) for s in U]

    for i in u: print(i)
    # return u


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

