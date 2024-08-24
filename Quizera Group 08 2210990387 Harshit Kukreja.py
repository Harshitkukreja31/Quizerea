#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("**********WELCOME TO QUIZEREA***********")
print("!!!TO START THE GAME ENTER NUMBER OF CONTESTANTS !!!")
##ROUND1
def check_guess1(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
            if attempt == 3:
                print("The Correct answer is ",answer )
n=int(input("enter the number of participants"))
li=[]

for i in range(n):
    li1=[]
    name=input("enter your name")
    li1.append(name)

    score = 0

    print("Guess the Animal")
    count=0
    guess11 = input("Which bear lives at the North Pole? ")
    check_guess1(guess11, "polar bear")
    guess12 = input("Which is the fastest land animal? ")
    check_guess1(guess12, "Cheetah")
    guess13 = input("Which is the larget animal? ")
    check_guess1(guess13, "Blue Whale")
    guess14 = input("Which is the largest bird alive?")
    check_guess1(guess14, "Ostrich")
    guess15 = input("Which is the tallest living animal?")
    check_guess1(guess15,"Giraffe")
    li1.append(score)
    print(name+" Score is "+ str(score))
    li.append(li1)
##PRINTING RESULT OF ROUND1    
print("HERE IS THE RESULT OF ROUND 1")

rows=n
columns=2
for i in range(rows):
    for j in range(columns):
        print(li[i][j],end=" ")
    print()
##PARTICIPANTS ELIGIBLE FOR ROUND2    
print("PARTICIPANTS WHO ARE ELIGIBLE FOR ROUND 2 ARE:")
round2=[]
for i in range(rows):
    for j in range(columns):
        if li[i][1]>=3:
            round2.append(li[i][0])
p=set(round2)
for i in p:
    print(i,end=" ")
    
##ROUND2
print("CONGRATULATIONS!!\nWELCOME TO ROUND2")
print("Instructions for the round 2 are as follows:")
print("1) There are 5 questions in total.")
print("2) Each question carries 1 mark.")
print("3) 1 mark is awarded for each right answer and no mark for wrong answer.")
print("4) 2 attempts are available based on participant's choice")
print("5) 0.5 mark is awarded for right answer in the attempt and 0.5 mark is deducted for each wrong attempt")
def check_guess2(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt <3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt<2:
                print("sorry wrong answer")
                print("click 1 to get more attempt")
                k=int(input())
                if k==1: 
                    guess = input("answer again")
                    score=score-0.5
                else: 
                    print("the correct answer is",answer)
                    break
            attempt=attempt+1
            if attempt==3:
                print("The Correct answer is ",answer )
                
mi=[]
zi=[]
for i in p:
    mi1=[]
    zi1=[]
    mi1.append(i)
    print("its",i+"'s","turn")
    
    score=0
    
    print("Lets explore on India")
    guess21 = input("What is the capital city of India?\na)Bombay b)Jaipur c)Kolkata d)Delhi")
    check_guess2(guess21,"d")
    guess22 = input("What is the national currency of India?\na)Euro b)Dollar c)Rupee d)Pound")
    check_guess2(guess22, "c")
    guess23 = input("Which is the national sport of India?\na)Cricket b)Hockey c)Chess d)Boxing")
    check_guess2(guess23, "b")
    guess24 = input("What is India's national flower?\na)Lotus b)Rose c)Tulip d)Jasmine")
    check_guess2(guess24, "a")
    guess25 = input("Who is known as the father of the nation(India)?\na)Rabindra nath tagore b)Mahatma Gandhi c)Jawahar lal Nehru d)Bhagat singh")
    check_guess2(guess25,"b")
    mi1.append(score)
    print(i+" Score is "+ str(score))
    mi.append(mi1)
    zi1.append(score)
    zi1.append(i)
    zi.append(zi1)
    
    
    
print("HERE IS THE RESULT OF ROUND 2")

count=0
for i in p:
    count=count+1
    
rows=count
columns=2
#mi=final result of the students
for i in range(rows):
    for j in range(columns):
        print(mi[i][j],end=" ")
    print()
    
    
#printing the name of winner
print("ITS TIME TO ANNOUNCE WINNER")
z=max(zi)
for i in range(count):
    if zi[i][0]==z[0]:
        print(zi[i][1],end=" ")
        
        
print("!!!Heartiest Congratulation!!!")
        


      

    
    

    
    


# In[ ]:




