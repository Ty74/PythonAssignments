def arr1():
    arr1=["Person_Name","Pet_Name"]
    return arr1

arr1()

def arr2():
    arr2=["Anna","Benji"]
    return arr2
arr2()


def make_dict(arr1, arr2):
  new_dict = {}
  
  count=0
  for i in enumerate(arr1):  
      count+=1
      for r in enumerate(arr2):
          if count ==1:
             new=[(arr1[0],arr2[0]),(arr1[1],arr2[1])]   
             return new     
          break

make_dict(arr1(),arr2())

def captureInfo(d):
    print dict(d)
    
captureInfo(make_dict(arr1(),arr2()))
