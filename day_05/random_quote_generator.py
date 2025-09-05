# Starter file for students to create a Random Quote Generator

# Step 1: Import any necessary modules
# Step 2: Define a function to load quotes from a file when called
# Step 3: Define a function that returns a random quote when called
# Step 4: Define a main function that runs the program. Make sure to call the function.

'''
* Objective: In the file `random_quote_generator.py`, read lines from `quotes.txt` use the random `package` to generate random quotes for a user.
    * Create a function load_quotes()
        * *Parameter: file_name_1.txt* 
        * *Return Value: List of quotes from file_name_1.txt*
    * Create a function get_random_quote()
        * *Parameter: list of quotes*
        * *Return Value: random quote string*
    * Create a function add_to_favorites()
        * *Parameter: file_name_2.txt and random_quote*
        * *Doesn't have a return value, but should create a new file and add quotes if user chooses quote as a favorite.  
    * Create a function view_favorites()
        * *Parameter: file_name_2*
        * *Return Value: List of quotes from file_name_2.txt*

    * Challenge: Create a new file called  `authors.txt` with the authors of each quote on the same line number as the quote.  
    Modify your code to print `"Quote" - Author`

### Tips and Hints
* Always use `.strip()` to remove `\n` from lines. (new line markers)
* Test your functions independently.
'''

import random

# Functions takes in filename parameter and returns list of strings with lines from file
def load_quotes(filename):
    with open(filename, "r") as quote_list:
        lines = quote_list.readlines()
    return [lines.strip() for item in lines]

# Function takes in list of strings and randomly chooses one to return
def get_random_quote(quotes):
    return random.choice(quotes)

def add_to_favorites(filename, random_quote):
    with open(filename, "a") as favorite_quote:
        favorite_quote.write(random_quote.strip() + "\n")

def view_favorites(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

# Runs program. Main() is the only function called so that it calls the other functions appropriately and controls logic flow.
def main():
    quotes = load_quotes("quotes.txt")
    random_quote = get_random_quote(quotes)
    print(f"Quote of the day: {random_quote}")

    choice = input("Do you want to add this quote to favorites? yes/no")
    if choice.lower() == "yes":
        add_to_favorites("favorites.txt", random_quote)
        print("Quote added to favorites!")

    view = input("Do you want to view your favorites? yes/no")
    if view.lower() == "yes":
        view_favorites("favorites.txt")

    return None 

if __name__ == "__main__":  
    main()