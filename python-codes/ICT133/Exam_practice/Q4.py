def readScoresFromFile(filename):
    scoredict = {}
    keys = []
    scores = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key = line[0]
            keys.append(line[0])
            for n in line.split():
                if n.isdigit():
                    scores.append(int(n))
            
    
            scoredict[key] = scores
            scores = []

    return scoredict


def inputScore(scoredict):
    gamescore = input("Enter score: ")
    x = gamescore.split()
    team1, score1, team2, score2 = x[0], x[1], x[2], x[3]
    if team1 not in scoredict:
        print(f"Team {team1} does not exist. No scores recorded")
        return
    elif team2 not in scoredict:
        print(f"Team {team2} does not exist. No scores recorded")
        return
    
    if x[1] > x[3]:
        scoredict[x[0]][0] = str(int(scoredict[team1][0]) + 1)
        scoredict[team2][2] = str(int(scoredict[team2][2]) + 1)
    elif x[1] == x[3]:
        scoredict[team1][1] = str(int(scoredict[team1][1]) + 1)
        scoredict[team2][1] = str(int(scoredict[team2][1]) + 1)
    else:
        scoredict[team1][2] = str(int(scoredict[team1][2]) + 1)
        scoredict[team2][0] = str(int(scoredict[team2][0]) + 1)
    return scoredict

def printScoreTable(scoredict):
    
    for keys in scoredict.keys():
        points = (int(scoredict[keys][0]) * 3 + int(scoredict[keys][1]) * 1)
        scoredict[keys] = [str(points)] + scoredict[keys]

    print(f"{'Team':<5} {'Pts':<4} {'W':<3} {'D':<3} {'L':<2}")
    for key, values in scoredict.items():
        pts, wins, draws, loss = values 
        print(f"{key:<5} {pts:<4} {wins:<3} {draws:<3} {loss:<2}")

    return scoredict
    
    
def saveScoresToFile(scoredict):
    with open(r"c:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133\Exam_practice\scores.txt", "w") as file:
        file.write(f"{'Team':<5} {'Pts':<4} {'W':<3} {'D':<3} {'L':<2}\n")
        for key, values in scoredict.items():
            pts, wins, draws, loss = values 
            file.write(f"{key:<5} {pts:<4} {wins:<3} {draws:<3} {loss:<2}\n")

def main():
    print("Menu")
    print("1. Input score table")
    print("2. Print score table")
    print("3. Exit")
    scoredict = readScoresFromFile(r"c:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133\Exam_practice\scores.txt")

    while True:

        option = int(input("Enter option:"))

        if option == 1:
            inputScore(scoredict)
            continue
        elif option == 2:
            printScoreTable(scoredict)
            continue
        elif option == 3:
            saveScoresToFile(scoredict)
            break
        else:
            print("Invalid input, try again.")
            continue

main()


