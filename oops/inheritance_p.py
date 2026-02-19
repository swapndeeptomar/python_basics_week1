#Class and Objects
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"Vector is {self.i}i + {self.j}j")

# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k=k
#     def show(self):
#         print(f"Vector is {self.i}i + {self.j}j + {self.k}k")

# a=TwoDVector(1,2)
# b=ThreeDVector(1,2,3)
# a.show()
# b.show()

# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dog(Pets):
#     def bark(self,bark):
#         self.bark=bark
#         print(bark)
# d=Dog()
# d.bark("Bow Bow")

# class Employee:
#    sal=500
#    inc=10
#    @property
#    def salaryafterincrement(self):
#        return self.sal+self.sal*(self.inc/100)
#    @salaryafterincrement.setter
#    def salaryafterincrement(self,sal):
#     self.inc=((sal/self.sal)-1)*100
 
# e=Employee()
# # print(e.salaryafterincrement)
# e.salaryafterincrement=(1000)
# print(e.inc)

# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return f"{self.r+c2.r} + {self.i+c2.i}i"
    
# c1=Complex(1,2)
# c2=Complex(3,4)

# print(c1+c2)
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,v):
        result=Vector(self.x+v.x,self.y+v.y,self.z+v.z)
        return result
    def __mul__(self,v):
        result=Vector(self.x*v.x,self.y*v.y,self.z*v.z)
        return result
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)

print(v1+v2)
print(v1*v2)

print(v2*v3)
print(v2*v3)
print(len(v1))



        
