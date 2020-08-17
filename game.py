#type in the input rock, paper or scissors
#hope you enjoy the game 
#if you do hit the like button.
#Thank you :) 
##################ENJOY#####################                                                             
print(" __          ______		 ____  ____     __       ____   ____           __________ ")                                   
print(" |   |         | 		\		| 	|  |	  |   /	\	|	  |   |    |           |    _______|")                                     
print(" |   |         |     |\	\	  |	 |  |	  |/		\   |      |  |     |          |    |_______")                                           
print(" |   |         |     |   \    \  |	  |  |			/\	\|	  |   |     |          |    _______|")                                    
print(" |   | ____ |     |     \     \|     |  |		 /	 \ 	 	|    |     |____   |     |")                                                      
print(" |           | |     |       \           |  		/  	  \		|    |             |  |     |")                                                      
print("  ------------ |___|        \______|  |___/			\___|     |_______|  |___|")                              
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
