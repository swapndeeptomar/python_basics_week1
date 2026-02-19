# Normal Function Definition
def square(n):
    return n * n
square = square(5)
print(square)  # Output: 25

#lambda Function Definition
square=lambda x:x*x
sum=lambda a,b,c:a+b+c
print(square(5))  # Output: 25
print(sum(1, 2, 3))  # Output: 6   

# String Joins
l=["apple", "banana", "cherry"]
res="::".join(l)
print(res) 

# Format method
a="{} is a good {}".format("Deep", "boy") 
print(a)
b="{1} is a good {0}".format("Deep", "boy") 
print(b)

# Map Function
l=[1, 2, 3, 4, 5]
square=lambda x:x*x
res=list(map(square,l))
print(res)

# Filter Function
def even(n):
    if n%2==0:
        return True
res=list(filter(even, l))
print(res)

# Reduce Function
from functools import reduce
sum=lambda a,b:a+b
mul=lambda a,b:a*b
res=reduce(sum,l)
res2=reduce(mul,l)
print(res)  
print(res2)

# Practice Set
n=7 
for i in range(0,11):
    print(f"{n*i}")

table=[str(7*i) for i in range (1,11)]
s="\n".join(table)
print(s)

div5=lambda x: x if x%5==0 else 0
num=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(div5,num))
print(res)

# max using reduce
from functools import reduce
l=[10,20,50,70,90,100]
max=lambda x,y:x if x>y else y
res=(reduce(max,l))
print(res)
