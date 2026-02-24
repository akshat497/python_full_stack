# tupples in python are immutable and can only be read u cant add or remove or update any value inside the tupple
# a=(1,2,3,4,5)
# print(a[0])

# # tupples methods
# print(a.count(1))
# print(a.index(3))

# b=(4,2,1,9,11,6) #tuple are ordered and indexed but they are immutable

#sets in python are unordered and unindexed and mutable

set={1,2,3,4,5}

#sets methods
set.add(6)
print(set)
set.remove(3)
print(set)
set.discard(10) # it will not throw error if the element is not present in the set
print(set)
set.pop() # it will remove a random element from the set
print(set)
set.clear() # it will remove all the elements from the set
print(set)
