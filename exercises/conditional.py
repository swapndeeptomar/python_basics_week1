a=int(input("Enter your Age "))
if(a>=18):
    print("You are Eligible to vote")
elif(a<0):
    print("Invalid Age")
elif(a==0):
    print("Zero Entered Age")
else:
    print("You are not Eligible")
print("End of Program")

# #Practise set
nums=[]
for i in range(4):
    num=int(input("Enter the Number : "))
    nums.append(num)
print(nums)

if(nums[0]>nums[1] and nums[0]>nums[2] and nums[0]>nums[3]):
    gre=nums[0]
    print(f"Greatest is {gre}")
elif(nums[1]>nums[0] and nums[1]>nums[2] and nums[1]>nums[3]):
    gre=nums[1]
    print(f"Greatest is {gre}")
elif(nums[2]>nums[0] and nums[2]>nums[1] and nums[2]>nums[3]):
    gre=nums[2]
    print(f"Greatest is {gre}")
elif(nums[3]>nums[0] and nums[3]>nums[2] and nums[3]>nums[1]):
    gre=nums[3]
    print(f"Greatest is {gre}")
else:
    print("Enter Valid Numbers")


nums = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

greatest = nums[0]
for num in nums:    
    if num > greatest:
        greatest = num

print(f"The greatest number is {greatest}")

marks=[]
for i in range(3):
    mark=int(input("Enter Marks "))
    marks.append(mark)
print(marks)

total=0
for mark in marks:
    total+=mark
print(total)

per=total/3

if(per>=40):
    if(marks[0]>=33 and marks[1]>=33 and marks[2]>=33):
        print("Passed in all Subjects",per)
    else:
        print("Failed in One Subject",per)
else:
    print("Failed",per)

spam=("make a lot of money", "buy now", "subscribe this", "click this")
message=input("Enter the Message ").lower()
print(message)
if(spam[0] in message or spam[1] in message or spam[2] in message or spam[3] in message):
    print("Message is Spam")
else:
    print("Message looks Good")

spam=("make a lot of money", "buy now", "subscribe this", "click this")
message=input("Enter the Message ").lower()
print(message)

is_spam=False
for spam_item in spam:
    if spam_item in message:
        is_spam=True
        break
if is_spam:
    print("Message is Spam")
else:
    print("Message is not spam")

nums=[12,13,44,56,78,1,2,3,4,5,88,90,100]
num=int(input("Enter the Number "))

if(num in nums):
    print("Number is Present in List")
else:
    print("Number is not in List")

post="Hey every one my name is Swapndeep I am currently practcing python programming"
post1=post.lower()
print(post1)

if "swapndeep" in post1:
    print("Yes")
else:
    print("No")

# match case in python
http_message=int(input("Enter code "))
match http_message:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Error")
