"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["ice cream", "hot dog", "cheeseburger", "tacos", "cheesecake"]

# Access items by index (first = 0):
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?

        # There is no item at index 100

# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()
foods.append("beef wellington")

# TODO: Insert a food at the beginning with .insert()
foods.insert(0, "doner")

# TODO: Remove one food from the list with .remove()
foods.remove("hot dog")

# TODO: How many foods are in the list? Use len()
print(len(foods))

# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?

        # chocolate is not in the list

# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.
for i in foods:
    print(i)

# Bug Exploration:
# Change your loop to go past the length of the list:
for i in range(len(foods)):
    print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?

        # Because the range doesn't match the length of the list

# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Kevin",
    "age": 30,
    "student": False
}

# TODO: Make a dictionary with at least 3 pieces of information about yourself.

student = {
    "name": "Alan",
    "grade": "12th",
    "school": "NMH",
    "age": 18
}

# Access values using keys by using the .get() method rather than indexing
print(f"My name is {student.get('name')}")
print(f"My age is {student.get('grade')}")
print(f"My favorite color is {student.get('school')}")

# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?

        # This error is called KeyError, and the get() method returns the value of None if the key is not found

# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.

student.update({"sport":"water polo"})

# TODO: Change the value of an existing key.

student.update({"school":"Deerfield Academy"})

# TODO: Remove one key-value pair.

student.pop("grade")

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?

        # It also throws a KeyError

# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()

for i in student.items():
    print(i)

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

        # It only prints the keys

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?

        # use .items()

# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.

friends = [
    {"name":"Alex", "food":"ice cream"},
    {"name":"Emma", "food":"cheesecake"},
    {"name":"David","food":"egg coffee"}
]

# TODO: Print the favorite food of the second friend.
print(friends[1].get("food"))

# TODO: Loop through and print "<name> likes <food>" for each friend.

for friend in friends:
    print(friend.get("name"), "likes", friend.get("food"))

# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?

        # What might happen is I can get a KeyError because "hobby" 
        # is not a key in the dictionary. However, this can be prevented by using .get() to get the keys.


# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# 2. When would you want to use a dictionary instead of a list?
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# 4. What types of mistakes gave you the most errors today?
# 5. How might noticing errors actually help you learn?


'''
A list is different from a dictionary because it stores data in key-value pairs, as opposed to lists' indexing. You would want to use a dictionary instead
of a list when you want custom keys. An example of a real-world dictionary+list use case is a phonebook. Each dictionary is a contact with keys 
like name, address, and phone number, and the list is a collection of those contacts. The only error I've gotten today was KeyError. Noticing errors 
can help you learn techniques using which would prevent you from making those mistakes again.
'''