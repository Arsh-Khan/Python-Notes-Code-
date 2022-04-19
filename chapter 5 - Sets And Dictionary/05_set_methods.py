# creating a empty set
b = set()
print(b)
print(type(b))


# adding value to the set

b.add(4)
b.add(4)
b.add(5)
b.add(5)#adding values to set repeatedly does not change the set

# cant add list here because list is unhashable
# as we can change value of list 
#but sets are non repetative collection
# b.add([5,6,7])

#but we can add tuples 
b.add((4,5,6))

#also we cannot add dictionaries
# b.add({4:6})

print(b)

# length of the set 
print(len(b)) #prints the length of this set

# removal of an item 

b.remove(5) # removes 5 from set b
# b.remove(15)# throws an error while trying to remove 15
              # which is not present in set 
print(b)

print(b.pop())#returns any arbitary item from set
print(b)

print(b.clear()) #empties the set
