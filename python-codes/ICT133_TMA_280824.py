# Question 1a)
# def main():
#     birth_year = int(input("Enter year of birth: "))
#     age = 2025 - birth_year
#     if age < 21:
#         print("You are not eligible for AP cash")
#     else:
#         p = input("Do you own more than 1 property? (Y/N): ")
#         if p == "Y":
#             print("You will receive $200 AP Cash")
#         else:
#             AI = int(input("Assessable Income: "))
#             if AI <= 34000:
#                 print("You will receive $600 AP Cash")
#             elif AI > 34000 and AI <= 100000:
#                 print("You will receive $350 AP Cash")
#             else:
#                 print("You will receive $200 AP Cash")

# main()

# # Question 1b)
# def mainb():
#     birth_year = int(input("Enter year of birth: "))
#     age = 2025 - birth_year
    
#     if age < 21:
#         print("You are not eligible for AP cash")

#  # case 1: not a senior
#     elif 21 <= age < 55:
#         p = input("Do you own more than 1 property? (Y/N): ")
#         if p == "Y":
#             print("You will receive $200 AP Cash")
#         else:
#             AI = int(input("Assessable Income: "))
#             if AI <= 34000:
#                 print("You will receive $600 AP Cash")
#             elif AI > 34000 and AI <= 100000:
#                 print("You will receive $350 AP Cash")
#             else:
#                 print("You will receive $200 AP Cash")

# # case 2: between 55-64
#     elif 55 < age < 65:
#         p1 = input("Do you own more than 1 property? (Y/N): ")
#         if p1 == "Y":
#             print("You will receive $200 AP Cash")
#         else:
#             AI = int(input("Assessable Income: "))
            
#             if AI <= 34000:
#                 AV_home1 = int(input("Annual value of home: "))

#                 if AV_home1 <= 21000:
#                     print("You will receive $600 AP Cash + $250 AP Seniors' Bonus")
#                 elif 21000 < AV_home1 <= 25000:
#                     print("You will receive $600 AP Cash + $200 AP Seniors' Bonus")
#                 else:
#                     print("You will receive $600 AP Cash")
                    
#             elif 34000 < AI <= 100000:
#                 print("You will receive $350 AP Cash")
#             else:
#                 print("You will receive $200 AP Cash")

# # case 3: older than 64
#     else:
#         p2 = input("Do you own more than 1 property? (Y/N): ")
#         if p2 == "Y":
#             print("You will receive $200 AP Cash")
#         else:
#             AI = int(input("Assessable Income: "))

#             if AI <= 34000:
#                 AV_home2 = int(input("Annual value of home: "))

#                 if AV_home2 <= 21000:
#                     print("You will receive $600 AP Cash + $300 AP Seniors' Bonus")
#                 elif AV_home2 > 21000 and AV_home2 <= 25000:
#                     print("You will receive $600 AP Cash + $200 AP Seniors' Bonus")
#                 else:
#                     print("You will receive $600 AP Cash")

#             elif AI > 34000 and AI <= 100000:
#                 print("You will receive $350 AP Cash")
#             else:
#                 print("You will receive $200 AP Cash")

# mainb() 

# # Question 2a
# def isAnagram(word1, word2):
#     word1str = str(word1).lower() # ensures the word is a string and in lower case
#     word2str = str(word2).lower()

#     list1 = list(word1str)
#     list2 = list(word2str)
    
#     list1.sort()
#     list2.sort()

#     if list1 == list2:
#         return True
#     else:
#         return False
    
# print(isAnagram("santa", "Satan"))
# print(isAnagram("santa", "Satay"))

# # Question 2b
# def countVowels(word):
#     wordstr = str(word).lower()
    
#     vowels = 'aeiou'

#     vowelcount = 0

#     for char in wordstr:
#         if char in vowels:
#             vowelcount += 1

#     return vowelcount

# print(countVowels("santA"))
# print(countVowels("SUSS"))
# print(countVowels("shy"))




# # Question 2c

# def countRepeatingChar(word):
#     wordstr = str(word).lower()

#     highest_count = 1
#     seen_letters =[]


#     for x in wordstr:                           # x is the variable of the current letter the function is looping through
#         if x in seen_letters:
#             count = wordstr.count(x)
#             if count > highest_count:
#                 highest_count = count
        
#         else:
#             seen_letters.append(x)

#     return highest_count
        
# print(countRepeatingChar("assistants"))
# print(countRepeatingChar("That"))
# print(countRepeatingChar("business"))
# print(countRepeatingChar("count"))
# print(countRepeatingChar("teacher"))
# print(countRepeatingChar("cheater"))

# # Question 2d
# def main():
#     while True:
#         wordA = str(input("Enter 1st word: "))
#         if wordA == "X" or wordA == "x":
#             print("bye")
#             break
#         else:
#             wordB = str(input("Enter 2nd word: "))
        
#             if isAnagram(wordA, wordB) == False:
#                 print(f"{wordB} is NOT an anagram of {wordA}")
#                 print()
#             elif isAnagram(wordA, wordB) == True:
                
#                 if int(countVowels(wordA)) == int(countVowels(wordB)) == int(countRepeatingChar(wordA)) == int(countRepeatingChar(wordB)):
#                     print(f"{wordB} is a super anagram of {wordA}")
#                     print()
#                 else:
#                     print(f"{wordB} is an anagram of {wordA}")
#                     print()
            
# main()


# # Question 3a)
# def factorial1(n):
#     product = 1 # Initialize product
#     for x in range(1, n + 1):
#         product *= x

#     print(product)

# factorial1(8)

 # Question 3b)
def factorial2(n: int, lookupTable: list) -> int:
    product = 1 # Initialize product
    for x in range(1, n + 1):
        product *= x


factorial2(5,lookupTable)




# Question 4
import random

def getPlayers():
    playerlist = []
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    playerlist.append(player1)
    playerlist.append(player2)

    print(playerlist)
    return playerlist

def getNewBoard(size):
    board = [['?' for x in range(size)] for x in range(size)]
    
    treasure_count = (size ** 2 - 1) // 2   # calculate no. of treasures needed to be planted (integer divison to be used)
    treasures = 0                         # initialize no. of treasures

    while treasures < treasure_count:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] == "?":
            board[row][col] = "x"
            treasures += 1
        
    return board

def printBoard(board, revealed):
    size = len(board)
    print("  ", end="")
    for r in range(size):
        print(r, end=" ")
    print()
    
    for r in range(size):
        print(str(r) + " ", end="")
        for c in range(size):
            # hides the treasures
            if revealed[r][c]:
                print(board[r][c], end=" ")
            else:
                print("?", end=" ")

        print()

def validatePick(player, board, revealed):
    while True:
        try:
            move = input(f"{player}, pick your square:")
            row, col = map(int, move.strip("[]").split("]["))
            if revealed[row][col] == "?":
                print("Square opened!! Please re-enter")
            elif board[row][col]== "x":
                return row, col,  True
            else:
                return row, col, False
        except (ValueError, IndexError):
            print("Invalid input. Please enter coordinates in the form [row][col].")


def main():

    players = getPlayers()

    score = [0, 0]

    current_player = random.randint(0, 1)

    while True:
        getSize = int(input("Size of game board: "))
        if getSize >= 5 and getSize % 2 != 0:
            print(f"Size of board is now set to {getSize}")
            break

        else:
            print("Size of board must be odd and at least 5! ")

    size = getSize
    board = getNewBoard(size)
    revealed = [[False for _ in range(size)] for _ in range(size)]

    treasures_remaining = (size ** 2 - 1) // 2

    while treasures_remaining > 0:
        printBoard(board, revealed)
        row, col, found_treasure = validatePick(current_player, board, revealed)
        
        if found_treasure:
            print("Is a hit!!")
            board[row][col] = "*"  # Mark found treasure with "X"
            score[current_player] += 1
            treasures_remaining -= 1
        else:
            print("No treasure there...")
            board[row][col] = "-"  # Mark missed attempt with "-"
        
        revealed[row][col] = True  # Mark the coor as revealed

        print(f"Current score: {players[0]} ({score[0]}) {players[1]} ({score[1]})")
    
        current_player = 1 - current_player

    printBoard(board, revealed)

    # player 0 wins
    while True:
        if score[0] > (size ** 2 - 1) // 4:
            print(f"Final score: {players[0]} ({score[0]}) {players[1]} ({score[1]})")
            print(f"{players[0]} is the winner!!")
            break
        # player 1 wins
        elif score[1] > (size ** 2 - 1) // 4:
            print(f"Final score: {players[0]} ({score[0]}) {players[1]} ({score[1]})")
            print(f"{players[1]} is the winner!!")
            break
        elif score[0] == score[1] and treasures_remaining < 1:
            print(f"It's a tie!! {players[0]} ({score[0]}) {players[1]} ({score[1]}")
            print("Rematch...")
            continue

 
main()  




