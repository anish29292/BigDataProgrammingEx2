import random
import time

class Card:
    def __init__(self, name, pace, shooting, passing, dribble, defence, physical):
        self.name = name
        self.pace = pace
        self.shooting = shooting
        self.passing = passing
        self.dribble = dribble
        self.defence = defence
        self.physical = physical

cards = []

cards.append(Card("Cristiano Ronaldo", 90, 93, 81, 90, 35, 79)) 
cards.append(Card("Lionel Messi", 88, 91, 88, 96, 32, 61)) 
cards.append(Card("Neymar Jr.", 92, 84, 83, 95, 32, 59)) 
cards.append(Card("Luka Modric", 76, 76, 90, 91, 70, 67)) 
cards.append(Card("Kevin De Bruyne", 77, 84, 92, 87, 60, 78)) 
cards.append(Card("Eden Hazard", 91, 82, 86, 94, 35, 67)) 
cards.append(Card("Sergio Ramos", 75, 63, 71, 72, 91, 84)) 
cards.append(Card("Luis Suarez", 80, 90, 79, 87, 52, 85)) 
cards.append(Card("Toni Kroos", 67, 82, 89, 82, 74, 69)) 
cards.append(Card("Robert Lewandowski", 78, 89, 75, 85, 41, 82)) 

random.shuffle(cards)

player1_deck = []
player2_deck = []
outdated_deck = []

while len(cards) > 0:
    player1_deck.append(cards.pop(0))
    player2_deck.append(cards.pop(0))

print("*************************************")
print("TRUMP CARDS GAME: Player1 vs Player2!")
print("*************************************")

playerTurn = True

def dice_roll():
    a=random.randint(1,6)
    b=random.randint(1,6)
    global playerTurn
    game_start = input("Player1 press Enter to roll the Dice: ")
    time.sleep(2)
    print("Player1 dice number is: " + str(a))
    game_start = input("Player1 press Enter to roll the Dice: ")
    time.sleep(2)
    print("Player2 dice number is: " + str(b))  
    if a>b:
        print("Player1 gets the first turn to play!")
        playerTurn = True
    elif a<b:
        print("Player2 gets the first turn to play!")
        playerTurn = False
    else:
        print("It's a tie. Please Roll again!")
        dice_roll()
    
dice_roll()

#start the game    

allowedResponses = ["a", "b", "c", "d", "e","f"]
    
godspell_countp1 = 0
godspell_countp2 = 0
resurrectspell_countp1 = 0
resurrectspell_countp2 = 0
p1 = 0
p2 = 0
rspell = "n"
rspell1 = "n"

while len(player1_deck) > 0 and len(player2_deck) > 0:
    
    time.sleep(1)
    if playerTurn == True:
        ra = 0
        if (resurrectspell_countp1 == 0 and len(outdated_deck) > 1 and ra == 0):
            rspell = input("Player1, do you want to cast the Resurrect Spell? (y/n): ")
            if (rspell == "y" and resurrectspell_countp1 == 0):
                random_card = random.randint(1,len(outdated_deck))
                player1_card = outdated_deck.pop(int(random_card)-1)
                outdated_deck.append(player1_card)
                resurrectspell_countp1 = 1
                ra = 1
            else:
                player1_card = player1_deck.pop(0)
                outdated_deck.append(player1_card)
        else:
            player1_card = player1_deck.pop(0)
            outdated_deck.append(player1_card)
        print("*************************************")    
        print("           PLAYER1 CARD")
        print("*************************************")
        print("Name:", player1_card.name)
        print("a. Pace:", player1_card.pace)
        print("b. Shooting:", player1_card.shooting)
        print("c. Passing:", player1_card.passing)
        print("d. Dribbling:", player1_card.dribble)
        print("e. Defence:", player1_card.defence)
        print("f. Physical:", player1_card.physical)
        print("") 
        answer = input("Player1, which attribute of the player do you want to choose? ")
        
        while allowedResponses.count(answer) == 0:
            answer = input("That isn't a valid answer, please try again: ")
        if (godspell_countp1 == 0  and len(player2_deck) > 1 and ra == 0):
            gspell = input("Player1, do you want to cast the God Spell? (y/n): ")
            if (gspell == "y" and godspell_countp1 == 0):
                godspell_countp1 = 1
                print("No of cards in Player2 deck:", len(player2_deck))
                cardno = input("Which card number from Player2 deck? ")
                if (resurrectspell_countp2 == 0 and len(outdated_deck) > 1):
                    rspell1 = input("Player2, do you want to cast the Resurrect Spell? (y/n): ")
                    if (rspell1 == "y" and resurrectspell_countp2 == 0):
                        random_card2 = random.randint(1,len(outdated_deck))
                        res_card = outdated_deck.pop(int(random_card2)-1)
                        player2_deck.insert(0,res_card)
                        print("")
                        print("Player1: ")
                        print("a. Force resurrected card")
                        print("b. Force earlier choice")
                        print("")
                        choice = input("Enter choice :(a/b) ")
                        if (choice == "a"):
                            player2_card = player2_deck.pop(0)
                            outdated_deck.append(player2_card)
                            resurrectspell_countp2 = 1
                        else:    
                            player2_card = player2_deck.pop(int(cardno)-1)
                            outdated_deck.append(player2_card)
                            resurrectspell_countp2 = 1
                    else:
                        player2_card = player2_deck.pop(int(cardno)-1)
                        outdated_deck.append(player2_card)
                else:
                    player2_card = player2_deck.pop(int(cardno)-1)
                    outdated_deck.append(player2_card) 
                    
            else:
                player2_card = player2_deck.pop(0)
                outdated_deck.append(player2_card) 
        
        else:
            player2_card = player2_deck.pop(0)
            outdated_deck.append(player2_card) 
        
        print("*************************************")    
        print("           PLAYER2 CARD")
        print("*************************************")
        print("Name:", player2_card.name)
        print("a. Pace:", player2_card.pace)
        print("b. Shooting:", player2_card.shooting)
        print("c. Passing:", player2_card.passing)
        print("d. Dribbling:", player2_card.dribble)
        print("e. Defence:", player2_card.defence)
        print("f. Physical:", player2_card.physical)
        print("") 
    
    else:
        rb = 0
        if (resurrectspell_countp2 == 0 and len(outdated_deck) > 1 and rb == 0):
            rspell1 = input("Player2, do you want to cast the Resurrect Spell? (y/n): ")
            if (rspell1 == "y" and resurrectspell_countp2 == 0):
                random_card2 = random.randint(1,len(outdated_deck))
                player2_card = outdated_deck.pop(int(random_card2)-1)
                outdated_deck.append(player2_card)
                resurrectspell_countp2 = 1
                rb = 1
            else:
                player2_card = player2_deck.pop(0)
                outdated_deck.append(player2_card)
        else:
            player2_card = player2_deck.pop(0)
            outdated_deck.append(player2_card)
        
       
        print("*************************************")    
        print("           PLAYER2 CARD")
        print("*************************************")
        print("Name:", player2_card.name)
        print("a. Pace:", player2_card.pace)
        print("b. Shooting:", player2_card.shooting)
        print("c. Passing:", player2_card.passing)
        print("d. Dribbling:", player2_card.dribble)
        print("e. Defence:", player2_card.defence)
        print("f. Physical:", player2_card.physical)
        print("") 
        answer = input("Player2, which attribute of the player do you want to choose? ")
        print("Player2 chooses", answer)
        
        if (godspell_countp2 == 0 and len(player1_deck) > 1 and rb == 0):
            gspell1 = input("Player2, do you want to cast the God Spell? (y/n): ")
            if (gspell1 == "y" and godspell_countp2 == 0):
                godspell_countp2 = 1
                print("No of cards in Player1 deck:", len(player1_deck))
                cardno1 = input("Which card number from Player1 deck? ")
                if (resurrectspell_countp1 == 0 and len(outdated_deck) > 1):
                    rspell = input("Player1, do you want to cast the Resurrect Spell? (y/n): ")
                    if (rspell == "y" and resurrectspell_countp1 == 0):
                        random_card = random.randint(1,len(outdated_deck))
                        res_card1 = outdated_deck.pop(int(random_card)-1)
                        player1_deck.insert(0,res_card1)
                        print("")
                        print("Player2: ")
                        print("a. Force resurrected card")
                        print("b. Force earlier choice")
                        print("")
                        choice1 = input("Enter choice :(a/b) ")
                        if (choice1 == "a"):
                            player1_card = player1_deck.pop(0)
                            outdated_deck.append(player1_card)
                            resurrectspell_countp1 = 1
                        else:
                            player1_card = player1_deck.pop(int(cardno1)-1)
                            outdated_deck.append(player1_card)
                            resurrectspell_countp1 = 1
                    else:
                        player1_card = player1_deck.pop(int(cardno1)-1)
                        outdated_deck.append(player1_card)
                else:                 
                    player1_card = player1_deck.pop(int(cardno1)-1)
                    outdated_deck.append(player1_card)
            else:
                player1_card = player1_deck.pop(0)
                outdated_deck.append(player1_card)
        
        else:
            player1_card = player1_deck.pop(0)
            outdated_deck.append(player1_card)
                                   
        print("*************************************")    
        print("           PLAYER1 CARD")
        print("*************************************")
        print("Name:", player1_card.name)
        print("a. Pace:", player1_card.pace)
        print("b. Shooting:", player1_card.shooting)
        print("c. Passing:", player1_card.passing)
        print("d. Dribbling:", player1_card.dribble)
        print("e. Defence:", player1_card.defence)
        print("f. Physical:", player1_card.physical)
        print("") 
    
    playerWins = False
    if answer == "a":
        playerWins = (player1_card.pace > player2_card.pace)
    elif answer == "b":
        playerWins = (player1_card.shooting > player2_card.shooting)
    elif answer == "c":
        playerWins = (player1_card.passing > player2_card.passing)
    elif answer == "d":
        playerWins = (player1_card.dribble > player2_card.dribble)
    elif answer == "e":
        playerWins = (player1_card.defence > player2_card.defence)
    elif answer == "f":
        playerWins = (player1_card.physical > player2_card.physical)
    time.sleep(1)

    if playerWins:
        print("") 
        print("Player1 wins this hand!")
        print("") 
        p1=p1+1      
        playerTurn = True
    else:
        print("")
        print("Player2 wins this hand!")
        print("")
        p2=p2+1
        playerTurn = False
time.sleep(2)

if p1<p2:
    print("*************************************")  
    print("      PLAYER2 WINS THE MATCH !!!!")
    print("*************************************")  
elif p1>p2:
    print("*************************************")  
    print("      PLAYER1 WINS THE MATCH !!!!")
    print("*************************************")  
else:
    print("*************************************")  
    print("            IT'S A TIE!")
    print("*************************************")  
 
time.sleep(2)
print("Player1 total points: ", p1)
print("Player2 total points: ", p2)
print("Total cards in Outdated Deck: ", len(outdated_deck))
print("*************************************")  
print("             GAME OVER")  
print("*************************************")  
time.sleep(2)
