import random

def getTreasureList():
    treasure = [1,1,1,1,1,0,0,0,0,0]
    random.shuffle(treasure)
    return treasure

def countTreasures(treasureList,indices):
    count = 0 
    locationlist = []
    for value in treasureList:
        if value == 1:
            locationlist.append(count)
            count += 1
        else:
            count += 1
    hits = 0
    for i in range(5):
        if indices[i] == locationlist[i]:
            hits += 1

    print(locationlist)
    return hits

def main():
    print("Treasure has been planted... You have 5 tries.")
    print()
    treasureList = getTreasureList()
    round = 1
    while round < 6:
        indices = []
        guess = input(f"Round {round}: Enter your guess:")
        round += 1
        guess = guess.split(",")
        for num in guess:
            num = int(num)
            indices.append(num)
        
        hits = countTreasures(treasureList, indices)
        if hits == 5:
            print(f"You found 5 treasures!!")
            print("You are the winner!!")
            break
        else:
            print(f"You found {hits} treasures!!")
            continue
    if hits < 5:        
        print("You lost!!")
        print(f"The treasures were at: {treasureList}")
main()