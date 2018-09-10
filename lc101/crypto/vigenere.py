from helpers import alphabet_position, rotate_character



def encrypt(text,key):
    cipher = ''
    l = len(key)
    idx = 0   #to access key characters
    for i in text:
        if i.isalpha():             #If the character is a alphabet then only rotate it otherwise leave it as it is
            cipher += rotate_character(i,alphabet_position(key[idx])) #get the position of the key's character and rotate the text's character by that amount
            idx = (idx+1)%l   #get the next character of the key
        else:
            cipher += i
    return cipher
def main():
    text = input("Type a message: \n")  
    key = input("Encryption key: \n")
    print(encrypt(text,key))
if __name__ == '__main__':
    main()
