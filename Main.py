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
# Updated:  2/14/2022

Library = ["Pride and Prejudice", "Frankenstein", "Sherlock Holmes", "Alice in Wonderland", "The Great Gatsby", "The Yellow Wallpaper", "A Tale of Two Cities", "Moby Dick", "Ulysses", "Dracula"]

# Setting Strings to None to ease debugging and test cases.
Keyword = None
BookSelected = None
KeywordFoundString = None
userInputString = None
mainMenuString = None

class BookandPosition():
    def __init__(self, BookName, Position):
        self.BookName = BookName
        self.Position = Position

# Function to retrieve three lines for three different books from keyword selected based on the user input.
def SearchKeyword(Keyword): 

    for x in range(3):
    
PassagesFound = [BookandPosition(BookTitle1,PassageLine), BookandPosition(BookTitle2,PassageLine2)-
# Return a 2D Array of objects (Title, Position) 
return KeywordFoundString


mainMenuString = input("Type the keyword you wish to search:" + "\n")
SearchKeyword(mainMenuString)

# Return the text opened to the first hit
print("Here's the first result from your keyword: " + "\n" + KeywordFound) 

# calling searchkeywprd function will return Warning if an invalid title was inputted.
#   mainMenuString = input("Type the keyword you wish to search" + "\n"