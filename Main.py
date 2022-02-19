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
userInputString = None
mainMenuString = None
mainMenuString = "Type the keyword you wish to search:" + "\n"

class BookandPosition():
    def __init__(self, BookName, Position):
        self.BookName = BookName
        self.Position = Position

# Function to retrieve three lines for three different books from keyword selected based on the user input.
def SearchKeyword(Keyword): 
    BookTitle1 = None
    BookTitle2 = None
    BookTitle3 = None
    PassageLine = None
    PassageLine2 = None
    PassageLine3 = None
    PassagesFound = []

    for x in range(3):
    # Need a function check each word parsed by spaces. Possibility to add partial keywords found, wildcards.
        print("Success")
    
    # Inside or out of loop depending how I build the array on book string at a time.
    PassagesFound = [BookandPosition(BookTitle1,PassageLine), BookandPosition(BookTitle2,PassageLine2), BookandPosition(BookTitle3,PassageLine3)]
    return PassagesFound


# Prompt user with main menu string, store input into string
userInputString = input(mainMenuString)

# Print line label and call the SearchKeyword function. 
print("Here's the first result from your keyword: " + "\n" + SearchKeyword(mainMenuString)) 

#Need functions to pull statistics like count, similar words found(Maybe adding widlcards for first and last letter.), and word association web graph.