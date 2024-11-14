def getmorse(filename):
    dict = {}
    with open(filename, "r") as file:
        for line in file:
            alphabet, key = line.strip().split(" ")
            dict[key] = alphabet
    return dict

def decode(morsedict, string):
    morselist = []
    morseword = string.split(" ")
    for char in morseword:
        if char in morsedict:
            w = morsedict[char]
            morselist.append(w)

    decodedmsg = " ".join(morselist)
    return decodedmsg

morsedict = getmorse(r"C:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133\exam2024\morse.txt")
decodedmsg = decode(morsedict,"... --- ...")
print(f"Your decoded message is: {decodedmsg}")