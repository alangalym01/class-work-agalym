"""
Lesson: Loops, Conditionals, and User Input
-------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how programs can respond to user input.
"""

# --- Section 1: Getting Input from the User ---

# TODO: Ask the user for their name and store it in a variable
name = input("Your name: ")

# TODO: Ask the user for their age and store it as an integer
age = int(input("Your age: "))

# Print out a greeting
print("Hello,", name)
print("You are", age , "years old")


# --- Section 2: Conditionals with Input ---

# TODO: Check if the user is old enough to vote (18+)
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# TODO: Ask the user for a number and check if it's even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# --- Section 3: Loops with Input ---

# Problem: You want to ask a user for 5 test scores and print them
# without loops, you'd have to write 5 separate inputs.  

# TODO: Try writing 5 input statements manually first (commented out)
score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))
score4 = int(input("Score 4: "))
score5 = int(input("Score 5: "))

# Question: How could a loop make this easier?
    # A loop would replace all the repetitive code

# --- Section 4: For Loops with Input ---

# TODO: Use a for loop to ask for 5 test scores and print each one
# Example starter:
for i in range(5):
    score = int(input("Enter score #" + str(i+1) + ": "))
    print("You entered:", score)


# --- Section 5: While Loops with Input ---

# TODO: Keep asking the user to enter a positive number
# until they actually do. Use a while loop.
# Example starter:
num = int(input("Enter a positive number: "))
while num <= 0:
    print("That is not positive. Try again!")
    num = int(input("Enter a positive number: "))
print("Thank you! You entered:", num)


# --- Section 6: Challenges ---

# 1. Ask the user for a number and tell them if it's divisible by 3, 5, or both

input_num = int(input("Enter number: "))

if input_num % 3 == 0 and input_num % 5 == 0:
    print("both")
elif input_num % 3 == 0:
    print("divisible by three")
elif input_num % 5 == 0:
    print("divisible by five")
else:
    print("Neither")

# 2. Ask the user for their favorite color repeatedly until they type "stop"

input_color = input("Favorite color: ")
while input_color != "stop":
    print("Nice! Now enter another one.")
    input_color = input("Favorite color: ")

# 3. Create a mini grading program:
#     - Ask the user for scores until they type -1
#     - Keep track of how many scores are passing (>= 60)
#     - Print a summary at the end

user_score = int(input("Enter your score (enter -1 to exit): "))
passing_scores = []

while user_score != -1:
    if user_score >= 60:
        passing_scores.append(user_score)
    user_score = int(input("Enter score: "))
print(f"{len(passing_scores)} of your scores are passing! Your highest score is {max(passing_scores)}")


# --- Section 7: Reflection ---
# 1. How does using input change the way your program works compared to fixed variables?
# 2. How do loops and conditionals work together when handling user input?
# 3. What are some real-world programs where loops + conditionals + input are all necessary?

'''
Input makes the program interactive. Loops and conditionals allow us to add functionality based on what the user inputs. Specifically, 
loops allow us to ask the user continuously, for example until the program receives a certain input, while conditionals allow us to 
output different results based on conditions. Any game requires a while loop to run the program and conditionals to add events.
'''