import random

A = 1
J = 11
Q = 12
K = 13




def getPlayers():
    playerList = []
    while True:
        player1 = input("Enter player 1:")
        player2 = input("Enter player 2:")

        if player1.lower() == player2.lower():
            print("Player names cannot be the same! Please re-enter.")
            continue

        else:
            playerList.append(player1)
            playerList.append(player2)
        
            
        return player1, player2

def getDeck():
    shuffledDeck = []
    Decklist = {
        "Diamond" : ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        "Club" :    ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        "Heart" :   ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        "Spade" :   ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    }
    
    for key, values in Decklist.items():
        for i in values:
            shuffledDeck.append([key, i])
    
    random.shuffle(shuffledDeck)

    return shuffledDeck

def drawCard(shuffledDeck):
    for x in shuffledDeck:
        player1card = shuffledDeck[0]
        player2card = shuffledDeck[1]
        shuffledDeck.pop(0)
        shuffledDeck.pop(0)

    return player1card, player2card

def compareCard(playerA, playerB, playerAcard, playerBcard):
    print(f"{playerA} drew {playerAcard[1]} of {playerAcard[0]}!")
    playerAcard.pop(0)
    print(f"{playerB} drew {playerBcard[1]} of {playerBcard[0]}!") 
    playerBcard.pop(0)

    card_values = {"A": 1, "J": 11, "Q": 12, "K": 13}

game_over = False

while not game_over:
    def main():
        player1, player2 = getPlayers()
        for x in range(0,10):
            shuffledDeck = getDeck()
            player1card, player2card = drawCard(shuffledDeck)
            compareCard(player1, player2, player1card, player2card)
    main()

    again = input("Do you wish to play again? (Y/N) : ")
    if again.lower() == "y":
        continue
    else:
        print("Thanks for playing!")
        game_over = True
    