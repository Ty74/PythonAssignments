

def odd_even():
    for i in range(0,2001):
        if i%2==0:
           print "Number is",i, "This number is even."
        elif i%3==0:
           print "Number is",i, "This number is odd."

odd_even()

def multiply(zero,ten):
    temp=[]
    a = [2,4,10,16]

    total1=[]
    total2=[]
    total3=[]
    total4=[]
    for i in range(0,len(a)):

        total1= a[i]*ten
        total2= a[1]*ten
        total3= a[2]*ten
        total4= a[3]*ten
        #Sprint total1, total2,total3,total4
        return total1,total2, total3, total4



def getMultiply(param):
    list=[param]
    print list
getMultiply(multiply(0,10))


def multiply1(a,ten):




           total = a*ten
           return total


def multiply2():
    a=[1,1,1]
    list=[]
    for i in range(0,len(a)):
        b=multiply1(a,10)
        print [b],
multiply2()
