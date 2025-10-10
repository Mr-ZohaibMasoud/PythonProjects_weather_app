import random

print("Wellcome to Number Guesser\n")

target = random.randint(1, 10)
print("Enter a Number b/w 1 & 10\nYou have 3 tries")
trie = 3


def NumChecker(target, trie):
    
    num = int(input("Give Number: "))
    
    if trie < 0:
        return

    if num == target:
        print("Hurrah! you are correct")
        return
    else:
        print("Try Again 😁")
        trie = trie - 1
        NumChecker(target , trie)
        
        
NumChecker(target, trie)