# function in python
def avg(): #function definition
    a=int(input("Enter the number "))
    b=int(input("Enter the number "))
    c=int(input("Enter the number "))

    average=(a+b+c)/3
    print(average)

avg() #function call

def greet():
    name=input("Enter name ")
    print(f"Hello {name}")
greet()

def goodDay(name,end):
    print("Good Day, "+name)
    print(end)
goodDay("Swapndeep","ThankYou")
goodDay("Swapndeep","Python")

#Return type of a function

def goodDay(name,end):
    print("Good Day, "+name)
    print(end)
a=goodDay("Swapndeep","ThankYou")
print(a) #None because a will just call greet but greet dosen't have return

def good(name):
    return "Good Day, "+name

good("Swapndeep")
a=good("Deep")
print(a)

#Default parameter value 
def greet(name="Swapndeep",ending="ThankYou"):
    print("Goodday, ",name)
    print(ending)
greet()
greet("Aman","Hello")

#Recursion 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

print(f"Factorial of is {fact(5)}")

#Practice Set 
#Greatest of 3
def greatest():
    a=int(input("Enter the number "))
    b=int(input("Enter the number "))
    c=int(input("Enter the number "))

    if a==b==c:
        return "All are equal"
    elif a>=b and a>=c:
        return f"{a} A is Greatest"
    elif b>=a and b>=c:
        return f"{b} B is Greatest"
    else:
        return f"{c} C is Greatest"

result=greatest()
print(result)

#F to C
def f_to_c(f):
    return 5*(f-32)/9 
f=int(input("Enter the Temp in F "))
print(f"{round(f_to_c(f),2)} ^C")

# Recursive fun for sum of n natural num
def natural_sum(n):
    sum=n
    if n==1: 
        return 1
    return sum+natural_sum(n-1)

n=int(input("Enter the Number : "))
a=(natural_sum(n))
print(a)

# pattern print 
def pattern(n):
    for i in range(n,0,-1):
        print("*"*i)
pattern(3)

def pat(n):
    if n==0:
        return
    print("*"*n)
    pat(n-1)
pat(5)

#Remove item from list and strip it 
def remove(list,word):
    result_list=[]
    for item in list:
        if word not in item:
            result_list.append(item)
    return result_list

list=["Aman","Rohan","Deep","Kunal","Rohit"]
word="an"
a=remove(["Aman","Rohan","Deep","Kunal","Rohit"],"an")
print(a)

# Multiplication Table 
def multiply(n):
    for i in range(1,n+1):
        print(f"{n} * {i} = {n*i}")
multiply(10)

str="My name is Swapndeep".lower()
print(str)

a=str.__contains__("name")
print(a)

if "name" in str:
     print("True")
else:
    print("False")

