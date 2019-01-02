# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

# For example:

# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.

# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

# Note:
# If you are given an array with multiple answers, return the lowest correct index.
# An empty array should be treated like a 0 in this problem.
import pdb

def find_even_index(arr):
    #your code here

    def get_l_and_r_sums(arr, index):
        l_sum, r_sum = 0,0
        if index == 0:
            l_sum = 0
            r_sum = sum([i for i in arr[index+1:]])
        elif index == len(arr) - 1:
            l_sum = sum([i for i in arr[0:index]])
            r_sum = 0
        else:
            l_sum = sum([i for i in arr[0:index]])
            r_sum = sum([i for i in arr[index+1:]])

        return (l_sum, r_sum)

    # Either way...
    # sum_pairs = [get_l_and_r_sums(arr, i) for i in range(len(arr))]
    sum_pairs = [get_l_and_r_sums(arr, i[0]) for i in enumerate(arr)] # Memorize enumerate()

    # First way
    # print([i for i in range(len(sum_pairs)) if sum_pairs[i][0] == sum_pairs[i][1]])
    # With enumerate
    successful_indices = [i for i,j in enumerate(sum_pairs) if j[0] == j[1]]
    # pdb.set_trace()
    return -1 if len(successful_indices) == 0 else successful_indices[0]

answer = find_even_index([1,2,3,4,3,2,1])



#Sample Tests
# Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
# Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# Test.assert_equals(find_even_index(range(1,100)),-1)
# Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# Test.assert_equals(find_even_index(range(-100,-1)),-1)