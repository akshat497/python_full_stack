
#dictionary
#objects

student={
    #key : value
    "name":"akshat",
    "age":25,
    "phone":12345,
    "city":"delhi"
    
}

print(student.get("name"))

print(student["age"])

# student["email"]="akshat@gmail.com"
student.update({"email":"akshat@gmail.com","address":"qwede123"})

print(student)

# student.pop("name")
# student.popitem()
# print(student)

#clear pura delete krny ky liye

# viewing keys and values

print(student.keys())
print(student.values())
print(student.items())

new_dict=dict.fromkeys(["a","b","c","d"],12)
print(new_dict)
