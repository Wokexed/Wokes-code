import os

def readBallotData(n):
    Liangvotes = 0
    Songvotes = 0
    Thamvotes = 0
    votes = {
        "Liang" : 0,
        "Song" : 0,
        "Tham" : 0
        }
    with open(n) as file:
        for line in file:
            line = line.strip().lower()
            if line == "liang":
                votes["Liang"] +=1
            elif line == "song":
                votes["Song"] += 1
            elif line == "tham":
                votes["Tham"] += 1
    
        return votes

def getElectionWinner(dict):
    
    winner = max(dict, key=dict.get)
    return winner

def writeBallotResult(txt, data):
    names = ["Liang", "Song", "Tham"]
    votes = []
    votes.append(data["Liang"])
    votes.append(data["Song"])
    votes.append(data["Tham"])
    with open(txt, 'w') as file:
        file.write(f"{'Name':<8}{'Votes':>8}\n")
        for name, vote in zip(names,votes):
            file.write(f"{name :<8}{vote :>4}\n")
        winner = max(data, key=data.get)
        file.write("\n")
        file.write(f"Winner is {winner}")

def main():
    ballotData = readBallotData(r"C:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133_Jan2024EQP\ballots.txt")
    winner = getElectionWinner(ballotData)
    print(f"The winner is {winner}")
    writeBallotResult(r"C:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133_Jan2024EQP\result.txt", ballotData)

main()