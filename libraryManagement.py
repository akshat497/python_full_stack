import datetime as dt

students = [
    {"id": 1, "name": "Amit", "age": 20, "allotedBooks": []},
    {"id": 2, "name": "Neha", "age": 21, "allotedBooks": []},
    {"id": 3, "name": "Rahul", "age": 19, "allotedBooks": []},
    {"id": 4, "name": "Priya", "age": 20, "allotedBooks": []}
]
books = [
    { "id": 1,
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 399,
        "pages": 208,
        "available":True
    },
    {"id": 2,
        "name": "Atomic Habits",
        "author": "James Clear",
        "price": 499,
        "pages": 320,
        "available":True
    },
    {"id": 3,
        "name": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "price": 350,
        "pages": 336,
        "available":True
    }
]
def add(type):
    name=input("enter your name")
    if type=="student":
        
        age=int(input("enter your age"))
        newStudent={
        "id":len(students)+1,
        "name":name,
        "age":age
        }
        students.append(newStudent)
        print("student added successfully")
    elif(type=="book"):
        author=input("enter author name")
        price=input("enter book price ")
        pages=input("enter book pages")
        book={
        "id":len(books)+1,
        "name":name,
        "author":author,
        "price":price,
        "pages":pages
        }
        books.append(book)
        print("books added successfully")
    else:
        print("something went wrong")
        
  
def deleteStudent():
    id=int(input("enter student id you want to delete"))
    
    for student in students:
        if id ==student.get("id"):
            students.remove(student)
            
    print("student deleted sucessfully")
    
    

def allotBook():
  
    student_not_found=0 
    student_id=int(input("enter student id"))
    for student in students:
        if student_id==student.get("id"):
            for book in books:
                if book.get('available'):
                    print(book.items())
                    
            book_id=int(input("enter book id"))
            for book in books:
               if book.get('id')==book_id:
                    if book['available']==True:
                       book['available']=False
                       student.get('allotedBooks').append({"book_id":book_id,"allotedDate":dt.date.today()})
                    else:
                        print(f"book already alloted to {student.get('name')}")
        else:
           student_not_found=student_not_found+1
      
    if student_not_found==len(students):
        print("No such student found") 
        
        
def returnBook():
    student_not_found=0 
    book_found={}
    student_id=int(input("enter student id"))
    book_id=int(input("enter book id"))
    for student in students:
        if student['id']==student_id:
            for allotedBook in student['allotedBooks']:
                if allotedBook['book_id']==book_id:
                    for book in books:
                        if book['id']==book_id:
                            book['available']=True
                            student['allotedBooks'].remove(allotedBook)
                            
                    
                
                
            
                    
while True:
    print("enter 1 to see students")
    print("enter 2 to add student")
    print("enter 3 to remove student")
    print("enter 4 to add new book")
    print("enter 5 to view  books")
    print("enter 6 to allot  book")
    print("enter 7 to return  book")
    
    print("enter 9 to exit")
    count=int(input("enter a number"))
    
    
    if count==9:
        break
    if count==1:
       print(students)
    if count==2:
        add("student")
    if count==3:
        deleteStudent()
    if count==4:
        add("book")
    if count==5:
        print(books)
    if count==6:
       allotBook()
    if count==7:
       returnBook()
        
    
    


#list