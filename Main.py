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
# An array storing a range of public domain literature



Library = ["Pride and Prejudice", "Frankenstein", "Sherlock Holmes", "Alice in Wonderland", "The Great Gatsby", "The Yellow Wallpaper", "A Tale of Two Cities", "Moby Dick", "Ulysses", "Dracula"]

#User input keyword
Keyword = None

# Returned string after calling SearchBookTitle function.
BookSelected = None

# Returned string after calling SearchKeyword function.
# Return string possibly of section of one piece of literature with the highest count for keyword.
KeywordFoundString = None

# Setting both Strings to None to ease debugging and test cases.
# String holding user input.
userInputString = None

# String acting as the root to Menu navigation and user input.
mainMenuString = None
mainMenuString = input("Type the keyword you wish to search:" + "\n")


# May remove entire function to focus on Keyword search accross all books. 
# Function to retrieve book selected based on the user input.
# what different ways can I use user input to select 1 book. How do I get a simple logical hit. Exact match first vs partial match?
def SearchBookTitle(Keyword): 
    x = 0
    #For loop to compare user input against the titles of the library.
    for x in range(len(Library)) :
        if Keyword == Library[x] :
            return Library[x]

# Function to retrieve keyword selected based on the user input.
def SearchKeyword(Keyword): 
    return KeywordFoundString


# Possibly break menu navigation into a module or function.
userInputString = input("Type the name of the book:" + "\n")

# Call search book title function.
BookSelected = SearchBookTitle(userInputString)

# Return the selected book
print("You selected: " + str(BookSelected))

# Prompt user to input keyword
userInputString = input("Type the keyword you wish to search:" + "\n")

# Call search keyword function
# KeywordFound = SearchKeyword(userInputString)

# Return the text opened to the first hit
print("Here's the first result from your keyword: " + "\n" + KeywordFound) 

# calling searchkeywprd function will return Warning if an invalid title was inputted.
#   mainMenuString = input("Type the keyword you wish to search" + "\n"