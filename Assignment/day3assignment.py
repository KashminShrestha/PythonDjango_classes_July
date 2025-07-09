# 1. Even or Odd Checker
# Write a program that takes an integer as input and checks whether it is even or odd.
# Sample Input: 7
# Sample Output: 7 is odd
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# 2. Positive, Negative, or Zero
# Ask the user to enter a number and print whether it is positive, negative, or zero.
# Sample Input: -5
# Sample Output: The number is negative
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
    


# 4. Greatest of Two Numbers
# Take two numbers from the user and print which one is greater. If both are equal, print “Both are equal.”
# Sample Input: 10, 20
# Sample Output: 20 is greater
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")

# 5. Check for Leap Year
# Take a year as input and check if it's a leap year.

# A year is leap if:

# divisible by 4 and

# not divisible by 100 unless also divisible by 400.
# Sample Input: 2020
# Sample Output: 2020 is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Day 3 assignment 
#1.Grade Calculator
# Ask the user to enter marks (0–100) and print the grade:

# 90-100: A

# 80-89: B

# 70-79: C

# 60-69: D

# <60: Fail

marks = int(input("Enter marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
elif marks >= 0 and marks < 60:
    print("Fail")
else:
    print("Invalid input! Please enter marks between 0 and 100.")
    
    
    #2 Voting Eligibility
# Ask the user's age and check if they are eligible to vote (age ≥ 18).
# Sample Input: 16
# Sample Output: You are not eligible to vote

age = 16

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")