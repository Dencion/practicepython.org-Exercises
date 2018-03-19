#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string,except with the words in backwards order.

def reverseString(userString):
    '''
    Reverses the order of a string
    '''
    splitString = userString.split()
    newString = splitString[::-1]
    result = " ".join(newString)
    return result 

userString = input("Please enter a few words:")
print(reverseString(userString))
