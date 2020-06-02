import sys

def main():
    vowels = 'aeiouy'
    
    while True:
        words = input("Enter a word/phrase to convert to pig latin: ").lower()
        
        pig = []
        for word in words.split(' '):   
            if word[0] in vowels:
                pigLatin = word + 'way'
            else:
                pigLatin = word[1:] + word[0] + 'ay'
            
            pig.append(pigLatin)
        
        print("\nTranslation in pig latin is", end=" ")
        for word in range(len(pig)):
            print(pig[word], end=" ")
        
        newWord = input("\nTranslate a new word? (Press enter to continue or 'n' to quit)")
        
        if newWord.lower().startswith('n'):
            sys.exit()
            
if __name__ == '__main__':
    main()