import random
from turtle import *
speed(0)
tracer(0)

# COLORS:
    # BLUE PINK GREEN YELLOW RED PURPLE

def mastermind():
    
    #creates the board
    def board():
        color("gray")
        penup()
        setposition(-150,200)
        pendown()
        begin_fill()
        forward(300)
        right(90)
        forward(50)
        right(45)
        forward(50)
        left(45)
        forward(228)
        left(45)
        forward(50)
        right(45)
        forward(50)
        right(90)
        forward(300)
        right(90)
        forward(50)
        right(45)
        forward(50)
        left(45)
        forward(228)
        left(45)
        forward(50)
        right(45)
        forward(50)
        end_fill()
        color("black")
        penup()
        setposition(-70,180)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(-70,90)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(-70,0)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(-70,-90)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(20,180)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(20,90)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(20,0)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(20,-90)
        for i in range(4):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(-70,-180)
        for i in range(2):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        penup()
        setposition(35,-180)
        for i in range(2):
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            right(90)
            penup()
            forward(30)
            right(90)
            forward(15)
            left(90)
        
        right(180)
        penup()
        color("#989898")
        setposition(75,187)
        pendown()
        for i in range(8):
    
            begin_fill()
            circle(5)
            end_fill()
            penup()
            forward(15)
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            penup()
            forward(30)
            pendown()
            
        penup()
        setposition(90,187)
        pendown()
        for i in range(8):
    
            begin_fill()
            circle(5)
            end_fill()
            penup()
            forward(15)
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            penup()
            forward(30)
            pendown()
        
    #calls the board
    board()
    tracer(1)
    
    #Possible colors
    color_list = ["pink","purple","blue","yellow","green","red"]
    
    #four random colors that = answer
    secret = []
    for i in range(4):
        x = random.choice(color_list)
        secret.append(x)
    
    #rules
    print ("The six possible colors: ")
    print ("pink, purple, blue, yellow, green, red")
    print ("Input colors with only a space in between")
    print ("Do not capitalize the color")
    print ("Example input: pink red green blue")
    
    #sets position
    left(90)
    penup()
    setposition(-85,165)
    pendown()
    
    #tracks to see if lose
    count = 0
    
    #sets y value for placement
    y = 0
    
    #loops until user wins or loses
    while True:
        
        #user inputs colors and splits
        colors = input("Give four colors: ")
        colors = colors.split(" ")
                
                
        #makes a copy of the secret list
        secretcopy = []
        for item in secret:
            secretcopy.append(item)
            
        #sets a count to see if user loses   
        count = count + 1
        
        #sets a variable to 0
        ind = 0
        
        #sets the position for the colored circles
        penup()
        setposition(-85,165+y)
        pendown()
    
        #draws the sequence user inputs on the board
        for i in range(4):
            color(colors[ind])
            begin_fill()
            circle(15)
            end_fill()
            penup()
            forward(45)
            pendown()
            ind = ind + 1
        penup()
        backward(180)
        right(90)
        forward(45)
        left(90)
        pendown()
        
        #runs if the user wins
        if colors == secret:
            ind = 0
            penup()
            setposition(-85,-195)
            pendown()
            for i in range(4):
                color(colors[ind])
                begin_fill()
                circle(15)
                end_fill()
                penup()
                forward(45)
                pendown()
                ind = ind + 1
            print ("This is the correct sequence! You win!")
            break
        
        #runs if the user loses
        if count == 8:
            ind = 0
            penup()
            setposition(-85,-195)
            pendown()
            for i in range(4):
                color(secret[ind])
                begin_fill()
                circle(15)
                end_fill()
                penup()
                forward(45)
                pendown()
                ind = ind + 1
            print ("This is the correct sequence! You lose!")
            break
        
        #creates empty lists
        black_list = []
        white_list = []
        poss_white = []
        
        #sets amount of black to 0
        black_count = 0
        
        #loops to see how many black placements there are
        for i in range(len(colors)):
            
            if colors[i] == secretcopy[i]:
                secretcopy[i] = "done"
                black_list.append(colors[i])
                black_count += 1
    
            else:
                poss_white.append(colors[i])
        
        #sets amount of white to 0
        white_count = 0
        #loops to see how many white placements there are
        for colorr in poss_white:
            if colorr in secretcopy:
                secretcopy.remove(colorr)
                white_list.append(colorr)
                white_count += 1
    
        #gets next position ready
        penup()
        setposition(80, 182+y)
        pendown()
        
        # FOUR STATEMENTS BELOW ARE FOR THE BLACK AND WHITE CHIPS
        
        #runs if the user gets no whites or blacks
        if black_count == 0 and white_count == 0:
            y = y - 45
            penup()
            setposition(500,500)
            pendown() 
            continue
        
        #runs if there is one white no blacks
        elif black_count == 0 and white_count >= 1:
            #runs if there are 1 or 2 whites
            if white_count <= 2:
                for i in range(white_count):
                    color("white")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
            
            #runs if there are more than two whites
            else:
                for i in range(2):
                    color("white")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
                for i in range(white_count-2):
                    color("white")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
        
        #runs if there is one black no whites
        elif black_count >= 1 and white_count == 0:
            
            #runs if there are 1 or 2 blacks
            if black_count <= 2:
                for i in range(black_count):
                    color("black")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
            #runs if there are more than 2 blacks
            else:
                for i in range(2):
                    color("black")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
                for i in range(black_count-2):
                    color("black")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
        
        #runs if there is at least one black one white 
        elif black_count >= 1 and white_count >= 1:
            
            #runs if there are 2 whites, two blacks    
            if black_count == 2 and white_count == 2:
                for i in range(2):
                    color("black")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                        
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
                
                for i in range(2):
                    color("white")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
            #runs if there are one of each         
            if black_count == 1 and white_count == 1:
                    
                color("black")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
                
                color("white")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
            #runs if two blacks and one white    
            if black_count == 2 and white_count == 1:  
                for i in range(2):
                    color("black")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                    
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
                
                color("white")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
            #runs if one black and two whites         
            if black_count == 1 and white_count == 2:
                for i in range(2):
                    color("white")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                        
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
    
                color("black")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
            #runs if three blacks one white        
            if black_count == 3 and white_count == 1:
                for i in range(2):
                    color("black")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                        
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
    
                color("black")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
                    
                color("white")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
            #runs if one black 3 white
            if black_count == 1 and white_count == 3:
                    
                for i in range(2):
                    color("white")
                    begin_fill()
                    circle(5)
                    end_fill()
                    penup()
                    forward(15)
                    pendown()
                    
                penup()
                backward(30)
                right(90)
                forward(15)
                left(90)
                pendown()
    
                color("white")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
                    
                color("black")
                begin_fill()
                circle(5)
                end_fill()
                penup()
                forward(15)
                pendown()
    
        #tracks y value for placement
        y = y - 45
        
        #clears turtle
        penup()
        setposition(500,500)
        pendown()
        
mastermind()
