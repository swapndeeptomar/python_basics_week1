#loops in python
for i in range(5):
    print(i)

#While loop
i=1
while(i<6):
    print(i)
    i+=1
# elements of list print using while loop
l=[1,2,3,4,5,6,7,8,9,10,50,60,111]

i=0
while(i<len(l)):
    print(l[i])
    i+=1

# For Loop in Python

# for loop list
l=[1,4,6,234,6,764]
for i in l:
    print(i)

# for loop tuple
t=(6,34,7,8,999)
for i in t:
    print(i)

# for loop dictionary
marks ={
    "Deep":100,
    "Shubham":56,
    "Aman":34
}
for i in marks:
    print(i,marks[i])
    print(f"{i}:{marks[i]}")

# for loop string
s="Hello World"
for i in s:
    print(i)

# for with else
l=[1,2,3,4,5,6]
for item in l:
    print(item)
else:
    print("Done") # after full for loop then else will execute

# # break stmt

for i in range(20):
    print(i) 
    if i==12:
        break


for i in range(20): 
    if i==12:
        break
    print(i)

# #continue

for i in range(20): 
    if i==12:
        continue
    print(i)

for i in range(20): 
    print(i)
    if i==12:
        continue

#Practice set
#mutiplication table 

num=int(input("Enter the Number : "))

for i in range(11):
    print(f"{i} * {num} = {i*num}")
else:
    print("Done")


l=["Aman","Rohan","Deep","Akshat"]

for name in l:
    if "A" in name or "D" in name:
        print(f"Hello {name}")

for name in l:
    if name.startswith("D"):
        print(f"Hello {name}")


num=int(input("Enter the Number : "))

i=0
while i<11:
    print(f"{num} * {i} = {num*i}") 
    i+=1

#prime number
num=int(input("Enter the Number : "))
if num<0 or num<2:
    print("Enter Valid Number")
for i in range(2,num):
    if num%i==0:
        print("Number is not prime")
        break
else:
    print("Number is Prime")

#sum of n natural num
num=int(input("Enter the Number : "))

i=1
sum=0
while i<=num :
    sum+=i
    i+=1
print(sum)

#factorial of num
num=int(input("Enter the Number : "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

#reverse multiplication
num=int(input("Enter the Number : "))
for i in range(num,0,-1):
    print(f"{num} * {i} = {num*i}")


#Pattern printing
n=int(input("Enter the Number : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

n=int(input("Enter the Number : "))  
for i in range(1,n+1):
    print("*"*i,end="")
    print("")

n=int(input("Enter the Number "))
for i in range(1,n+1):
    if (i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")