import random 
from words import random_words
import string 

def get_valid_word(random_words):
    word = random.choice(random_words) # Take in a list and randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(random_words)
        
    return word.upper()
def hangman():
    word = get_valid_word(random_words)
    word_letters = set(word) #Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guessed
    
    lives = 6
    
    # getting user input 
    while len(word_letters) > 0 and lives > 0 :
        #letters used
        # ''.join(['a','b','cd']) --> 'a b cd'
        print('You have',lives,'remainig and','You have used these letters:  ', ' '.join(used_letters))
        
        # What current word is (W-R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # print('')
            else: 
                lives -= 1 # takes away a life if wrong
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that character, Please try again!')
        
        
        else:
            print('Invalid Character. Please try again!')
    #Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry try again') 
    print('The computer guessed the word', word , '!!')
    # Gets here when len(word_letters) == 0
    
    
if  __name__ == '__main__': 
    hangman()