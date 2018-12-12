
"""
We need to rearrange the words in x using only a 1 character temp variable
"""
string = list("Rearrange something")

# First reverse the entire string
def reverse_string(x = string):
    """
    Notice how we use a temp variable y that is 1 character in size at all times
    """
    for i in range(int(len(x)/2)):
        y = x[-1*i-1]
        x[-1*i-1] = x[i]
        x[i] = y
    return x

# Notice that at this point none of i, x, or y exist in memory (try >>> locals() )
string = reverse_string(string)

# Now reverse individual words
def reverse_words():
    j=0 # to track spaces (or more specifically the beginning of each word)
    for i in range(len(string)):
        # If we hit a space reverse everything up to the space
        if string[i] == ' ':
            string[j:i] = reverse_string(string[j:i])
            # Update the beginning of next word to 1 after the space
            j = i+1

    # Reverse the last word, because it doesn't have a space after it to trigger its reverse
    string[j:len(string)] = reverse_string(string[j:len(string)])

# Notice that at this point none of i, x, or y exist in memory (try >>> locals() )
print(string)