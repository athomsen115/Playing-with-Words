import sys, re
from collections import defaultdict
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
    word_list = load_dictionary('wordlist.txt')
    name = 'Voldemort' #tmvoordle
    name = name.lower()
    
    diagrams = set()
    perms = {''.join(i) for i in permutations(name)}
    for perm in perms:
        for i in range(0, len(perm) - 1):
            diagrams.add(perm[i] + perm[i + 1])
            
    #print(*diagrams, sep='\n')
    print("Number of diagrams: {}".format(len(diagrams)))
    
    mapped = defaultdict(int)
    for word in word_list:
        word = word.lower()
        for diagram in diagrams:
            for _ in re.finditer(diagram, word):
                mapped[diagram] += 1
    
    print("Diagram Frequency Count")
    for k in mapped:
        print("{} {}".format(k, mapped[k]))
        
if __name__ == "__main__":
    main()
