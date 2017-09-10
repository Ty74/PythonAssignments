

def names():
    students=[
    {"first_name":"Michael","last_name":"Jordan"},
    {"first_name":"John","last_name":"Rosales"},
    {"first_name":"Mark","last_name":"Gulllen"},
    {"first_name":"KB","last_name":"Tonel"}
    ]

    for i in range(0,len(students)):
        print students[i]["first_name"],students[i]["last_name"]
names()

def peopleUsers():
    users={
      "Students":[
      {"first_name":"Michael","last_name":"Jordan"},
      {"first_name":"John","last_name":"Rosales"},
      {"first_name":"Mark","last_name":"Gulllen"},
      {"first_name":"KB","last_name":"Tonel"}

      ],
      "Instructors":[
        {"first_name":"Michael","last_name":"Choi"},
        {"first_name":"Martin" ,"last_name":"Puryear"}
      ]
    }
    for i in range(0,len(users.Students)):
        print users[0].Students[i]["first_name"],users[0].Students[i]["last_name"]


peopleUsers()
