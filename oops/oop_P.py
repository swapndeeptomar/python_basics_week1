# # Practice set OOPs

# # programmer class
# class Programmer:
#     company="Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# pr=Programmer("Deep","12LPA",242511)
# prr=pr.name,pr.salary,pr.pin,pr.company
# print(prr)

# calculator 
# class Calculator:
#     @staticmethod
#     def greet():
#         print("Hello User")
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube(self):
#         print(f"The cube is {self.n**3}")
#     def squareroot(self):
#         print(f"The squareroot is {self.n**1/2}")
# a=Calculator(5)
# a.greet()
# a.square()
# a.cube()
# a.squareroot()

# #Class and object instance question
# class Demo:
#     a=10 #class attribute

# b=Demo()
# b.a=0     #instance attribute
# print(b.a) # instance has preference so a=0

# c=Demo()
# print(c.a)  #for other object class attribute was same
# print(Demo.a) #class attribute not change

# class Demo2:
#     def __init__(demo,name,sal,pin):
#         demo.name=name
#         demo.sal=sal
#         demo.pin=pin
#     def greet(demo):
#         print(f"Hello {demo.name}")

# obj=Demo2("Deep","12LPA",22334)
# a=obj.name,obj.sal,obj.pin
# print(a)
# obj.greet()

# # Train Class System
from random import randint
class Train:
    def __init__(self,trainNo,fro,to):
        self.trainNo=trainNo
        self.fro=fro
        self.to=to
        print(self.trainNo)
    def getBook(self):
        print(f"Ticked is booked in train no : {self.trainNo} from {self.fro} to {self.to} ")
    def getStatus(self):
        print(f"Train no : {self.trainNo} is on Time")
    def getFare(self):
        print(f"Ticked Fair in train no : {self.trainNo} from {self.fro} to {self.to} is {randint(222,5555)}")

p=Train(5567,"Delhi","Mumbai")
p.getBook()
p.getStatus()
p.getFare()


# class Student_Login:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
    
#     def validate(self):
#         if len(self.username) > 3 and len(self.password) > 8:
#             if self.username == "deep" and self.password == "password123":
#                 return "Login Successful Welcome User"
#             return "Invalid username or password"
#         else:
#             return "Username must be more than 3 characters and password must be more than 8 characters"
        
#     def register(username,password):
#         if len(username) > 3 and len(password) > 8:
#             return "Registration Successful"
#         else:
#             return "Username must be more than 3 characters and password must be more than 8 characters"


# student1=Student_Login("deep", "password123")
# print(student1.validate())

# student2=Student_Login("abc", "pass")
# print(student2.validate())