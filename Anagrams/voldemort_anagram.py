import sys
from collections import Counter
from itertools import permutations

def load_dictionary(file):
    try:
        with open(file) as f:
            text = f.read().strip().split('\n')
            text = [x.lower() for x in text]
            return text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
        

def main():
    name = 'tmvoordle'
    name = name.lower()
    
    word_list = load_dictionary('words.txt')
    trigrams = load_dictionary('least_likely_trigraphs.txt')
    
    words = prep_words(name, word_list)
    cv_map = cv_map_words(words)
    filter1 = cv_map_filter(name, cv_map)
    filter2 = trigram_filter(filter1, trigrams)
    filter3 = letter_pair_filter(filter2)
    view_by_letter(name, filter3)
    
def prep_words(name, word_list):
    print("Length of initial word list: {}".format(len(word_list)))
    len_name = len(name)
    words = [word.lower() for word in word_list if len(word) == len_name]
    print("Length of new word list: {}".format(len(words)))
    return words

def cv_map_words(words):
    #Maps letters in words to consonants(c)/vowels(v)
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in words:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)
    
    total = len(set(cv_mapped_words))
    target = 0.05
    n = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print("Length filtered CV map: {}".format(len(filtered_cv_map)))
    return filtered_cv_map

def cv_map_filter(name, filtered_cv_map):
    perms = {''.join(i) for i in permutations(name)}
    print("Length of initial permutations set: {}".format(len(perms)))
    vowels = 'aeiouy'
    filter1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter1.add(candidate)
    print("Number of choices after filter 1: {}".format(len(filter1)))
    return filter1

def trigram_filter(filter1, trigrams_filtered):
    filtered = set()
    for candidate in filter1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter2 = filter1 - filtered
    print("Number of choices after filter 2: {}".format(len(filter2)))
    return filter2

def letter_pair_filter(filter2):
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv', 'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    start_letter_rejects = ['ld', 'lm', 'lt', 'lv', 'rd', 'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for start in start_letter_rejects:
            if candidate.startswith(start):
                filtered.add(candidate)
    filter3 = filter2 - filtered
    print("Number of choices after filter 3: {}".format(len(filter3)))
    
    if 'voldemort' in filter3:
        print("Voldemort found!")
    
    return filter3

def view_by_letter(name, filter3):
    print("Remaining Letters: {}".format(name))
    first = input("Select a starting letter or press 'enter' to see all: ")
    subset = []
    for candidate in filter3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print("Number of choices starting fit {}: {}".format(first, len(subset)))
    
    again = input("Go again? (Press enter to continue or 'n' to exit)")
    if again.lower() == '':
        view_by_letter(name, filter3)
    elif again.lower.startswith('n'):
        sys.exit()
    else:
        sys.exit()
        
if __name__ == '__main__':
    main()