#type in the input rock, paper or scissors
#hope you enjoy the game 
#if you do hit the like button.
#Thank you :) 
##################ENJOY#####################                                                             
print(" oo_________________________________________________ooo_____oooo_")                          
print(" oo_______ooooo__oo_ooo___ooooo__oo_______o__ooooo___oo____oo____")                                     
print(" oo______oo___oo_ooo___o_oo____o_oo__oo___o_oo___oo__oo___ooooo__")                                           
print(" oo______oo___oo_oo____o_ooooooo_oo__oo___o_oo___oo__oo___oo_____")                                    
print(" oo______oo___oo_oo____o_oo_______oo_oo__o__oo___oo__oo___oo_____")                                                      
print(" ooooooo__ooooo__oo____o__ooooo____oo__oo____ooooo__ooooo_oo_____")                                                      
print(" ________________________________________________________________")                              
import random
userHand = input("Chose between rock,paper or scissors:\n")
computerHand = random.random()

if computerHand <= .33:
    computerHand = "rock"
elif computerHand <= .66:
    computerHand = "paper"
else:
    computerHand = "scissors"
def game(first,second):
    if first == second:
        print("You chose:", first)
        print("Computer chose:", second)
        print("It's a tie")
    elif first == "rock":
        if second == "scissors":
            print("You chose:",first)
            print("Computer chose:", second)
            print("You win!")
        else:
            print("You chose:", first)
            print("Computer chose:", second)
            print("You lose.")
    elif first == "paper":
        if second == "rock":
            print("You chose:", first)
            print("Computer chose:", second)
            print("You win.")
        else:
            print("You chose:", first)
            print("Computer chose:", second)
            print("You lose.")
    elif first == "scissors":
        if second == "paper":
            print("You chose:", first)
            print("Computer chose:", second)
            print("You win.")
        else:
            print("You chose:", first)
            print("Computer chose:", second)
            print("You lose.")

game(userHand,computerHand)
