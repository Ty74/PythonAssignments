'''
def draw_stars(param1,param2,param3,param4,param5,param6,param7):
    x=[param1,param2,param3,param4,param5,param6,param7]
    for value in range(0,len(x)):
        if x[value]==4:
            print "****"
        if x[value]==6:
           print "******"
        if x[value]==1:
           print "*"
        if x[value]==3:
           print "***"
        if x[value]==5:
           print "*****"
        if x[value]==7:
           print "*******"
        if x[value]==25:
           print "*************************"

draw_stars(4,6,1,3,5,7,25)
'''

def draw_starsII(param1,param2,param3,param4,param5,param6,param7):
    x=[param1,param2,param3,param4,param5,param6,param7]
    for value in range(0,len(x)):
        if x[value]==4:
            print "****"
        if x[value]=="Tom":
           print x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower()
        if x[value]==1:
           print "*"
        if x[value]=="Michael":
           print x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower()
        if x[value]==5:
           print "*****"
        if x[value]==7:
           print "*******"
        if x[value]=="Jimmy Smith":
            print x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower(),x[value][0:1].lower()

draw_starsII(4,"Tom",1,"Michael",5,7,"Jimmy Smith")
