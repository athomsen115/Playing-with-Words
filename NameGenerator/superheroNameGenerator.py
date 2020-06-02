import sys, random, time

def main():
    print('Welcome to the Superhero Name Generator')
    print('Your name might end up awesome, or it might be silly... only time will tell')
    
    with open('firstName.txt') as f:
        first = f.readlines()
    first = [x.strip() for x in first]
    
    with open('lastNames.txt') as f:
        last = f.readlines()
    last = [x.strip() for x in last]
    
    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        
        print("\nYour superhero name is: {} {}".format(first_name, last_name), file=sys.stderr)
        
        time.sleep(1)
        
        newName = input("\nDo you want a different name? (Press enter. To quit press 'n')\n")
        if newName.lower().startswith('n'):
            break

    
if __name__ == '__main__':
    main()
