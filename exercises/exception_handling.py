# # Exception Handling in python
# try:
    # a=int(input("Enter a number : "))
    # print(a)

# except ValueError as v:
#     print(v)
#     print("ok")

# except ZeroDivisionError as z:
#     print(z)

# except Exception as e:
#     print(e) 

# print("Thank You") 

# # Raising exception
# a=int(input("Enter a 1st number : "))
# b=int(input("Enter a 2nd number : "))
# if(b==0):
#     raise ZeroDivisionError
# else:
#     print(f"Division is {a/b}")

# # Try with Else
# try:
#     a=int(input("Enter a number : "))
#     print(a)

# except ValueError as v:
#     print("ok Value is not entered")

# else:
#     print("Executed")

# # Try with Finally
# def main():
#     try:
#         a=int(input("Enter a number : "))
#         print(a)
#         return

#     except ValueError as v:
#         print("ok Value is not entered")
#         return
    
#     finally:
#         print("Finally Executed")
#         return

# main()

# # __name__ and "__main__" in python
# def myFunc():
#     print("Hello World")

# if __name__=="__main__":
#     print("Directly Running")
#     myFunc()
#     print(__name__)  