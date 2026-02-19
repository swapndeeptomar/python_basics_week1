print(" My name is Swapndeep \n My course is B.Tech")
print(" My name is Swapndeep \t My course is B.Tech")
print(" My name is Swapndeep \t My course is \"B.Tech\"")
print('My name is Swapndeep \t My course is \'B.Tech\'')

# Practise set 3

name=input("Enter your Name : ")
print(f"Good afternoon {name}")

letter= '''Dear <|Name|>, 
You are Selected 
<|Date|>'''

print(letter.replace("<|Name|>","Swapndeep").replace("<|Date|>","12 Aug 2025"))

text="Python is a Powerfull  Language"
print(text.find("  "))

print(text.replace("  "," OK "))
print(text) # Strings are immutable means original will not change 

let="Dear Swapndeep,This python course is nice."
print(let)

let="Dear Swapndeep,\n\tThis Python course is nice.\nThanks ! "
print(let)