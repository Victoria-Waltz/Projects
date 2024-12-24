# Code by Victoria Waltz
import random
from turtle import *

#makes sure turtle draws fast
speed(0)

#function for color box
def box(box_color):
    pendown()
    color(box_color)
    begin_fill()
    for i in range(4):
        forward(40)
        right(90)
    end_fill()
    penup()

# function changes keyboard color
def InsertKeyboardColor():

    letter_positions = {"Q": (-150, -100), "W": (-117, -100), "E": (-79, -100),
    "R": (-51, -100), "T": (-21, -100), "Y": (9, -100), "U": (40, -100),
    "I": (70, -100), "O": (89, -100), "P": (121, -100), "A": (-130, -135),
    "S": (-99, -135), "D": (-72, -135), "F": (-42, -135), "G": (-16, -135),
    "H": (17, -135), "J": (48, -135), "K": (69, -135), "L": (101, -135),
    "Z": (-110, -170), "X": (-81, -170), "C": (-50, -170), "V": (-20, -170),
    "B": (10, -170), "N": (41, -170), "M": (72, -170)}

    position = letter_positions[guess[x]]
    setposition(position)
    write(guess[x], font=("Times New Roman", 25))

#function to move turtle off screen
def moveTurtle():
    penup()
    setposition(10000,10000)
    pendown()

# dict to help with keyboard colors
keyboard = {
    "A": "black", "B": "black", "C": "black", "D": "black", "E": "black", "F": "black", "G": "black", 
    "H": "black", "I": "black", "J": "black", "K": "black", "L": "black", "M": "black", "N": "black", 
    "O": "black", "P": "black", "Q": "black", "R": "black", "S": "black", "T": "black", "U": "black", 
    "V": "black", "W": "black", "X": "black", "Y": "black", "Z": "black"
}

tracer(0)

#creates a "behind the scenes" board
board = []
for i in range(6):
    board.append(["O"]*5)
for row in board:
    print (row)

#creates the boxes on the wordle board
penup()
setposition(-120,215)
pendown()
for i in range(6):
    for i in range(5):
        for i in range(4):
            forward(40)
            right(90)
        penup()
        forward(50)
        pendown()
    penup()
    backward(250)
    right(90)
    forward(45)
    left(90)
    pendown()

# writes the keyboard letters on the wordle board
penup()
setposition(-150,-100)
write("Q W E R T Y U I O P", font=("Times New Roman", 25))
setposition(-130,-135)
write("A S D F G H J K L", font=("Times New Roman", 25))
setposition(-110,-170)
write("Z X C V B N M", font=("Times New Roman", 25))
setposition(-165,-165)
write("[enter]", font=("Times New Roman", 12))
setposition(120,-165)
write("[back]", font=("Times New Roman", 12))

moveTurtle()
tracer(1)

file_name = "WordleWords.txt"

#tries to grab random word from the file words
try:
    with open(file_name, "r") as file: #opens file
        Fwords = file.readlines() #reads the lines in the file
        wordle = list(random.choice(Fwords).upper().strip()) #makes random word uppercase and strips the \n
        
except FileNotFoundError:
    print("Error with opening file")
    exit()

#declares a win check
check_win = False

#declares a loop counter
count = 0

#loops six times
for i in range(6):

    #prompts user to guess a word
    guess = input("Enter your guess: ")

    #runs if the guess is not in the list of real wordle words
    while (guess + "\n") not in Fwords:
        print("Please enter a real word")
        guess = input("Enter your guess: ")

    # makes the guess into a list of uppercases
    guess = list(guess.upper())
    
    #adds the letters to board
    for x in range(5):
        board[i][x] = guess[x]

    #makes check win true if the guess matches the wordle
    if(guess == wordle):
        check_win = True

    #makes a copy of the wordle
    wordle_copy = []
    for letter in wordle:
        wordle_copy.append(letter)

    #checks for greens
    for j in range(5):
        if guess[j] == wordle[j]:
            board[i][j] = "1"
            wordle_copy[j] = "1"

    #checks for yellows
    index = 0
    for letter in guess:
        set_copy = set(wordle_copy)
        oldsize = len(set_copy)
        set_copy.add(letter)
        if oldsize == len(set_copy):
            update_index = wordle_copy.index(letter)
            wordle_copy[update_index]="2"
            board[i][index] = "2"
        index+=1 
    
    for row in board:
        print (row)
        
    penup()
    for x in range(5):

        #gets the positioning of the colored boxes
        xRange, yRange = -120, 215
        setposition(xRange + (x * 50), (yRange - (i*45)))

        # changes colors of boxes and draws on board
        if(board[i][x]) == "1":
            box("light green")
        elif(board[i][x]) == "2":
             box("yellow")
        else:
            box("gray")

        color("black")

    # places guessed words on the board
    penup()
    for x in range(5):

        xRange, yRange = -111, 170
        setposition(xRange + (x * 50), (yRange - (i*45)))

        #places the lettters
        if(guess[x] == "W"):
            backward(6)
            write(guess[x], font=("Times New Roman", 30))
        elif(guess[x] == "I"):
            forward(4)
            write(guess[x], font=("Times New Roman", 30))
        elif(guess[x] == "M"):
            backward(4)
            write(guess[x], font=("Times New Roman", 30))
        else:
            write(guess[x], font=("Times New Roman", 30))

    # loop ensures correct color change on keyboard
    for x in range(5):

        #once green stays green
        if board[i][x] == "1":
            keyboard[guess[x]] = "green"

        # once yellow can change to green
        elif (board[i][x] == "2") and (keyboard[guess[x]] == "black"):
            keyboard[guess[x]] = "yellow"
                    
        elif keyboard[guess[x]] == "black":
            keyboard[guess[x]] = "gray"
                    
        # changes color to the correct one
        color(keyboard[guess[x]])

        # changes color on keyboard
        InsertKeyboardColor()

    #counts through the loop
    count += 1

    #removes the cursor from screen
    moveTurtle()

    #checks to see if user wins
    if(check_win == True):
        print("You win! The wordle was " + "".join(wordle))
        break
    #runs if user loses
    elif(check_win == False and count == 6):
        print("You lose! The wordle was " + "".join(wordle))
        break

