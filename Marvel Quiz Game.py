import random
import time

print ()
print("######################################################################")
print ()

#game rules
print ("The topic for this quiz is the Marvel Cinematic Universe (MCU)")
print ("There are 30 different questions, each having one answer")
print ("If the answer to a question is a number, instead of 5, write five")
print ("Unless the question asks for a first name, assume it's first and last")
print ("No answers or questions will be repeated")
print ("Your score will be calculated at the bottom")

#dictionary of questions
dict_questions = {1:"What is spider-man's real name?", 2:"Who was the first avenger?",
             3:"What's Iron Mans real name?", 4:"What is the raccoons name?",
             5:"What is the name of Thor's Hammer?", 6:"Who killed Tony Stark's parents?",
             7:"What type of doctor is Stephen Strange?", 8:"Who uses a bow and arrow?",
             9:"Who's the villian in Ant-Man", 10:"What's Captain America's Shield made of?",
             11:"What hero holds the time stone?", 12:"What's black widow's real name?",
             13:"Who sacrifices themself on Vormir?", 14:"How many infinity stones are there?",
             15:"Where is Captain America from?", 16:"What planet is the soul stone on?",
             17:"What was the first MCU movie?", 18:"What country is black panther from?",
             18:"What country is black panther from?",
             19:"Thor's hammer is made from metal of a dying?",
             20:"What game was Thor playing in Endgame?",
             21:"What's Thor and Loki's sister name?", 22:"How many children does Hawkeye have?",
             23:"Who is the Winter Soldier?", 24:"Who is Thor's love intrest?",
             25:"What hero held a town hostage?", 26:"Who is the main villain in Infinity War?",
             27:"What's the cats name in Captain Marvel?",
             28:"What's Peter Parkers bestfriend's first name?",
             29:"What is the name of the big green hero?", 30:"Who got the Avengers together?"}

#dictionary of answers
dict_answers = {1:"peter parker", 2:"captain america", 3:"tony stark", 4:"rocket", 5:"mjolnir",
           6:"the winter soldier", 7:"neurosurgeon", 8:"hawkeye", 9:"yellowjacket", 10:"vibranium",
           11:"doctor strange", 12:"natasha romanoff",13:"black widow",14:"six", 15:"brooklyn",
           16:"vormir",17:"iron man", 18:"wakanda", 19:"star", 20:"fortnite", 21:"hela", 22:"three",
           23:"bucky barnes",24:"jane foster", 25:"scarlet witch", 26:"thanos", 27:"goose",
           28:"ned", 29:"the hulk",30:"nick fury"}

#Seperates rules
print ()
print("######################################################################")
print ()



#inputs the amount of questions
num_of_questions = input("Do you want 10 questions or all of the questions?: ")

#if input is 10 the amount of question will be 10
if num_of_questions == "10":
    amount = 10
    
#if input is all the amount of question will be 30
elif num_of_questions == "all":
    amount = 30

print ()
print("######################################################################")
print ()


#used for calculating score
total = amount
correct = 0

#keeps track of question user is on
q_on = 1

#sets empty list
old_questions = []

#tracks time
start_time = time.time()

#loops through the amount of questions user wants
for i in range(amount):


    #loops until a new question generates
    while True:
        x = (random.randint(1,30))
        if x not in old_questions:
            break

    #random question
    question = (dict_questions[x])

    #prints the question
    print ("Question " + str(q_on) + ":")
    print (question)

    #user inputs an answer
    answer = input("Your answer: ")

    #makes all letters in answer lowercase
    answer = answer.lower()

    #checks if the answer is correct
    if dict_answers[x] == answer:
        print ("That answer is correct!")
        correct = correct + 1

    #runs if answers wrong
    else:
        print ("That's incorrect, the correct answer is: " + str(dict_answers[x]))

    print ()
    print ("######################################################################")
    print ()

    #keeps track of question user is on
    q_on = q_on + 1

    #adds question to list to prevent repeats
    old_questions.append(x)

#tracks time it ends
end_time = time.time()

#finds the percent
percent = (round((correct/total),4)) * 100

print ()
print ("######################################################################")
print ()

#gets total time
total_time = round((end_time - start_time),3)


#prints how amount correct/incorrect
print ("You got " + str(correct) + "/" + str(total) + " correct")

#prints the percent
print ("That's a " + str(percent) + "%")

#prints the total time
print("Total time taken: " + str(total_time) + " seconds")










#ANSWER KEY BELOW
'''   
1 What is spider-man's real name? Peter Parker
2 Who was the first avenger? Captain America
3 What's Iron Mans real name? Tony Stark
4 What is the raccoons name? Rocket
5 What is the name of Thor's Hammer? Mjolnir
6 Who killed Tony Stark's parents? The Winter Soldier
7 What type of doctor is Stephen Strange? Neurosurgeon
8 Who uses a bow and arrow? Hawkeye
9 Who's the villian in Ant-Man Yellowjacket
10 What's Captain America's Shield made of? Vibranium
11 What hero holds the time stone? Doctor Strange
12 What's black widow's real name? Natasha Romanoff
13 Who sacrifices themself on Vormir? Black Widow
14 How many infinity stones are there? Six
15 Where is Captain America from? Brooklyn
16 What planet is the soul stone on? Vormir
17 What was the first MCU movie? Iron Man
18 What country is black panther from? Wakanda
19 Thor's hammer is made from metal of a dying? Star
20 What game was Thor playing in Endgame? Fortnite
21 What's Thor and Loki's sister name? Hela
22 How many children does Hawkeye have? Three
23 Who is the Winter Soldier? Bucky Barnes
24 Who is Thor's love intrest? Jane Foster
25 What hero held a town hostage? Scarlet Witch
26 Who is the main villain in Infinity War?: Thanos
27 What's the cats name in Captain Marvel? Goose
28 What's Peter Parkers bestfriend's first name? Ned
29 What is the name of the big green hero? The Hulk
30 Who got the Avengers together? Nick Fury
'''
