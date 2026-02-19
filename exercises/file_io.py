# f=open("i\\file.txt")
# data=f.read()
# print(data)
# f.close()

# f=open("i\\file.txt","w")
# str= "Hello Swapndeep"
# f.write(str)
# f.close()

# f=open("i\\file.txt")
# line=f.readlines() #list of strings
# print(line)
# f.close()

# f=open("i\\file.txt")
# line=f.readline() #single line
# print(line)
# f.close()

# f=open("i\\file.txt","a")
# f.write("New append\n")
# f.close()

# f=open("i\\file.txt","a+")
# f.write("New Append 2\n")
# f.seek(4)  #pointer for character not line
# print(f.read())
# f.close()

# with open("i\\file.txt","r") as f:
#     print(f.read())

# # Practice Set

# # 1
# with open("i\\file.txt","r") as f:
#     a=f.read().lower()
#     print(a) 
#     if "twinkles" in a:
#         print("Yes")
#     else:
#         print("No")

# # 2 Highscore Game
# import random
# def game():
#     print("You are Playing a Python Game")
#     score=random.randint(1,50)
#     print(score)
#     # fetch file data
#     with open("i\\hiscore.txt","r") as f:
#         hiscore=f.read()
#         if hiscore != "":
#             hiscore=int(hiscore)
#         else:
#             hiscore=0

#     if score>hiscore:
#         with open("i\\hiscore.txt","w") as f:
#             f.write(str(score))
#     return score        
    
# game()

# import time

# start_time=time.time()
# def gentable(n):
#     for i in range (1,11):
#          print(f"{n} * {i} = {n*i}")

#     with open(f"i\\table_{n}.txt","w") as f:
#         f.write(f"Table of {n}\n")
#         for i in range (1,11):
#             f.write(f"{n} * {i} = {n*i}\n")

# for i in range(1,21):
#     print(f"Table of {i} is :- ")
#     gentable(i)
#     print("")

# print("Success")
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed Time: {elapsed_time} seconds")

# import time

# start_time=time.time()
# def gentable(n:int):
#     table=""
#     for i in range (1,11):
#          table += (f"{n} * {i} = {n*i}\n")
#     with open(f"i\\table{n}","w") as f:
#         f.write(f"Table of {n} : \n")
#         f.write(table)

# for i in range(1,21):
#     gentable(i)

# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed Time: {elapsed_time} seconds")

# word="Donkey"

# with open("i\\donkey.txt","r+") as f:
#     content=f.read()
#     new_c=content.replace(word,"####")
#     f.seek(0)
#     f.write(new_c)
#     f.truncate()

# cen=["loreum","ipsum"]

# with open("i\\censored.txt","r+") as f:
#     content=f.read().lower()
#     f.seek(0)

#     for item in cen:
#         if item in content:
#             content=content.replace(item,"####")
#     f.write(content)
#     print(content)
#     f.truncate()

# with open("i\\python.txt") as f:
#     line=f.readline()
#     if "python" in line:
#         print(f"Yes,{line}")
#     else:
#         print("No")

# with open("i\\python.txt") as f:
#     lines=f.readlines()

# lineno=1
# for line in lines:
#     if "python" in line:
#         print("yes",{lineno})
#         break
#     lineno+=1
# else:
#      print("no")



