# the Atbash cipher is an encryption method where each letter of a word is replaced with its mirror letter
# e.g., A = Z, B = Y
# create a function that takes a string and applies the Atbash cipher to it
# capitalisation should be retained
# non-alphabetic character should not be altered

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def atbash(txt):
    mirrorTxt = []
    cipher = ''
    for character in txt:
        if character.isalpha():
            index = alphabet.index(character.lower())
            mirror = alphabet[25 - index]
            if character.isupper():
                mirrorTxt.append(mirror.upper())
            else:
                mirrorTxt.append(mirror)
        else:
            mirrorTxt.append(character)
    for character in mirrorTxt:
        cipher += character
    return cipher