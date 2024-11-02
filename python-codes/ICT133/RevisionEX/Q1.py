import math

def getWeight():
    while True:
        weight = int(input("weight(g): "))
        if weight < 0 or weight > 2000:
            continue
        else:
            return weight
def getRate(type, weight):
    price = 0
    if type == "PC":
        return price == 0.30
    if type == "LPP":
        if weight < 20:
            return price == 0.50
        elif weight > 20 and weight < 50:
            return price == 0.70
        elif 