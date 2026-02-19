a='Deep'
b="Deep"
c="""Deep"""

print(a,b,c)
print(len(a))
 
slice=a[0:3]
print(slice)

slice=a[-4:-2]
print(slice)

skip=a[1:4:2]
print(skip)

str="abcdefghijklmnopqrstuvwxyz"
print(str[1:27:4])

print(a.find("e"))
print(a.startswith("D"))
print(a.count("e"))
print(a.replace("e","a"))
print(a.split("ep"))