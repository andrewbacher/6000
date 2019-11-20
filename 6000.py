#6000
import random

score = 0
#open up the word file
def openfile():
    try:
        infile = open('words.txt','r')
    except IOError:
        print('file not found')
    else:
        target_list = []
        i = 0
        for line in infile:
            new = line.rstrip('\n')
            target_list.append(new)

    return target_list
target_list = openfile()

def choose_word(list):
    i = random.randint(1,(len(list)-1))
    target = list[i]
    return target
target = choose_word(target_list)

def parse(word):
    target_letters = []
    for ch in word:
        target_letters.append(ch)
    return target_letters
target_letters = parse(target)
print(target_letters)

def guess():
    guess = input('Enter a two letter word:')
    while len(guess) != 2:
        print('No that is wrong!')
        guess = input('Enter a two letter word:')
    if len(guess) == 2:
        guess1 = parse(guess)
        return guess1

guess_letters = guess()
print(guess_letters)

def score(target,guess):
    score1 = 0
    for i in range(0,len(target)):
        for j in range(0,len(guess)):
            if guess[j] == target[i]:
                score1 += 250
                if j == i:
                    score1 +=750
                elif j != i:
                    score1 += 0
    return score1

score = score(target_letters,guess_letters)
print(score)

