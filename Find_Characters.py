'''
Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
Copy
Hint: how many loops will you need to complete this task?
'''                                                                                                                                                                                                                                                                                                                                                                                                                  


def printWordsWithO():
    # input
    word_list = ['hello','world','my','name','is','Anna']
    char = 'o'
    # output

    for value1 in word_list:
        if char in value1:
           new_list=[value1]

           print new_list[0]



printWordsWithO()
