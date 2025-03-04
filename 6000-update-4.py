# 6000 is a game where you try to figure out a six letter word by making and then receiving feedback on word guesses
# (first two letter, then three, four, five, and finally six letter word guesses)

# 250 points are awarded for a letter guessed that is in the target word but not in the correct place
# 1000 points are awarded for a letter guessed that is in the target word and IS in the correct place

# Consider the example target word of 'mitten' and guess word 'eat'

# In this example, 250 points are awarded for the letter 'e' in 'eat' because 'e' is in 'mitten', however
# because 'e' is in the 1st position in 'eat' and the 5th position in 'mitten' no further points are given

# no points are awarded for 'a' in 'eat' because 'a' is not in 'mitten'

# 1000 points are awarded for 't' in 'eat' because 't' is in 'mitten' and it is in the 3rd spot in both words

# therefore, the total score awarded for the guess 'eat' would be 1250

# There is some debate about the following:
# because there is a 2nd 't' in the word 'mitten', some feel that the player should be given a score for that letter too
# which would result in 1250 points being awarded for the 't' alone, because it appears twice in mitten and one of the
# appearances is in the same spot as it is in the guess word

# One other thing to note:
# Consider the guess word 'eel' was chosen for the same target word 'mitten'
# In this case, both 'e's in 'eel' are counted and scored, giving the player an awarded score of 500

######################################### DEFINING FUNCTIONS ###########################################################

import sys # This is used to cancel out of the program after the game is over
import os # This is used to clear the command prompt window everytime a guess is made
import random # used to assign the target word from the target_list

guess_count = 1 # number of guess player is currently on
guess_letter_count = 0 # number of letters required for the current guess
num_offset = 0 # used for setting the number of blank spaces in front of the guess word to line up guesses 3-7 and 10
               # i.e. in the third guess this is set to 1 so the first letter is in the second spot

def openfile(file): #openfile function is now a universal file opener, it just requires the name of the file when called
    try:
        infile = open(file,'r') #read words from specified file
    except IOError:
        print('file not found')
    else:
        word_list = [] #create list to hold words read from file
        for line in infile: # for every line in the file, containing a word and a new line ('\n')
            new = line.rstrip('\n') # strip off the new line ('\n') at the end of the word
            word_list.append(new) # add the word in 'new' to the 'word_list'
        return word_list

def choose_target_word(list): #function to assign the target word
    i = random.randint(1,(len(list)-1))
    target = list[i] #assign target word as a random word from the target word list
    return target

def parse(word): #function to separate characters in a word (target or guess)
    word_letters = [] #create list of letters in the target word
    for ch in word:
        word_letters.append(ch)
    return word_letters

#======================================== GUESSING FUNCTION ============================================================

def guess (glc, check, g_c , n_o): #function to make guess, glc is guess_letter_count, g_c is guess_count, n_o is num_offset

    current_glc = 2 + glc # defines the number of letters needed in this guess (add to count to increase this amount)
    correct = False # correct is a boolean variable that will return true when the guess is verified to be an actual word
                    # ??? but this never happens? which works because the function terminates as soon as it 'return's
                    # valid guess, but not sure it was what you intended?

    while correct == False:
        print('\nGuess',g_c,'- Enter a',current_glc,'letter word:')
        guess = input('') #user input

        while len(guess) != current_glc: # if guess is < or > the amount of letters required for current guess...
            print('That is the wrong amount of letters. Enter a',current_glc,'letter word:')
            guess = input('') # ...reiterate the input function

        for i in range(0,len(check)): # check every word in the check list
            if guess == check[i]: # If a match is found, add the appropriate offset to line up in the grid
                                  # then return the word as a list of its letters

                while n_o > 0:  # while num_offset is greater than zero, add a # in front of the word to offset it
                    guess = "#" + guess
                    n_o -= 1

                valid_guess = parse(guess)
                return valid_guess

        else: # if no match is found in the check list
            print('Your guess is not an English word. Try again')

#======================================== SCORING FUNCTION =============================================================

#--------------------------------------- ANJ'S SCORE 1000S FIRST SOLUTION ----------------------------------------------
#--------------------------------------- THIS IS A NEW AND...FRESH SOLUTION --------------------------------------------

def score(target, guess): #function to compare target word and guess word letters and allot points based on matches

    score = 0
    temp_target = target[:] # created to modify the items in the target letter list without actually modifying them as
                            # the original list still needs to be used to score all other guesses
    temp_guess = guess[:] # same as above, but for guess. This is so that the guess letters can be properly printed in
                          # the guess_grid

    for i in range(0, len(temp_guess)):
        if temp_guess[i] in temp_target:
            if temp_guess[i] == temp_target[i]:
                score += 1000
                temp_target[i] = '-'
                temp_guess[i] = '_'
    for i in range(0, len(temp_guess)):
        if temp_guess[i] in temp_target:
            for j in range(0, len(temp_target)):
                if temp_guess[i] == temp_target[j]:
                    score += 250
                    temp_target[j] = '-'
                    temp_guess[i] = '_'

    return score

#---------------------------------------- THE POT_DOUB TRAVESTY --------------------------------------------------------
#---------------------------------------- THIS SOLUTION IS TO BE TUCKED AWAY -------------------------------------------
#---------------------------------------- NEVER TO BE USED AGAIN -------------------------------------------------------

    #pot_doub = [] # potential double letters list
    #con_doub = [] # confirmed doubles list

    #pass_through = 0

    #for j in range(0, len(temp_guess)): # checks every letter in the guess word

        #pot_doub = [] # have to reinitiate pot_doub here to avoid doubles from previous guesses causing extra substractions

        #for i in range(0, len(temp_target)):  # ...against every letter in target word

            #pass_through += 1 # matching passes for testing purposes only
            #print('\nPass', pass_through, end=' - ')

            #if temp_guess[j] == temp_target[i]:
                #score += 250 # matches are awarded 250 points
                #if j == i:
                    #score += 750 # exact matches are awarded an additional 750

                #if temp_target[i] in pot_doub: # if a match is already in the pot_doub list, add it to the con_doub list
                    #con_doub.append(temp_target[i])

                    #pot_doub.append(temp_target[i])

                    #score = score -250 # for every letter added to the con_doub list, subtract 250 points

                    #print('pot_doub:', pot_doub, '| con_doub:', con_doub, '| Score - 250 =', score) # printing pot_doub
                        # for testing purposes only

                #else:
                    #pot_doub.append(temp_target[i]) # if it's not already in pot_doub list, add it in

                    #temp_target[i] = '-'
                    #print('pot_doub:', pot_doub, ' | con_doub:', con_doub, '| Score:', score) # for testing purposes only

                #print('Guess letter:', temp_guess[j]) # for testing purposes only

    #return score

#======================================= VISUAL ELEMENT ================================================================

guess1 = '  '.join(['_','_','#','#','#','#'])
guess2 = '  '.join(['_','_','_','#','#','#'])
guess3 = '  '.join(['#','_','_','_','#','#'])
guess4 = '  '.join(['#','#','_','_','_','#'])
guess5 = '  '.join(['#','#','#','_','_','_'])
guess6 = '  '.join(['#','#','_','_','_','_'])
guess7 = '  '.join(['#','_','_','_','_','#'])
guess8 = '  '.join(['_','_','_','_','#','#'])
guess9 = '  '.join(['_','_','_','_','_','#'])
guess10 = '  '.join(['#','_','_','_','_','_'])
guess11 = '  '.join(['_','_','_','_','_','_'])
guess12 = '  '.join(['_','_','_','_','_','_'])

score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score7 = 0
score8 = 0
score9 = 0
score10 = 0
score11 = 0
score12 = 0

#----------------------- FUNCTION TO BUILD GUESS GRID ------------------------------------------------------------------

def build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                    guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12):
    guess_grid = [[guess1,score1],
                  [guess2,score2],
                  [guess3,score3],
                  [guess4,score4],
                  [guess5,score5],
                  [guess6,score6],
                  [guess7,score7],
                  [guess8,score8],
                  [guess9,score9],
                  [guess10,score10],
                  [guess11,score11],
                  [guess12,score12]
                 ]

    print('1000 points - Correct letter & Correct position\n'
          '250 points - Correct letter & Incorrect position\n')

    # for testing purposes
    #upper_target_letters = []
    #for ch in target_letters:
    #    upper_target_letters.append(ch.upper())
    #print(' ', '  '.join(upper_target_letters))


    for item in guess_grid:
        print('|',item[0],'| Score:', item[1])

################################## CALLING FUNCTIONS ###################################################################

os.system('cls')

print('                      ', '6000.py')


print('\n6000 is a game where you try to figure out a six letter word by making\n'
      'and then receiving points for word guesses\n'
      '(first two letter, then three, four, five, and finally six letter word guesses)\n')

target_list = openfile('6letterEasy.txt') #create target word list forms words.txt

target = choose_target_word(target_list) #choose target word from list

# target = 'banana' # for testing triples

target_letters = parse(target) #separate letters out in target word

# Reveal is for displaying target word at the end of the game, this code visualized it the same way as the guess grid
reveal = '--------------------------------\n| '+target_letters[0].upper()+'  '+target_letters[1].upper()+'  '+target_letters[2].upper()+'  '+target_letters[3].upper()+'  '+target_letters[4].upper()+'  '+target_letters[5].upper()+' |'

print(reveal) # for testing purposes only

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

#======================================== GUESS 1 ======================================================================

# Open two letter words file
two_letter_list = openfile('2letter.txt') #create 2 letter word list

guess1_letters = guess(guess_letter_count,two_letter_list, guess_count, num_offset) #accept user input of guess word
                                                                                    # and then separate letters out
                                                                                    # in guess word
guess_letter_count += 1 # add 1 to the glc, required letters becomes 3

#updating guess1 for the visual element
guess1 = '  '.join([guess1_letters[0].upper(),guess1_letters[1].upper(),'#','#','#','#'])

#clears the screen and makes two enters for visibility
os.system('cls')

score1 = score(target_letters,guess1_letters) #compare target and guess letters and allot points

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 2 ======================================================================

# Open three letter words file
three_letter_list = openfile('3letter.txt') #create 3 letter word list

# repeat steps, but now with three letters instead of two
guess2_letters = guess(guess_letter_count,three_letter_list, guess_count, num_offset)

guess2 = '  '.join([guess2_letters[0].upper(),guess2_letters[1].upper(), guess2_letters[2].upper(), '#','#','#'])

os.system('cls')

score2 = score(target_letters,guess2_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 3 ======================================================================

num_offset = 1 # setting offset to 1 for guess 3

guess3_letters = guess(guess_letter_count, three_letter_list, guess_count, num_offset)

guess3 = '  '.join([guess3_letters[0],guess3_letters[1].upper(), guess3_letters[2].upper(), guess3_letters[3].upper(),'#','#'])

os.system('cls')

score3 = score(target_letters, guess3_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 4 ======================================================================

num_offset = 2 # setting offset to 2 for guess 4

guess4_letters = guess(guess_letter_count, three_letter_list, guess_count, num_offset)

guess4 = '  '.join([guess4_letters[0],guess4_letters[1], guess4_letters[2].upper(), guess4_letters[3].upper(),
                    guess4_letters[4].upper(),'#'])

os.system('cls')

score4 = score(target_letters, guess4_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 5 ======================================================================

num_offset = 3 # setting offset to 3 for guess 5

guess5_letters = guess(guess_letter_count, three_letter_list, guess_count, num_offset)
guess_letter_count += 1 # going from 3 letter word guesses to 4

guess5 = '  '.join([guess5_letters[0],guess5_letters[1], guess5_letters[2], guess5_letters[3].upper(),
                    guess5_letters[4].upper(),guess5_letters[5].upper()])

os.system('cls')

score5 = score(target_letters, guess5_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 6 ======================================================================

num_offset = 2 # setting offset to 2 for guess 6

# Open four letter words file
four_letter_list = openfile('4letter.txt') #create 4 letter word list

guess6_letters = guess(guess_letter_count, four_letter_list, guess_count, num_offset)

guess6 = '  '.join([guess6_letters[0],guess6_letters[1], guess6_letters[2].upper(), guess6_letters[3].upper(),
                    guess6_letters[4].upper(),guess6_letters[5].upper()])

os.system('cls')

score6 = score(target_letters, guess6_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 7 ======================================================================

num_offset = 1 # setting offset to 1 for guess 7

guess7_letters = guess(guess_letter_count, four_letter_list, guess_count, num_offset)

guess7 = '  '.join([guess7_letters[0],guess7_letters[1].upper(), guess7_letters[2].upper(), guess7_letters[3].upper(),
                    guess7_letters[4].upper(),'#'])

os.system('cls')

score7 = score(target_letters, guess7_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 8 ======================================================================

num_offset = 0 # setting offset to 0 for guess 8

guess8_letters = guess(guess_letter_count, four_letter_list, guess_count, num_offset)
guess_letter_count += 1 # going from 4 letter guess words to 5

guess8 = '  '.join([guess8_letters[0].upper(),guess8_letters[1].upper(), guess8_letters[2].upper(), guess8_letters[3].upper(),
                    '#','#'])

os.system('cls')

score8 = score(target_letters, guess8_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 9 ======================================================================

num_offset = 0 # setting offset to 0 for guess 9

# Open five letter words file
five_letter_list = openfile('5letter.txt') #create 5 letter word list

guess9_letters = guess(guess_letter_count, five_letter_list, guess_count, num_offset)

guess9 = '  '.join([guess9_letters[0].upper(),guess9_letters[1].upper(), guess9_letters[2].upper(), guess9_letters[3].upper(),
                    guess9_letters[4].upper(),'#'])

os.system('cls')

score9 = score(target_letters, guess9_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 10 =====================================================================

num_offset = 1 # setting offset to 1 for guess 10

guess10_letters = guess(guess_letter_count, five_letter_list, guess_count, num_offset)
guess_letter_count += 1 # going from 5 letter guess words to 6

guess10 = '  '.join([guess10_letters[0],guess10_letters[1].upper(), guess10_letters[2].upper(), guess10_letters[3].upper(),
                    guess10_letters[4].upper(),guess10_letters[5].upper()])

os.system('cls')

score10 = score(target_letters, guess10_letters)

print('\n')

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 11 =====================================================================

num_offset = 0 # setting offset to 0 for guess 11

six_letter_list = openfile('6letterEasy.txt') #create 6 letter word list

guess11_letters = guess(guess_letter_count, six_letter_list, guess_count, num_offset)

guess11 = '  '.join([guess11_letters[0].upper(),guess11_letters[1].upper(), guess11_letters[2].upper(), guess11_letters[3].upper(),
                    guess11_letters[4].upper(),guess11_letters[5].upper()])

os.system('cls')

score11 = score(target_letters, guess11_letters)

print('\n')

#---------------------------------------- WINNING LOGIC ----------------------------------------------------------------

if score11 >= 6000:
    build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6,
                     score6, guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11,
                     guess12, score12)
    reveal = '| '+target_letters[0].upper()+'  '+target_letters[1].upper()+'  '+target_letters[2].upper()+'  '+target_letters[3].upper()+'  '+target_letters[4].upper()+'  '+target_letters[5].upper()+' |'
    
    print(reveal) # prints the target word in the format of the guess grid
    print('\nWINNER! 6000 master are you. And quick too!')

    sys.exit()

#-----------------------------------------------------------------------------------------------------------------------

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)

guess_count+=1

#======================================== GUESS 12 =====================================================================

num_offset = 0 # setting offset to 0 for guess 12

guess12_letters = guess(guess_letter_count, six_letter_list, guess_count, num_offset)

guess12 = '  '.join([guess12_letters[0].upper(),guess12_letters[1].upper(), guess12_letters[2].upper(), guess12_letters[3].upper(),
                    guess12_letters[4].upper(),guess12_letters[5].upper()])

os.system('cls')

score12 = score(target_letters, guess12_letters)

print('\n')

#-------------------------------------- WINNING LOGIC ------------------------------------------------------------------

if score12 >= 6000:
    build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6,
                     score6, guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11,
                     guess12, score12)
    
    
    print(reveal) # prints the target word in the format of the guess grid
    print('\nWINNER! 6000 master are you.')

    sys.exit()

#----------------------------------------- LOSING LOGIC ------------------------------------------------------------------

build_guess_grid(guess1, score1, guess2, score2, guess3, score3, guess4, score4, guess5, score5, guess6, score6,
                  guess7, score7, guess8, score8, guess9, score9, guess10, score10, guess11, score11, guess12, score12)


print(reveal) # prints the target word in the format of the guess grid
if score12 < 6000:
    print('\nyou didn\'t make it. MAMA LUIGI')
