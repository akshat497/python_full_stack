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
    
    
def delete(type):
    id=int(input(f"enter the {type} id u want to delete")) 
    if type =="students":
        data=getStudents()
    elif type =="Courses":
        data=getCourse()
     
    for i in data:
        if i['id']==id:
            data.remove(i)
            print(f"{type} deleted successfully")
            
    write=open(f"{type}.json","w")
    json.dump(data,write,indent=2)  
 
def writeStudent(name,data):
        write=open(f"{name}.json","w")
        json.dump(data,write,indent=2) 
    
def update():
    print("press 1 to update name")
    print("press 2 to update age")
    id=int(input("enter the id of the student you want to update"))
    choice=int(input("enter the choice"))
    data=getStudents()
    def updateData(type,updatedValue):
        for i in data:
             if i['id']==id:
                i[f'{type}']=updatedValue
    
    if choice==1:
        newName=input("enter the new name")
        updateData("name",newName)
        writeStudent("students",data)        
    elif choice ==2:
         newAge=int(input("enter the new name"))
         updateData("age",newAge)
         writeStudent("students",data)  
    else:
        print("wrong choice")         
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
    print("press 10 to update student")
    
    
    number=int(input("enter the number"))
    if number == 1:
        addStudent()
    if number == 2:
        addCourse()
    if number==3:
        students=getStudents()
        for student in students:
           print(student)
    if number==5:
        enroll("enroll")
    if number==6:
        enroll("unEnroll")
    if number==7:
        searchStudent()
    if number==8:
        delete("students")
    if number==9:
        delete("Courses")
    if number == 10:
        update()
        
        