# class student:
#     #contructor
#     #what does constructor do?
#     #constructor is a special method that is automatically called when an object of a class is created
#     #it is used to initialize the attributes of the class
    
#     def __init__(self, name, age):
#         #what does self do?
#         #self is a reference to the current instance of the class
#         self.__name = name
#         self.age = age
        
        
#     def display(self):   
#          print("Name:", self.__name)
#          print("Age:", self.age)
         
#     def update_age(self, new_age):
#         self.age = new_age
        
        
        
# s1 = student("Alice", 20)
# s2 = student("Bob", 22)
# s3 = student("Charlie", 19)
# s1.display()


# class BankAccount:
#  def __init__(self, balance):
#   self.__balance = balance
#  def deposit(self, amount):
#   self.__balance += amount
#  def show_balance(self):
#   print(self.__balance)
  
# user1=BankAccount(1000)
# user1.deposit(500)
# user1.show_balance()

#single inheritance
# class animal:
#     def jump(self):
#         print("Animal can jump")
        
  
# class dog(animal):
#     def make_sound(self):
#         print("Dog barks")
        
        
# d1=dog()

# d1.jump()


#multilevel inheritance
# class animal:
#     def jump(self):
#         print("Animal can jump")
        
# class dog(animal):
#     def walk(self):
#         print(" walkinggg")
        
#     def make_sound(self):
#         print("Dog barks")
        
# class cat(dog):
#     def make_sound(self):
#         print("Cat meows")   
        
#     def high_jump(self):
#         print("Cat can jump high")     
        
        
        
# c1=cat()

# c1.jump()
# c1.walk()
# c1.make_sound()
# c1.high_jump()

#multiple inheritance
class animal:
    def jump(self):
        print("Animal can jump")

class dog:
    def walk(self):
        print(" walkinggg")
        
    def make_sound(self):
        print("Dog barks")
        
class cat:
    def make_sound(self):
        print("Cat meows")   
        
    def high_jump(self):
        print("Cat can jump high")
        
class hybrid( cat, dog):
    pass


h1=hybrid()

h1.make_sound()
h1.walk()

h1.jump() #will not be accessed beacuse it is part of animal class and hybrid class is inheriting from cat and dog class only not from animal class