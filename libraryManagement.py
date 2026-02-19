students = [
    {"id": 1, "name": "Amit", "age": 20, "marks": 85},
    {"id": 2, "name": "Neha", "age": 21, "marks": 90},
    {"id": 3, "name": "Rahul", "age": 19, "marks": 78},
    {"id": 4, "name": "Priya", "age": 20, "marks": 88}
]

def addStudent():
    name=input("enter your name")
    age=int(input("enter your age"))
    newStudent={
        "id":len(students)+1,
        "name":name,
        "age":age
    }
    students.append(newStudent)
    print("student added sucessfully")
  
  
def deleteStudent():
    id=int(input("enter student id you want to delete"))
    for student in students:
        if id ==student.get("id"):
            students.remove(student)
        
      
while True:
    print("enter 1 to see students")
    print("enter 2 to add student")
    print("enter 3 to remove student")
    print("enter 9 to exit")
    count=int(input("enter a number"))
    
    
    if count==9:
        break
    if count==1:
       print(students)
    if count==2:
        addStudent()
    if count==3:
        deleteStudent()
    
    


#list