'''
Assignment: Filter by Type
Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

Integer
If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

String
If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

List
If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
'''
def checkGreater(number):
    print "200 was entered"
    if number > 100:
        print "That's a big number"
    elif number< 100:
        print "That's a small number"
print checkGreater(200)

def checkLess(number):
    print "50 was entered"
    if number > 100:
        print "That's a big number"
    elif number< 100:
        print "That's a small number"
print checkLess(50)



def  checkInput():
    input1=raw_input("Please enter a sentence:")
    input1=input1.split()
    d=dict()
    d=d.fromkeys(input1)
    for i in input1:
        d[i]=input1.count(i)
        if d[i]>=50:
            print "long sentence"
            break;
        elif d[i]<=50:
            print "Short sentence"
            break;
print checkInput()

def checkList():
    input1=raw_input("Please enter a sentence:")
    input1=input1
    list1=[input1]
    d=dict()
    d=d.fromkeys(list1)
    for values in list1:
        d[values]=len(values)
        if d[values]>=50:
            print "long sentence"
            break;
        elif d[values]<=50:
            print "Short sentence"
            break;
print checkList()
