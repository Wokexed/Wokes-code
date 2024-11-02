# a
def isBinary(digits):

    for n in digits:
        if n not in ['0', '1']:
            
            return False
    
    
    return True

isBinary("12345")
isBinary("001010010")

# b
def toDecimal(binary):
    value = 0
    length = len(binary)
    for i in range(length):
        if binary[i] == "1":
            value += 2**(length - 1 - int(i))
            
    return value

toDecimal("1011")
toDecimal("1110")
toDecimal("100")

# c
def main():
    binarycount = 0
    while True:
        digits = input("Enter binary number: ")
        if isBinary(digits) == False:
            print("Invalid binary number")
            continue
        elif digits == "0":
            print(f"{binarycount} binary numbers converted.")
            break
        else:
            binary = digits
            binarycount += 1

            print(f"{digits} is decimal {int(toDecimal(binary))}" )

main()