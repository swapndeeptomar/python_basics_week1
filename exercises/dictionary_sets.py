# Dictionary 
marks ={
    "Deep":100,
    "Shubham":56,
    "Aman":34
}
print(marks,type(marks))
print(marks["Deep"])

# Methods
print(marks.get("Deep"))
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Deep":99,"Mohan":77}))
print(marks.pop("Mohan","Default_Value"))
print(marks)
print(len(marks))
 
#Sets in Python

s={1,2,3,4,5,5,5,5,"Deep"}
print(s)

e=set()
print(type(e))

s.add(555)
print(s,type(s))

s.remove(555)
print(s)

# Union and Intersection on set
s1={1,45,6}
s2={7,8,1,78,45}
print(s1.union(s2))
print(s1.intersection(s2))

#practise set chapter 5
# words={"madad":"help",
#        "kursi":"chair",
#        "billi":"cat"}
# word=input("Enter the Word you want meaning of : ")
# print(words[word])

# s3=set()
# for i in range(8):
#     num=int(input("Enter the Numbers : "))
#     s3.add(num)
# print(s3)

s4=set()
s4.add(18)
s4.add('18')
s4.add(18.0)
print(s4)
print(len(s4))

d={}
for i in range(4):
    name=input("Enter friends Name : ")
    lang=input("Enter language name : ")
    d.update({name:lang})

print(d)

s={8,7,12,"Deep",[1,2]}
#no index in set also no update in set is possible
#s[4][0]=9