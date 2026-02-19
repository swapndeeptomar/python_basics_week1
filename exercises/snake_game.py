'''
Snake Water Gun Game

snake wat = snake
water gun = water
snake gun = gun
same same = draw

'''
import random
com=random.randint(1,3)

print("Snake Water Gun Game")
dict={"snake":1,"water":2,"gun":3}

you_c=input("Enter Your Choice : ")
you=dict[you_c]

rev_dict=dict={1:"snake",2:"water",3:"gun"}
print(f"Your Choice : {rev_dict[you]} \nComputer Choice : {rev_dict[com]}")

# if you==com:
#     print("Draw")
# else:
#     if you==1 and com==2:
#         print("You Win")
#     elif you==1 and com==3:
#         print("You Lose")

#     elif you==2 and com==1:
#         print("You Lose")
#     elif you==2 and com==3:
#         print("You Win")

#     elif you==3 and com==1:
#         print("You Win")
#     elif you==3 and com==2:
#         print("You Lose")
#     else:
#         print("Something Went Wrong")

if you==com:
    print("Draw")
else:
    if (you-com)==2 or (you-com)==-1:
        print("You Win")
    else:
        print("You Lose")