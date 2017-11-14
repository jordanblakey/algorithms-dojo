def get_middle(s):
# Return the middle character of the word. If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

    if len(s)%2 == 0:
        return (s[(len(s)/2)-1:(len(s)/2)+1])
    else:
        return s[len(s)/2]
