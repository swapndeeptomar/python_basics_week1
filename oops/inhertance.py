# # Single Inheritance
# class Employee:
#     company="ITC"

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def show(self):
#         print(f"Name is {self.name} and salary is {self.salary}")

# class Programmer(Employee):
#     company="ITC Infotech"
#     def __init__(self,name,salary,language):
#         super().__init__(name,salary)
#         self.language=language

#     def showLanguage(self):
#         print(f"Name is {self.name} and language is {self.language}")

# a= Programmer("Deep","12 LPA","Python")

# a.show()
# a.showLanguage()

# # #Miltiple Inheritance
# class Employee:
#     company="ITC"
#     name="Default Name"
#     def show(self):
#         print(f"The name of Employee is {self.name} and company is {self.company}")

# class Coder:
#     language="Python" 
#     def showLanguage(self):
#         print(f"Language of Coder is {self.language}")

# class Programmer(Employee,Coder):
#     Company="ITC Infotech"
#     def showP(self):
#         print(f"The name of compnay is {self.name} and he is good with {self.language}")

# b=Programmer()
# b.show()
# b.showLanguage()
# b.showP()

# # #Multilevel Inheritance

# class Employee:
#     a=1 
# class Programmer(Employee):
#     b=2
# class Manager(Programmer):
#     c=3

# o=Employee()
# print(o.a) # can access only a not b and c
# o=Programmer()
# print(o.a,o.b) #can access both a and b but not c
# o=Manager()
# print(o.a,o.b,o.c)

# # Super Keyword
# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a=1 
# class Programmer(Employee):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Programmer")
#     b=2
# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Manager")
#     c=3

# o=Employee()
# print(o.a)

# o=Programmer()
# print(o.a,o.b) 

# o=Manager()
# print(o.a,o.b,o.c)

# # Class Method
# class Employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"The class Value is {cls.a}")

# e=Employee()
# e.a=45
# e.show()

# # #Property Dcorators
# class Employee:
#     a=1
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name(self,value):
#         self.fname=value.split(" ")[0]
#         self.lname=value.split(" ")[1]

# e=Employee()
# e.name=("Swapndeep Tomar")
# print("OK")
# a=e.fname
# print(a)
# print(e.lname)

# # Sample problem 2

# class Employee:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
    
#     @property
#     def email(self):
#         return f"{self.first}.{self.last}@example.com"        
#     @property
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     @fullname.setter
#     def fullname(self,name):
#         self.first=name.split(" ")[0]
#         self.last=name.split(" ")[1]

# e=Employee("John","Doe")
# print(e.email)
# # print(e.fullname)

# e.fullname="Swapndeep Tomar"
# # print(e.fullname)
# print(e.first)
# print(e.last)
# print(e.email)
# print(e.fullname)