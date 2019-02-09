# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format

# The first line contains T, the number of testcases. 
# Each testcase contains 2 lines, representing time t1 and time t2.

# Constraints

# Input contains only valid timestamps
# .year <=3000
# Output Format

# Print the absolute difference (t1-t2) in seconds.

# Sample Input 0

# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0

# 25200
# 88200
# Explanation 0

# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7*3600 seconds or 25200 seconds.

# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24*3600+30*60=>88200 

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
# t1 = 'Sat 02 May 2015 19:54:36 +0530'
# t2 = 'Fri 01 May 2015 13:54:36 -0000'

# t1d = dt.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
# t2d = dt.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

def time_delta(t1, t2):
    t1d = dt.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2d = dt.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    delta = t1d-t2d
    return str(int(abs(delta.total_seconds())))




if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = os.path.join(os.getcwd(), 'output.txt')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    inputFile = open('input01.txt', 'r')

    # t = int(input())
    t = int(inputFile.readline())

    for t_itr in range(t):
        t1 = inputFile.readline().replace('\n','')
        t2 = inputFile.readline().replace('\n','')

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    inputFile.close()