import sys
from collections import Counter

def load_dictionary(file):
    try:
        with open(file) as f:
            text = f.read().strip().split('\n')
            text = [x.lower() for x in text]
            return text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
        
def anagram(word_list):
    anagram_list = []
    name = input("Enter a word/name to find its anagrams: ")
    print("Input Word: {}".format(name))
    name = name.lower()
    
    name_sorted = sorted(name)
    for word in word_list:
        word = word.lower()
        if word != name:
            if sorted(word) == name_sorted:
                anagram_list.append(word)
                
    print()
    if len(anagram_list) == 0:
        print("Pick a new word or use a larger dictionary")
    else:
        print("Anagrams: ", *anagram_list, sep='\n')
        
def anagram_phrases(name, word_list):
    
    
    nameLettersCount = Counter(name)
    anagram_list = []
    for word in word_list:
        let = ''
        wordsLettersCount = Counter(word.lower())
        for letter in word:
            if wordsLettersCount[letter] <= nameLettersCount[letter]:
                let += letter
        if Counter(let) == wordsLettersCount:
            anagram_list.append(word)
    
    print("Anagrams: ", *anagram_list,sep='\n')
    print()
    print("Remaining letters: {}".format(name))
    print("Number of remaining letters: {}".format(len(name)))
    print("Number of remaining (real word) anagrams: {}".format(len(anagram_list)))
    
def process_choice(name):
    while True:
        choice = input("Enter some words or press '!' to start over or 'q' to quit: ")
        if choice == '!':
            main()
        elif choice == 'q':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        nameList = list(name)
        for letter in candidate:
            if letter in nameList:
                nameList.remove(letter)
        if len(name) - len(nameList) == len(candidate):
            break
        else:
            print("Won't work! Choose different words")
            
    name = ''.join(nameList)
    return choice, name
    
    
        
def main():
    word_list = load_dictionary('wordlist.txt')
    word_list.append('a')
    word_list.append('i')
    word_list = sorted(word_list)
    
    name = input("Enter a name/phrase: ")
    name = ''.join(name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    run = True
    
    while run:
        temp = phrase.replace(' ', '')
        if len(temp) < limit:
            print("Length of anagram phrase: {}".format(len(temp)))
            
            anagram_phrases(name, word_list)
            print("Current anagram phrase: ", end =" ")
            print(phrase)
            
            choice, name = process_choice(name)
            phrase += choice + ''
        elif len(temp) == limit:
            print("*** FINISHED!!! ***")
            print("Anagram of Name: {}".format(phrase), end=" ")
            print()
            
            playAgain = input("Play Again? (Press 'enter' for yes or 'n' to quit)")
            if playAgain.lower().startswith('n'):
                run = False
                sys.exit()
            else:
                main()        
    
    
if __name__ == '__main__':
    main()
        
        