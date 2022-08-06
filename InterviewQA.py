# Create a function that will take a string as an input and return the 1st unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

def unique(string:str):
    string = string.lower()
    d= {}
    
    for letters in string:
        if letters not in d:
            d[letters] = 1

        else:
            d[letters] +=1
    print(d)

    for k,v in d.items():
        if v==1:
            return k

print(unique('amazon'))
print(unique('Google'))
print(unique('Xoxoxo'))
