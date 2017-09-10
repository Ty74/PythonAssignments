def scoresandGrades():
    print "Scores and Grades"
    for b in range (0,10):
      for i in range(60,100):
          if i ==60 and i<=69:
              print "Score:",i,":","Your Grade is D"
              if i==70 and i<=79:
                  print "Score:",i,":","Your Grade is C"
                  if i==80 and i<=89:
                     print "Score:",i,":","Your Grade is B"
                     if i==90 and i<=100:
                        print "Score:",i,":","Your Grade is A"
    print " End of the program Bye!!!"
scoresandGrades()
