# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

# Your task is to determine the winner of the game and their score.

# Input Format

# A single line of input containing the string S. 
# Note: The string S will contain only uppercase letters: [A-Z].

# Constraints

# 0<len(S)<=10^6

# Output Format

# Print one line: the name of the winner and their score separated by a space.

# If the game is a draw, print Draw.

# Sample Input

# BANANA

# Sample Output

# Stuart 12

def minion_game(string):
    # your code goes here



    # Works in theory, but is ridiculously inefficient    
    # vowels = ['A','E','I','O','U']
    # # find position of vowels and consonants
    # string_vowels = []
    # string_consonants = []
    # for i,v in enumerate(string):
    #     if vowels.__contains__(v):
    #         string_vowels.append((i,v))
    #     else:
    #         string_consonants.append((i,v))
    # print("here1")
    # words_from_vowels = []
    # words_from_consonants = []
    # # words from vowels
    # for i,v in string_vowels:
    #     for j in range(i, len(string)):
    #         words_from_vowels.append(string[i:j+1])
    # # words from consonants
    # for i,c in string_consonants:
    #     for j in range(i, len(string)):
    #         words_from_consonants.append(string[i:j+1])
    # print("here2")
    # vowel_score = [words_from_vowels.count(i) for i in set(words_from_vowels)]
    # consonant_score = [words_from_consonants.count(i) for i in set(words_from_consonants)]
    # print("here3")
    # if sum(consonant_score) == sum(vowel_score):
    #     print('Draw')
    # elif sum(consonant_score) > sum(vowel_score):
    #     print('Stuart', sum(consonant_score))
    # elif sum(consonant_score) < sum(vowel_score):
    #     print('Kevin', sum(vowel_score))

    vowels = 'AEIOU'
    # string = 'BANANA'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if kevin_score == stuart_score:
        print('Draw')
    elif kevin_score > stuart_score:
        print('Kevin', kevin_score)
    else:
        print('Stuart', stuart_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)
