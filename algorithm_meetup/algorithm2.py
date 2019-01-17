

# only take 1 or 2 steps

# find the combinations of 1 or 2 steps needed to  get to the top of any step amount

# n = 1
# a=1
# d=0
# step_combos = (1) # 1 <> 0

# n = 2
# a=2
# d=1
# step_combos = [(1,1),(2)] # 2 <> 1

# n = 3
# a=3
# d=1
# step_combos = [(1,1,1),(1,2),(2,1)] # 3 <> 1

# n = 4
# a=5
# d=2
# step_combos = [(1,1,1,1),(1,1,2),(1,2,1),(2,1,1),(2,2)] # 5 <> 2

# n = 5
# a=8
# d=3
# step_combos = [(1,1,1,1,1),(1,1,1,2),(1,1,2,1),(1,2,1,1),(2,1,1,1),(2,2,1),(2,1,2),(1,2,2)] # 8 <> 3

# n = 6
# a = 13
# d=5
# step_combos = [(1,1,1,1,1,1),(1,1,1,1,2),(1,1,1,2,1),(1,1,2,1,1),(1,2,1,1,1),(2,1,1,1,1),(2,2,1,1),(1,2,1,2),(2,1,2,1),(1,1,2,2),(2,1,1,2),(1,2,2,1),(2,2,2)] # 13 <> 5

from itertools import combinations 
perm = combinations([1, 2], 3) 
print([i for i in perm])


def stepClimber(stairs):
    """
    Important to note that this only serves to represent the
    function and not the combination theory. The function is that 
    if you have the answer to the previous two stair step inputs, 
    then you can just add their answers to get the new answer.
    """

    if stairs < 1: 
        return 0
    if stairs == 1: 
        return 1
    if stairs == 2: 
        return 2

    return stepClimber(stairs-1) + stepClimber(stairs-2)


if __name__ == '__main__':
    n = int(input())
    print(stepClimber(n))

