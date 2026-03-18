# # class student:
# #     #contructor
# #     #what does constructor do?
# #     #constructor is a special method that is automatically called when an object of a class is created
# #     #it is used to initialize the attributes of the class
    
# #     def __init__(self, name, age):
# #         #what does self do?
# #         #self is a reference to the current instance of the class
# #         self.__name = name
# #         self.age = age
        
        
# #     def display(self):   
# #          print("Name:", self.__name)
# #          print("Age:", self.age)
         
# #     def update_age(self, new_age):
# #         self.age = new_age
        
        
        
# # s1 = student("Alice", 20)
# # s2 = student("Bob", 22)
# # s3 = student("Charlie", 19)
# # s1.display()


# # class BankAccount:
# #  def __init__(self, balance):
# #   self.__balance = balance
# #  def deposit(self, amount):
# #   self.__balance += amount
# #  def show_balance(self):
# #   print(self.__balance)
  
# # user1=BankAccount(1000)
# # user1.deposit(500)
# # user1.show_balance()

# #single inheritance
# # class animal:
# #     def jump(self):
# #         print("Animal can jump")
        
  
# # class dog(animal):
# #     def make_sound(self):
# #         print("Dog barks")
        
        
# # d1=dog()

# # d1.jump()


# #multilevel inheritance
# # class animal:
# #     def jump(self):
# #         print("Animal can jump")
        
# # class dog(animal):
# #     def walk(self):
# #         print(" walkinggg")
        
# #     def make_sound(self):
# #         print("Dog barks")
        
# # class cat(dog):
# #     def make_sound(self):
# #         print("Cat meows")   
        
# #     def high_jump(self):
# #         print("Cat can jump high")     
        
        
        
# # c1=cat()

# # c1.jump()
# # c1.walk()
# # c1.make_sound()
# # c1.high_jump()

# #multiple inheritance
# class animal:
#     def jump(self):
#         print("Animal can jump")

# class dog:
#     def walk(self):
#         print(" walkinggg")
        
#     def make_sound(self):
#         print("Dog barks")
        
# class cat:
#     def make_sound(self):
#         print("Cat meows")   
        
#     def high_jump(self):
#         print("Cat can jump high")
        
# class hybrid( cat, dog):
#     pass


# h1=hybrid()

# h1.make_sound()
# h1.walk()

# h1.jump() #will not be accessed beacuse it is part of animal class and hybrid class is inheriting from cat and dog class only not from animal class

# we want to count number of each sentence in a string


word_count = {}
count=0

# student={
#     "name":"prateek",
#     "age":20,
#     "course":"python"   
# }


# student["number"]=12345
# print(student)
# for word in data.split():
#    word_count[word] = len(word)
     
                
                

# for key ,value in word_count.items():
#     if value>5:
#         count+=1
        
    
# print(count)


# def akshatsSplit(data):
#     var=""
#     length=len(data)
#     arr={}
#     for i in range(length):
#      if i==length-1:
#         var=var+data[i]
#         arr[var]=len(var)
#      if data[i]!=" " :
#         var=var+data[i]
        
#      else:
#         arr[var]=len(var)
#         var=""
#     return arr

               
# print(akshatsSplit("hello world this is a test"))


# string="naman"
# string_1=""

# for i in string:
#       string_1=i+string_1
      
# if string==string_1:
#     print("palindrome")
# else:    print("not palindrome")



# array=["akshat", "prateek", "naman", "prateek", "naman", "naman"]

# unique=[]

# for i in array:
#    if i not in unique:
#       unique.append(i)     
# print(unique)


# list=[22,1,12,2,66]
# max=list[0]
# second_max=list[0]


# for i in list:
#    if i >max:
#       second_max=max
#       max=i
      
# print("max:", max)
# print("second max:", second_max)      
#     
# list=[22,1,12,2,66]



# for i in range(len(list)):
#       for j in range(i+1, len(list)):
#          if list[i]>list[j]:
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
# print(list)

array=[0,2,0,23,0,44]


for i in range(len(array)):
   if array[i]==0:
      for j in range(i+1, len(array)):
         if array[j]!=0:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            break
print(array)
 
 #inheritance 
 
 # when a child inherit property from its parents or grandparents 
 
 
 #single inheritance
 #multiple inheritance
 #multilevel inheritance
 
 
 #single inheritance
class animal:  
   def speak(self):
      print("animal is making sound")
 
 
class dog(animal):
   def bark(self):
      print("dog is barking")     

#multiple inheritance

class father():
   def height(self):
      print("6ft")
      
class mother():
   def color(self):
      print("fair")
      
class grandMother():
   def hairs(self):
      print("long")
      
class child(grandMother,father):
   def color(self):
      print("dark")
   pass      
      
      
#multilevel inheritance
class one():
   def first(self):
      print("i am first class")
      
class two(one):
   def second(self):
      print("i am second class")
class three(two):
   def third(self):
      print("i am third class")
class four(three):
   def fourth(self):
      print("i am fourth class")
class five(four):
   def fifth(self):
      print("i am fifth class")
a=five()

a.first()
a.second()
a.third()
a.fourth()



       
   
    