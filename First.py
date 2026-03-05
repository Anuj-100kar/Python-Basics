import random

def getchoices():
    player_choice=input("enter a choice (rock,paper,scissors): ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def checkWin(player,computer):
    print(f"player choice {player} , computer choice {computer}")
    if(player==computer):
        return "It's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "Rock Smashes Scissors , You Win!"
        else: 
            return "Paper covers rock,You lose"
    
    elif player=="paper":
        if computer=="rock":
            return "Paper Covers Rock, You Win!"
        else: 
            return "Scissors cuts paper, You lose"
        
    elif player=="scissors":
        if computer=="paper":
            return "Scissors cuts paper, You Win!"
        else: 
            return "Rock Smashes Paper, You lose"
    
choices=getchoices()

result=checkWin(choices["player"],choices["computer"])
print(result)

