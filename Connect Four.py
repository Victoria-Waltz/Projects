from turtle import *

speed(0)

#creates the board
def connect_board():
    tracer(0)
    #board of cirlces
    pensize(2)
    penup()
    setposition(-200,100)
    for i in range(6):
        for i in range(7):
            penup()
            forward(50)
            pendown()
            circle(25)
        penup()
        backward(350)
        right(90)
        forward(50)
        left(90)
    
    #boarder around the circles
    pensize(3)
    penup()
    forward(25)
    left(90)
    pendown()
    for i in range(3):
        forward(350)
        right(90)
    
    penup()
    right(90)
    forward(50)
    left(90)
    pendown()
    forward(350)
    
    tracer(1)
    
#draws board
connect_board()
penup()
home()

setposition(-500,5000)
pendown()

player_one = input("Give your name, you're player 1: ")
player_two = input("Give your name, you're player 2: ")

#tracks which player is up
player_count = 2

#tracks for placement in rows
count_row_1 = 0
count_row_2 = 0
count_row_3 = 0
count_row_4 = 0
count_row_5 = 0
count_row_6 = 0
count_row_7 = 0

pensize(0.1)
board = []
for i in range(6):
    board.append(["O"]*7)
    


#loops until someone wins
while True:
    
    #see if someone wins to break code
    win = ""
    
    #clears turtle
    penup()
    setposition(1000,1000)
    pendown()
    
    #makes sure input is valid
    try:
        #user inputs a row number between 1 and 7
        row = int(input("What row do you choose? 1-7: "))
        
        #runs if input is not between 1 and 7
        if row > 7 or row < 1:
            print ("MUST BE A # BETWEEN 1-7")

        #checks to see if the row is filled
        if row == 1 and count_row_1 == 6:
            print ("That row is filled, select a new one")
            continue
        elif row == 2 and count_row_2 == 6:
            print ("That row is filled, select a new one")
            continue
        elif row == 3 and count_row_3 == 6:
            print ("That row is filled, select a new one")
            continue
        elif row == 4 and count_row_4 == 6:
            print ("That row is filled, select a new one")
            continue
        elif row == 5 and count_row_5 == 6:
            print ("That row is filled, select a new one")
            continue
        elif row == 6 and count_row_6 == 6:
            print ("That row is filled, select a new one")
            continue
        elif row == 7 and count_row_7 == 6:
            print ("That row is filled, select a new one")
            continue
        
        #checks what player is up
        if player_count % 2 == 0:
            color("#95bb72")
        else:
            color("#D8BFD8")
        
        #counter to alternate colors
        player_count += 1
        
        #places chip in row 1    
        if row == 1:
            
            if count_row_1 == 0:
                penup()
                setposition(-150,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_1 += 1
                
                if player_count % 2 == 0:
                    board[5][0] = "1"
                else:
                    board[5][0] = "2"

                
                
            elif count_row_1 == 1:
                penup()
                setposition(-150,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_1 += 1
                
                if player_count % 2 == 0:
                    board[4][0] = "1"
                else:
                    board[4][0] = "2"
                
    
            elif count_row_1 == 2:
                penup()
                setposition(-150,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_1 += 1
                
                if player_count % 2 == 0:
                    board[3][0] = "1"
                else:
                    board[3][0] = "2"
                
                
    
            elif count_row_1 == 3:
                penup()
                setposition(-150,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_1 += 1
                
                if player_count % 2 == 0:
                    board[2][0] = "1"
                else:
                    board[2][0] = "2"
                
    
            elif count_row_1 == 4:
                penup()
                setposition(-150,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_1 += 1
                
                if player_count % 2 == 0:
                    board[1][0] = "1"
                else:
                    board[1][0] = "2"
                
                
            elif count_row_1 == 5:
                penup()
                setposition(-150,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_1 += 1
                
                if player_count % 2 == 0:
                    board[0][0] = "1"
                else:
                    board[0][0] = "2"

        #places chip in row 2
        if row == 2:
    
            if count_row_2 == 0:
                penup()
                setposition(-100,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_2 += 1
                
                if player_count % 2 == 0:
                    board[5][1] = "1"
                else:
                    board[5][1] = "2"
                
                
                
            elif count_row_2 == 1:
                penup()
                setposition(-100,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_2 += 1
                
                if player_count % 2 == 0:
                    board[4][1] = "1"
                else:
                    board[4][1] = "2"
                    
                
    
            elif count_row_2 == 2:
                penup()
                setposition(-100,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_2 += 1
                
                if player_count % 2 == 0:
                    board[3][1] = "1"
                else:
                    board[3][1] = "2"
                    
                
    
            elif count_row_2 == 3:
                penup()
                setposition(-100,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_2 += 1
                
                if player_count % 2 == 0:
                    board[2][1] = "1"
                else:
                    board[2][1] = "2"
                
                
    
            elif count_row_2 == 4:
                penup()
                setposition(-100,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_2 += 1
                
                if player_count % 2 == 0:
                    board[1][1] = "1"
                else:
                    board[1][1] = "2"
                
                
            elif count_row_2 == 5:
                penup()
                setposition(-100,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_2 += 1
                if player_count % 2 == 0:
                    board[0][1] = "1"
                else:
                    board[0][1] = "2"

        #places chip in row 3   
        if row == 3:
    
            if count_row_3 == 0:
                penup()
                setposition(-50,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_3 += 1
                if player_count % 2 == 0:
                    board[5][2] = "1"
                else:
                    board[5][2] = "2"
                
                
            elif count_row_3 == 1:
                penup()
                setposition(-50,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_3 += 1
                if player_count % 2 == 0:
                    board[4][2] = "1"
                else:
                    board[4][2] = "2"
                
    
            elif count_row_3 == 2:
                penup()
                setposition(-50,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_3 += 1
                if player_count % 2 == 0:
                    board[3][2] = "1"
                else:
                    board[3][2] = "2"
                
    
            elif count_row_3 == 3:
                penup()
                setposition(-50,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_3 += 1
                if player_count % 2 == 0:
                    board[2][2] = "1"
                else:
                    board[2][2] = "2"
                
    
            elif count_row_3 == 4:
                penup()
                setposition(-50,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_3 += 1
                if player_count % 2 == 0:
                    board[1][2] = "1"
                else:
                    board[1][2] = "2"
                
                
            elif count_row_3 == 5:
                penup()
                setposition(-50,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_3 += 1
                if player_count % 2 == 0:
                    board[0][2] = "1"
                else:
                    board[0][2] = "2"
               
        #places chip in row 4    
        if row == 4:
            if count_row_4 == 0:
                penup()
                setposition(0,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_4 += 1
                if player_count % 2 == 0:
                    board[5][3] = "1"
                else:
                    board[5][3] = "2"
                
                
            elif count_row_4 == 1:
                penup()
                setposition(0,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_4 += 1
                if player_count % 2 == 0:
                    board[4][3] = "1"
                else:
                    board[4][3] = "2"
                
    
            elif count_row_4 == 2:
                penup()
                setposition(0,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_4 += 1
                if player_count % 2 == 0:
                    board[3][3] = "1"
                else:
                    board[3][3] = "2"
                
    
            elif count_row_4 == 3:
                penup()
                setposition(0,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_4 += 1
                if player_count % 2 == 0:
                    board[2][3] = "1"
                else:
                    board[2][3] = "2"
                
    
            elif count_row_4 == 4:
                penup()
                setposition(0,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_4 += 1
                if player_count % 2 == 0:
                    board[1][3] = "1"
                else:
                    board[1][3] = "2"
                
                
            elif count_row_4 == 5:
                penup()
                setposition(0,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_4 += 1
                if player_count % 2 == 0:
                    board[0][3] = "1"
                else:
                    board[0][3] = "2"
                
        #places chip in row 5
        if row == 5:
            if count_row_5 == 0:
                penup()
                setposition(50,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_5 += 1
                if player_count % 2 == 0:
                    board[5][4] = "1"
                else:
                    board[5][4] = "2"
                
                
            elif count_row_5 == 1:
                penup()
                setposition(50,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_5 += 1
                if player_count % 2 == 0:
                    board[4][4] = "1"
                else:
                    board[4][4] = "2"
                
    
            elif count_row_5 == 2:
                penup()
                setposition(50,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_5 += 1
                if player_count % 2 == 0:
                    board[3][4] = "1"
                else:
                    board[3][4] = "2"
                
    
            elif count_row_5 == 3:
                penup()
                setposition(50,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_5 += 1
                if player_count % 2 == 0:
                    board[2][4] = "1"
                else:
                    board[2][4] = "2"
                
    
            elif count_row_5 == 4:
                penup()
                setposition(50,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_5 += 1
                if player_count % 2 == 0:
                    board[1][4] = "1"
                else:
                    board[1][4] = "2"
                
                
            elif count_row_5 == 5:
                penup()
                setposition(50,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_5 += 1
                if player_count % 2 == 0:
                    board[0][4] = "1"
                else:
                    board[0][4] = "2"
                
        #places chip in row 6
        if row == 6:
            if count_row_6 == 0:
                penup()
                setposition(100,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_6 += 1
                if player_count % 2 == 0:
                    board[5][5] = "1"
                else:
                    board[5][5] = "2"
                
                
            elif count_row_6 == 1:
                penup()
                setposition(100,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_6 += 1
                if player_count % 2 == 0:
                    board[4][5] = "1"
                else:
                    board[4][5] = "2"
                
    
            elif count_row_6 == 2:
                penup()
                setposition(100,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_6 += 1
                if player_count % 2 == 0:
                    board[3][5] = "1"
                else:
                    board[3][5] = "2"
                
    
            elif count_row_6 == 3:
                penup()
                setposition(100,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_6 += 1
                if player_count % 2 == 0:
                    board[2][5] = "1"
                else:
                    board[2][5] = "2"
                
    
            elif count_row_6 == 4:
                penup()
                setposition(100,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_6 += 1
                if player_count % 2 == 0:
                    board[1][5] = "1"
                else:
                    board[1][5] = "2"
                
                
            elif count_row_6 == 5:
                penup()
                setposition(100,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_6 += 1
                if player_count % 2 == 0:
                    board[0][5] = "1"
                else:
                    board[0][5] = "2"
                
        #places chip in row 7    
        if row == 7:
            if count_row_7 == 0:
                penup()
                setposition(150,-150)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_7 += 1
                if player_count % 2 == 0:
                    board[5][6] = "1"
                else:
                    board[5][6] = "2"
                
                
            elif count_row_7 == 1:
                penup()
                setposition(150,-100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_7 += 1
                if player_count % 2 == 0:
                    board[4][6] = "1"
                else:
                    board[4][6] = "2"
                
    
            elif count_row_7 == 2:
                penup()
                setposition(150,-50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_7 += 1
                if player_count % 2 == 0:
                    board[3][6] = "1"
                else:
                    board[3][6] = "2"
                
    
            elif count_row_7 == 3:
                penup()
                setposition(150,0)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_7 += 1
                if player_count % 2 == 0:
                    board[2][6] = "1"
                else:
                    board[2][6] = "2"
                
    
            elif count_row_7 == 4:
                penup()
                setposition(150,50)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_7 += 1
                if player_count % 2 == 0:
                    board[1][6] = "1"
                else:
                    board[1][6] = "2"
                
                
            elif count_row_7 == 5:
                penup()
                setposition(150,100)
                pendown()
                begin_fill()
                circle(25)
                end_fill()
                count_row_7 += 1
                if player_count % 2 == 0:
                    board[0][6] = "1"
                else:
                    board[0][6] = "2"
        

        
        #Checks for horizontal wins   
        for row in board:
            check = "".join(row)
        
            if "1111" in check:
                win = "done"
                print
                print (player_two + " wins!")
                break
            elif "2222" in check:
                win = "done"
                print
                print (player_one + " wins!")
                break
            
        # Checks for vertical wins
        for i in range(7):
            for j in range(3):
                check = "".join([board[j + k][i] for k in range(4)])
        
                if "1111" in check:
                    win = "done"
                    print(player_two + " wins!")
                    break
                elif "2222" in check:
                    win = "done"
                    print(player_one + " wins!")
                    break

        # Checks for diagonal wins (bottom-left to top-right)
        for i in range(3):
            for j in range(4):
                check = "".join([board[i + k][j + k] for k in range(4)])
                
                if "1111" in check:
                    win = "done"
                    print(player_two + " wins diagonally!")
                    break
                elif "2222" in check:
                    win = "done"
                    print(player_one + " wins diagonally!")
                    break
        
        # Checks for diagonal wins (bottom-right to top-left)
        for i in range(3):
            for j in range(6, 2, -1):
                check = "".join([board[i + k][j - k] for k in range(4)])
                
                if "1111" in check:
                    win = "done"
                    print(player_two + " wins diagonally!")
                    break
                elif "2222" in check:
                    win = "done"
                    print(player_one + " wins diagonally!")
                    break

            
        if win == "done":
            break
        


    #runs if input isn't a number
    except:
        print("Must be a number")
        
        
