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

    print(scoredict)
    return scoredict
readScoresFromFile(r"c:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133\Exam_practice\scores.txt")

