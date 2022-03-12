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
# Updated:  3/11/2022

Library = ["Pride and Prejudice.txt", "Frankenstein.txt", "The Adventures of Sherlock Holmes.txt", "Alice’s Adventures in Wonderland.txt", "The Great Gatsby.txt", "The Yellow Wallpaper.txt", "A TALE OF TWO CITIES.txt", "Moby-Dick.txt", "Ulysses.txt", "DRACULA.txt"]

# Setting Strings to None to ease debugging and test cases.
Keyword = None
BookSelected = None
KeywordFoundString = None
UserInputString = None
MainMenuString = "Type the keyword you wish to search:" + "\n"
NumberOfBooks = 10
BookFileArray = None

# Build book files into an array
for x in range(NumberOfBooks):
    print(x)
    BookFileArray[x] = BookFileArray[open(Library[x])]

# Class to hold information on the book. 
class BookInfo ():
    Author = None
    Title = None
    Text = None
    
    def getAuthor(cls):
        return Author
    def getTitle(cls):
        return Title
    def getText(cls):
        return Text


# Function to retrieve three lines for three different books from keyword selected based on the user input.
def SearchKeyword(Keyword): 

    # Need an array of book objects
    Books = []

    # Need to use file open 
    #Need to loop through the 10 books to store them in the book object then the book array.
    for x in range(NumberOfBooks):
        print("")    
    
    return print("")


# Prompt user with main menu string, store input into string
UserInputString = input(MainMenuString)

# Print line label and call the SearchKeyword function. 
print("Here's the first result from your keyword: " + "\n" + SearchKeyword(MainMenuString)) 

# Need functions to pull statistics like count, similar words found(Maybe adding widlcards for first and last letter.), and word association web graph.