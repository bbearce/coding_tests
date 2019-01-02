# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples:

# "din" => "((("

# "recede" => "()()()"

# "Success" => ")())())"

# "(( @" => "))(("


# Notes:

# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is actually the expected result, not the input! (these languages are locked so that's not possible to correct it).

from collections import Counter

def duplicate_encode(word):
#your code here
    word = word.lower()
    distinct_characters = set(word)
    counts = Counter(word)

    new_string = ['(' if counts[l] < 2 else ')' for l in word]
    new_string = "".join(new_string)
    return new_string

answer = duplicate_encode('Success')
print(answer)


Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")