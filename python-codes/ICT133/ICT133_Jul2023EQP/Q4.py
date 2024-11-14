def readBiddingData(filename):
    
# Initialize an empty dictionary
    data_dict = {}

    # Open the file for reading
    with open(filename, 'r') as file:
        for line in file:
            # Strip any extra spaces and split by comma
            nric, value = line.strip().split(', ')
            
            # If the value already exists as a key, append the NRIC to the list
            if value in data_dict:
                data_dict[value].append(nric)
            else:
                # Otherwise, create a new list with the current NRIC
                data_dict[value] = [nric]

    return data_dict

def getSuccessfulBids(biddingData, quota):
    bidprice = []
    high =[]
    for key in biddingData.keys():
        bidprice.append(key)

    bidprice.sort(reverse = True)
    for price in bidprice:
        for w in biddingData[price]:
            high.append(w)
    
    result = high[0:5]
    return result

def writeBiddingResult(filename, result):
    with open(filename, "w") as file:
        for x in result:
            file.write(f"{x}\n")

def main():
    biddingData = readBiddingData(r"C:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133\ICT133_Jul2023EQP\May2023-CatA.txt")
    result = getSuccessfulBids(biddingData, 5)
    writeBiddingResult(r"C:\Users\Ray Lee\OneDrive\Desktop\Repository\Wokes-code\python-codes\ICT133\ICT133_Jul2023EQP\results.txt", result)
main()