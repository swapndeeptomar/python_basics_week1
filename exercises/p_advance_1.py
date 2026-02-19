# Walrus Operator
if (n:=len([1,2,3,4,5])>3):
    print("Too Long")

# Type Definiton
n : int=5
print(n.is_integer)

name : str="Deep"
def sum(a : int,b: int)->int:
    return a+b
print(sum(3,6))

# Advance Typing Hints
from typing import Dict,Tuple,List,Union

numbers:List[int]=[1,2,3,4,5]
person:Tuple[str, int]=("Alice", 30)
scores: Dict[str, int]={"Alice":90, "Bob": 85}
print(numbers)
print(person)
print(scores)

# match case in python (switch case)
def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unkonwn Status"
        
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(9))

# Dict merge 
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
mer=dict1|dict2
print(mer)

dict1 |= dict2
print(dict1)

# Global Keyword
def fun():
    global b
    a=3  # Local Variable
    print(a,b)
b=89
print(b)
fun()

# Enumerate Function
l=[34,35,36,37,38,39]
for i,item in enumerate(l):
    print(i,item)

#List Comphrensions
l1=[34,35,36,37,38,39,40,45,49,80]
l2=[i for i in l1 if i % 5==0] #list 1 ke liye jo iterable hai vahi output banega different name pe error ayegi
l3=[i*i for i in l1 ]
print(l2)
print(l3)

from exception_handling import myFunc
