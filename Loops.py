# for 
# while


# when we use while loop?

# when we dont know the starting and ending position 

# when we know the starting point and the ending point 


for i in range(4,41,4):
    print(i)
    
# find a factorial of a number 

number=int(input("enter number"))
# factor=1
# for i in range(1,number+1):
#     factor=factor*i

# print(factor)

#control flow statement to check if a number is prime or not 


count=0

for i in range(1,number+1):
    if number%i==0:
        count=count+1
    
    
if count>2:
    print("number is not prime")
else:
    print("number is prime")