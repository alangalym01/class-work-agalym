"""
Lesson: Conditionals in Python
------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how conditionals change what happens.
"""

# --- Section 1: True or False? (Boolean Expressions) ---

# Conditionals always depend on something being True or False.
# Let's explore.

# TODO: Create two variables. One that represents age, and the other a boolean that is True if you are a student and false if you are not:
age = 17
is_student = True

# What happens when we compare numbers?
print("Is age greater than 18?", age > 18)
print("Is age less than 13?", age < 13)

# What happens when we compare equality?
print("Is age exactly 16?", age == 16)

# What happens when we use a variable directly?
print("Is student status True?", is_student)

# Reflection Question (write your answer in a comment):
# Q: Why do all of these print either True or False?

# Because we're passing in a boolean value

# --- Section 2: If Statements ---

# Problem: You want to check if someone can vote (age >= 18).
# First, try without conditionals (just print something no matter what).

print("You can vote!")   # TODO: What’s wrong with this approach?


# Now add an IF statement:
if age >= 18:
    print("You can vote!")


# --- Section 3: If/Else ---

# TODO: Write a program that checks if a number is even or odd.
# Steps to guide you:
# 1. Make a variable called num
# 2. Use the modulo operator (%) to check if num % 2 == 0
# 3. If even, print "Even number"
# 4. Otherwise, print "Odd number"

num = 13

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# --- Section 4: If / Elif / Else ---

# TODO: Imagine a grading system:
#   - 90 or above → "A"
#   - 80 or above → "B"
#   - 70 or above → "C"
#   - 60 or above → "D"
#   - below 60   → "F"

# Write this using if / elif / else statements.
grade = 92

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# --- Section 5: Nesting Conditionals ---

# TODO: Ask two questions:
#   1. Is the person a student?
#   2. Is their age under 18?
# If both are true, print "You are a student and a minor."
# Otherwise, print something else.

is_student = bool(int(input("Is the person a student? 1 - Yes, 2 - No")))
age_under_18 = bool(int(input("Are they under 18? 1 - Yes, 2 - No")))

if is_student and age_under_18:
    print("You are a student and a minor")
else:
    print("Hot dog")

# --- Section 6: Reflection ---
# Answer in comments:
# 1. What does a conditional REQUIRE in order to run effectively?
#    (Think: a test/condition that evaluates to True or False)
# 2. How do elif and else make your code shorter or more readable?
# 3. Can you think of a situation in real life where you’d use multiple conditionals?

'''
a conditional requires an if statement, a condition, and a result of that condition

elif is a shorter way of writing else: if

Determining the price of an ice cream based on its falvor
'''