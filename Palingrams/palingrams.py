import sys

def load_dictionary(file):
    try:
        with open(file) as f:
            text = f.read().strip().split('\n')
            text = [x.lower() for x in text]
            return text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)

def dictionary_cleanup(word_list):
    permissible = ("a", "i")
    
    for word in word_list:
        if len(word) == 1 and word not in permissible:
            word_list.remove(word) 

def palindromes(word_list):        
    palindrome_list = []
    
    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)
            
    print("Found {} palindromes".format(len(palindrome_list)))
    #print(*palindrome_list, sep='\n')
    
def palingrams(word_list):
    
    palingram_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        reverse = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reverse[:end-i] and reverse[end-1:] in words:
                    palingram_list.append((word, reverse[end-i:]))
                    #print("{} {}".format(word, reverse[end-i:]))
                if word[:i] == reverse[end-i:] and reverse[:end-i] in words:
                    palingram_list.append((reverse[:end-i], word))
                    #print("{} {}".format(reverse[:end-i], word))
    return palingram_list



def main():
    word_list = load_dictionary('dictionary.txt')
    word_list = dictionary_cleanup(word_list)
    palindromes(word_list)
    palingram = palingrams(word_list)
    sorted_pali = sorted(palingram)
    
    print("Found {} palingrams\n".format((len(sorted_pali))))
    for word1, word2 in sorted_pali:
        print(" {} {}".format(word1, word2))
        
if __name__ == '__main__':
    main()
    
    
    
                    