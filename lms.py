import json
import os

def getStudents():
     if not os.path.exists("students.json"):
        make=open("students.json","x")
        make.close()
     else:
        ReadStudent=open("students.json","r")
        try:
           return json.load(ReadStudent)
        except:
            return []
           
    
def getCourse():
      if not os.path.exists("courses.json"):
        make=open("courses.json","x")
        make.close()
      else:
        ReadCourses=open("courses.json","r")
        try:
           return json.load(ReadCourses)
        except:
            return []
                
def addStudent():
    
    students=getStudents()
    print(students)
         
    name=input("enter the name ")
    age=int(input("enter the age"))
    student={
        "id":len(students)+1,
        "name":name,
        "age":age,
        "courses":[]
    }
    students.append(student)
    writeStudent=open("students.json","w")
    json.dump(students,writeStudent,indent=2)
    
def addCourse():
   
    Courses=getCourse()
    name=input("enter the name ")
    duration=int(input("enter the duration"))
    course={
        "id":len(Courses)+1,
        "name":name,
        "duration":duration
    }
    Courses.append(course)
    writeStudent=open("Courses.json","w")
    json.dump(Courses,writeStudent,indent=2)    
 
def enroll():
    students=getStudents()
    courses=getCourse()
    
    studentsId=int(input("enter your students id"))
    
    print(courses)
    
    courseId=int(input("enter the course id"))
    
    for student in students:
        if student["id"]==studentsId:
            student['courses'].append(courseId)
            
            
    writeStudent=open("students.json","w")
    json.dump(students,writeStudent,indent=2)   
    
while True:
    print("press 1 to add student")
    print("press 2 to add course")
    print("press 3 to view students")
    print("press 4 to view courses")
    print("press 5 to enroll ")
    print("press 6 to update")
    print("press 1 to add student")
    print("press 1 to add student")
    
    
    number=int(input("enter the number"))
    if number == 1:
        addStudent()
    if number == 2:
        addCourse()
    if number==5:
        enroll()