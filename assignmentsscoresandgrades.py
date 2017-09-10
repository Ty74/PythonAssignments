import random
def scoresandGrades():
    
    print "Scores and Grades"
    for i in range(0,4):
        r=random.uniform(1,59)
        q=random.uniform(59,69)
        d=random.uniform(69,79)
        k=random.uniform(79,89)
        n=random.uniform(89,100)
        if  i<=1 or r<=59:
           print "Score:", random.uniform(i,59),":"," Your Grade is F"
        if i>59 or q==69 or q<=60:
           print "Score:",random.uniform(60,69),":","Your Grade is D"
        if i>69 or d==79 or d<=70:
           print "Score:",random.uniform(70,79),":","Your Grade is C"
        if i>79 or k==89 or d<=80:
           print "Score:",random.uniform(80,89),":","Your Grade is B"
        if i>89 or k==100 or k<=90:
           print "Score:", random.uniform(90,100),":","Your Grade is A"
    print "End of the program Bye!!!"

scoresandGrades()
