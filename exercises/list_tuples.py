# # List in Python
friends=["Apple","Orange",7,8,9,False,"Rohan"]
print(friends[0])
 
friends[1]="Grapes"  # Lists are mutable can be changed
print(friends[1])
print(friends[0:5])

# # List Methods

friends.append("Harry")
print(friends)

l1=[34,33,2,4,7,8,22]
l1.sort()
l1.reverse()
l1.insert(3,5555) #insert 5555 at index 3\
print(l1)

l1.pop(3)
print(l1.pop(3))

l1.remove(2)
print(l1)

# # Tuples in python
a=(1,2,3,4,5)
print(type(a)) 

a=(1,)
print(type(a))

a=(1,2,3,4,4,4,5,6,"Name","Hello",False)
print(type(a))

print(a)

no=a.count(4)
print(no)

index=a.index(4)
print(index)

# #Practice Set
fruits=[]
f1=input("Enter Fruit name : ")
fruits.append(f1)
f2=input("Enter Fruit name : ")
fruits.append(f2)
f3=input("Enter Fruit name : ")
fruits.append(f3)
f4=input("Enter Fruit name : ")
fruits.append(f4)
f5=input("Enter Fruit name : ")
fruits.append(f5)

print(fruits)

marks=[]
m1=int(input("Enter marks Here : "))
marks.append(m1)
marks.sort()

print(marks)

l=[34,23,645,123]
print(sum(l))