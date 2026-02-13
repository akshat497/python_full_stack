# # for 
# # while


# # when we use while loop?

# # when we dont know the starting and ending position 

# # when we know the starting point and the ending point 


# for i in range(4,41,4):
#     print(i)
    
# # find a factorial of a number 

# number=int(input("enter number"))
# # factor=1
# # for i in range(1,number+1):
# #     factor=factor*i

# # print(factor)

# #control flow statement to check if a number is prime or not 


# count=0

# for i in range(1,number+1):
#     if number%i==0:
#         count=count+1
    
# if count>2:
#     print("number is not prime")
# else:
#     print("number is prime")
    
    
#arrays we use in js . list are similar to them


#array store different dataypes values at on plcae



# list=["akshart",34,12.34,False]


# for i in list:
#     print(i)
    
    
#while loop if if dont know where to stop 


# print(" gussed the correct number")
# attempts=0
# while True:
#     if attempts>3:
#         print("to many wrong attemps")
#         break
#     number=int(input("enter a number"))
#     if number == 10:
#         print("You gussed the correct number")
#         break
#     else:
#         attempts=attempts+1
        
        
        
        
#ask user for the username and password and keep asking until its correct



attempt=0
while True:
    if attempt>3:
        break
    username=input("enter ur username")
    password=input("enter ur password")
    if username == "akshat" and password =="1234":
        print("login successfull")
        break
    else:
        attempt=attempt+1
        print("try again!")   
        
        
a=0 # statring point
while a<10:#end point
    
    print("heelow")
    a=a+1# jumps  ya increment
    
    
    
    