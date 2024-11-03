# Qn 3b
score = [
    [1, 6],
    [2, 3, 1, 6],
    [3, 5, 6],
    [6]
]
w = []
x = len(score)
for i in range(x):
    print("R" + str(int(i + 1)), *score[i])
    w.append(len(score[i]))

print(f"Average number of rolls per round = {sum(w)/x}")