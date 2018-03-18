#Exercise 6
#Ask the user for a string and print out whether this string is a
#palindrome or not. 

userWord = input("Please enter a word:")

if userWord == userWord[::-1]:
    print("Your word is a palindrome")
else:
    print("Your word isn't a palindrome")

