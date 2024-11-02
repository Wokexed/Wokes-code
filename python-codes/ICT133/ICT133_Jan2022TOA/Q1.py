# Qn 1a)

def main(string):
    if len(string) != 8:
        print("invalid")
    elif string[7] not in ["S", "X", "Z"]:
        print("invalid")
    elif string[0].isupper() == False or string[1].isupper() == False or string[2].isupper() == False:
        print("invalid")
    elif not (string[3].isdigit() and string[4].isdigit() and string[5].isdigit() and string[6].isdigit()):   # must use AND 
        print('invalid')
    else:
        print('valid')

main("tWd1234S")
main("TWD1234Z")
main("twdABCDS")
main("tWd1234S")  # Invalid (2 invalid): First 3 characters are not all uppercase
main("TW12345S")  # Invalid (0 invalid): Not 8 characters long
main("TWD1234A")  # Invalid (1 invalid): Last character is not 'S', 'X', or 'Z'
main("TWD12A4S")  # Invalid (3 invalid): Middle characters not all digits
main("TWd1234S")  # Invalid (2 invalid): First 3 characters not all uppercase
main("TWD12XSZ")  # Invalid (3 invalid): Middle characters not all digits
main("TWD1234")   # Invalid (0 invalid): Only 7 characters, last character missing

# 1b)




#Qn 2
