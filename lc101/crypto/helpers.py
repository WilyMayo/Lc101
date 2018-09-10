
def alphabet_position(letter):
    if letter.isupper():
        return (ord(letter)-65)       #convert character to integer using ASCII code
    else:
        return (ord(letter)-97)
def rotate_character(char,rot):
    pos = (alphabet_position(char)+rot)%26
    new_char = chr(pos+65)          #convert to character using the ASCII code
    if char.islower():              #preserve the case of the character being rotated
        new_char = new_char.lower()
    return new_char