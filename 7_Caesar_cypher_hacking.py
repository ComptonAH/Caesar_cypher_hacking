from sys import exit

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    decryption()



def decryption():
    message = input("Enter the message to decrypt:\n>   ")
    for trying in range(26):
        cypher = ''
        for letter in message:
            index = LETTERS.find(letter.upper())
            if index != -1:
                newIndex = (index + trying) if (index + trying) < 26 else (index + trying) % 26
                cypher += LETTERS[newIndex]
            else:
                cypher += ' '
        print(cypher)
    
    

if __name__ == '__main__':
    main()