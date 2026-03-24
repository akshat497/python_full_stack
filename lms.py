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
 
def enroll(task):
    students=getStudents()
    courses=getCourse()
    studentsId=int(input("enter your students id"))
    courseId=int(input("enter the course id"))
    if task=="enroll":
          for student in students:
            if student["id"]==studentsId:
              student['courses'].append(courseId)
              print("enrolled successfully")
    elif task=="unEnroll":
          for student in students:
            if student["id"]==studentsId:
              student['courses'].remove(courseId)
              print("unEnrolled successfully")
            
  
            
            
    writeStudent=open("students.json","w")
    json.dump(students,writeStudent,indent=2)   



def searchStudent():
    students=getStudents()
    searchName=input("enter the student name you want to search")
    
    for student in students:
        if student['name']==searchName:
            print(student)
    
    
def deleteStudent():
    students=getStudents()
    id=int(input("enter the student id u want to delete"))  
    for student in students:
        if student['id']==id:
            students.remove(id)
     
       
while True:
    print("press 1 to add student")
    print("press 2 to add course")
    print("press 3 to view students")
    print("press 4 to view courses")
    print("press 5 to enroll ")
    print("press 6 to unEnroll")
    print("press 7 search  student")
    print("press 8 to delete student")
    print("press 9 to delete course")
    
    
    number=int(input("enter the number"))
    if number == 1:
        addStudent()
    if number == 2:
        addCourse()
    if number==5:
        enroll("enroll")
    if number==6:
        enroll("unEnroll")
    if number==7:
        searchStudent()