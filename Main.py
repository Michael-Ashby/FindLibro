# FindLibro searches popular public domain literature for keywords. 
# Program currently has 10 public works downloaded onto my PC. 
#
#           Pride and Prejudice     Frankenstein        Sherlock Holmes     
#           Alice in Wonderland     The Great Gatsby    The Yellow Wallpaper
#           A Tale of Two Cities    Moby Dick           Ulysses
#           Dracula            
#
# Michael Ashby
# Start:    2/14/2022
# Updated:  2/18/2022

Library = ["Pride and Prejudice", "Frankenstein", "Sherlock Holmes", "Alice in Wonderland", "The Great Gatsby", "The Yellow Wallpaper", "A Tale of Two Cities", "Moby Dick", "Ulysses", "Dracula"]

# Setting Strings to None to ease debugging and test cases.
Keyword = None
BookSelected = None
KeywordFoundString = None
UserInputString = None
MainMenuString = "Type the keyword you wish to search:" + "\n"
NumberOfBooks = 10

class BookandPosition():
    def __init__(self, BookName, Position):
        self.BookName = BookName
        self.Position = Position

# Function to retrieve three lines for three different books from keyword selected based on the user input.
def SearchKeyword(Keyword): 
    PassagesFound = []

    for x in range(NumberOfBooks):
    # Need a function check each word parsed by spaces. Possibility to add partial keywords found, wildcards.
        print("Ammend List")    
    # Ill need a 2D list that ammends booktitle and the keyword's  index within the passed strings. Is every book going to be its own string? Maybe a List of book strings.
    return print("Success")


# Prompt user with main menu string, store input into string
UserInputString = input(MainMenuString)

# Print line label and call the SearchKeyword function. 
print("Here's the first result from your keyword: " + "\n" + SearchKeyword(MainMenuString)) 

#Need functions to pull statistics like count, similar words found(Maybe adding widlcards for first and last letter.), and word association web graph.