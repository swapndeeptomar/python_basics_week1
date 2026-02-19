# basic_functions.py
#Addition of 2 Numbers
def add(a, b):
    return a + b

#Subtraction of 2 Numbers
def subtract(a, b):
    return a - b

#Multiplication of 2 Numbers
def multiply(a, b):
    return a * b

#Division of 2 Numbers
def is_even(number):
    return number % 2 == 0

#Factorial of a Number
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Finding the Maximum in a List
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

#Counting Vowels in a String
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

#Checking if a String is a Palindrome
def is_palindrome(text):
    return text == text[::-1]
