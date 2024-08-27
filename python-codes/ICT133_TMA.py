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
#             elif AI > 34000 and AI <= 100000:\
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

# Question 2a
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

# Question 3a)
def factorial1(n):
    product = 1 # Initialize product
    for x in range(1, n + 1):
        product *= x

    print(product)

factorial1(8)

 # Question 3b)
# def factorial2(n: int, lookupTable: list) -> int:




# Question 4
import random

def getPlayers():
    playerlist = []
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    playerlist.append(player1)
    playerlist.append(player2)

    print(playerlist)

def getNewBoard(size):
    print(type(size)) 
    board = [['?' for x in range(size)] for x in range(size)]
    
    treasure_count = (size**2 - 1) // 2   # calculate no. of treasures needed to be planted (integer divison to be used)
    treasures = 0                         # initialize no. of treasures

    while treasures < treasure_count:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] == "?":
            board[row][col] = "*"
            treasures += 1
        
    return board

def printBoard(board):
    size = len(board)
    print("  ", end="")
    for i in range(size):
        print(i, end=" ")
    print()
    
    for i in range(size):
        print(str(i) + " ", end="")
        for j in range(size):
            print(board[i][j], end=" ")
        print()




def main():

    getPlayers()

    while True:
        getSize = int(input("Size of game board: "))
        if getSize >= 5 and getSize % 2 != 0:
            size = int(getSize)
            print(f"Size of board is now set to {getSize}")
            break

        else:
            print("Size of board must be odd and at least 5! ")

    board = getNewBoard(size)
    getNewBoard(board)

main()




def spawnBoard(size):
  print(" ", end=" ")
  for i in range(size):
    print(i, end=" ")
  print("")
  for i in range(size):
    print(str(i) + " ?" * size)

spawnBoard(5)