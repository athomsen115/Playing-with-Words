import sys, pprint
from collections import defaultdict

def main():
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    text = "The lazy brown fox jumped over the log in mississippi swamp territory"
    
    while True:
        mapped = defaultdict(list)
        for character in text:
            character = character.lower()
            if character in ALPHABET:
                mapped[character].append(character)
                
        print("Sentance is {}".format(text))
        pprint.pprint(mapped, width = 110)
        
        newText = input("Do you want to get a new graph? (press enter to continue or 'n' to quit)")
        if newText.lower().startswith('n'):
            sys.exit()
            
        text = input("Enter your new phrase: ")

if __name__ == '__main__':
    main()