"""
Lesson: Data Types, Variables, and Why Loops Are Necessary
----------------------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice patterns.
"""

import math

# --- Section 1: Variables and Data Types ---

# TODO: Create a variable called name that stores your name
# TODO: Create a variable called age that stores your age
# TODO: Create a variable called pi that stores the value 3.14159

name = "Alex"
age = "43"
pi = math.pi

# Print each variable
print("Name:", name)
print("Age:", age)
print("Pi:", pi)


# --- Section 2: Why Loops? ---

# Imagine you want to print the numbers 1 through 10.
# First, try it the "long way".

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# TODO: Keep going until you reach 10

# Question for you:
#   What happens if I want to print 1 through 100? Or 1 through 1000?
#   Is it realistic to keep writing print statements forever?


# --- Section 3: For Loops ---
# TODO: Replace the repeated print statements above with a for loop.

for i in range(1, 11):
    print(i)

# Example starter (fill in the blanks):
# for ___ in ___:
#     print(___)

# Hint: What does range(start, stop) do?


# --- Section 4: While Loops ---
# A while loop repeats until a CONDITION is no longer true.

# TODO: Try to print numbers 1 through 10 using a while loop.

j = 1
while j < 11:
    print(j)
    j += 1

# Example starter:
# x = 1
# while ___:
#     print(___)
#     # TODO: Don’t forget to change x, or your loop will run forever!


# --- Section 5: Reflection ---
# Answer these questions (in comments):
# 1. Why is a loop better than writing 100 print statements?
# 2. What does a loop REQUIRE in order to work?
#    (Think: starting point, stopping condition, something that changes)

'''
Because loops allow us to use shorter syntax and make the program more efficient. 
A for loop requires an end point (starting point is 0 by default) or an iterable and the body of the loop.
A while loop requires a condition, a body, and sometimes a statement that prevents an infinite loop.

'''