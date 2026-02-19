class Employee:  #class
    language="Python"
    salary=1200000

deep=Employee()  #object
deep.name="Deep"
print(deep.name,deep.language,deep.salary)

print(Employee,deep)

aman=Employee()  #object
aman.name="Aman"
print(aman.name,aman.language,aman.salary)

# name is an instance attribute 
# salary and language are class attributes
# that belong to class Employee 

rohan=Employee()
rohan.name="Rohan"
rohan.language="JavaScript" # preference of object attribute
print(rohan.name,rohan.language,rohan.salary)

#__________________________________________________________________________

#Self Parameter of a Class

class Employee1:
    name="Employee_name"
    category="Intern"
    language="Python"
    salary=1200000

    def __init__(self,name,category,language,salary):
        self.name=name
        self.category=category
        self.language=language
        self.salary=salary
        print("Creating an Object")
 

    def getinfo(self): # self parameter
        print(f"The name is {self.name} the Category is {self.category} language is {self.language} and salary  is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning User")

# john=Employee1()
# john.name="John"
# john.language="JavaScript"

# john.getinfo()
# john.greet()
# Employee1.getinfo(john) converts in this 
    
aman=Employee1("Aman","Intern","Python","12LAC")
aman.getinfo()


