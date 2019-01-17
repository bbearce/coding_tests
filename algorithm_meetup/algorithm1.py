test1 = "" # True
test2 = "[" # False
test3 = "]" # False
test4 = "[]" # True
test5 = "[[asdf{{dasf}}asdfas(ads)]]" # True
test6 = "[" # False
test7 = "[" # False

import pdb

# keys = {'(':')','[':']','{':'}'}
# check for key or value of character and if not then move on
# Build stack as you gather open parenthesis
# if it's not a key and the stack is empty, return False
# if the stack is not empty, 
# 

class algo1():
    def __init__(self):
        pass

    def check(self, string):
        text = string
        keys = {'(':')','[':']','{':'}'}
        stack = []
        # pdb.set_trace()
        for i in text:
            if i in keys.keys():
                stack.append(i)
            elif i in keys.values() and len(stack) != 0:
                key = stack.pop()
                if i != keys[key]: return False
            elif i in keys.values() and len(stack) == 0:
                return False
            else:
                pass

        return True if len(stack) == 0 else False

        

    




