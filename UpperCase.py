string1 = input("Enter a string: ")
def uppercase():
    d = []
    for letters in string1:
        alphabets = letters.isupper()
        if alphabets == True :
            d.append(letters)
            print(letters)

uppercase()