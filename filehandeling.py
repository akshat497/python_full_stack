# #file handling means when we access the files of our local system
# #r w a x

# # file=open("data.txt","r")
# # content=file.read()

# # print(content)


# append=open("data.txt","a+")

# append.write("\n appended akshat")
# append.close()

import json

# students=[{
#     "name":"akshat",
#     "age":25,
#     "grade":"B"
# },{
#     "name":"ram",
#     "age":24,
#     "grade":"a"
# }]

# file=open("students.json","w")

# json.dump(students,file,indent=2)



def  addStudent():
    try:
       fileR= open("students.json", "r")  
       students = json.load(fileR)
       fileR.close()
    except:
        students = [] 
    
    for student in students:
        students.append(student)
        
        
    print(students)
    name=input("enter student name")
    age=int(input("enter student age"))
    grade=input("enter student grade")
    
    student={
        "name":name,
        "age":age,
        "grade":grade
    }
    file=open("students.json","w")
    students.append(student)
    json.dump(students,file,indent=3)
    file.close()
    
    
while True:
    print("1 press one to add student")
    print("2 press two to exit")
    
    
    number=int(input("enter number"))
    
    if number ==1:
        addStudent()