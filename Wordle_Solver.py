#Plan:

#import list of available answers
#Create a function that checks the score of each word based on the frequency of how often that word appears in list and returns
#the word with the maximum score. 
#Create and input function that asks the output of the wordle. The letters that were green yellow or gray
#create a function that removes from the initial list the words that have a grey letter and the words that don't have a yellow letter
# and words that have a yellow letter in the same spot abd words that do not have the green letters in the same spot.
# Find the word with the highest score
# #repeat till you get  the answer
# Optional: Add how many words were removed and the chances that the word suggested is the answer:


from collections import Counter

from answers import answer_list

import random

from tqdm import tqdm

def greyletters(results, guess):
    grey_letters = []

    for i in range(5):
        if results[i] == 'B':
            grey_letters.append(guess[i])
    return grey_letters

def yellowletters(results, guess):

    yellow_letters = []

    for i in range(5):
        if results[i]== 'Y':
            yellow_letters.append((guess[i], i))

    return yellow_letters

def greenletters(results,guess):

    green_letters = []

    for i in range(5):
        if results[i] == 'G':
            green_letters.append((guess[i], i))

    return green_letters

def matches_green (word, green_letters):
    return all(word[i] == letter for letter, i in green_letters)

def matches_yellows(word, yellow_letters):
    return all(letter in word and word[i] != letter for letter, i in yellow_letters)

def not_grey(word, grey_letters, green_letters, yellow_letters):
    confirmed_letters = {letter for letter, i in green_letters + yellow_letters}
    return all(letter not in word or letter in confirmed_letters for letter in grey_letters)
    
def new_list(results, guess, answer_list):


    grey_letters = greyletters(results, guess)
    yellow_letters = yellowletters(results, guess)
    green_letters = greenletters(results,guess)

    


    filtered_words = [word for word in answer_list if matches_green(word,green_letters) and
                       matches_yellows(word, yellow_letters) and not_grey(word, grey_letters, green_letters, yellow_letters)]
    
    return filtered_words

                      
def word_frequency(filtered_words):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    array = {}

    for c in alphabet:
        frequency = [0,0,0,0,0]
        for i in range(5):
            for word in filtered_words:
                if word[i] == c:
                    frequency[i] += 1
    
        array.update({c:frequency})

    return array


def word_score(word, array):
    return sum(array.get(letter, [0]*5)[i] for i, letter in enumerate(word))


    

def get_best_word(filtered_words, array):
    max_score = 0
    best_word = ''

    for word in filtered_words:
        score = word_score(word,array)
        if score > max_score:
            best_word = word
    
    return best_word

def wordle_solver():
    
    filtered_words = answer_list
    print('Welcome to the wordle Solver!\n')
    frequencies = word_frequency(filtered_words)
    best_word = get_best_word(filtered_words,frequencies)

    print('The best word to start with is: ' + best_word)

    counter = 0
    guess = best_word

    while counter < 6:
        results = input('Please input the results of the wordle (B,G,Y)\n')
        if results.lower() == 'solved' or results.lower() == 'ggggg':
            print('Congratulations!')
            break
        
        filtered_words = new_list(results, guess, filtered_words )

        frequencies = word_frequency(filtered_words)
        best_word = get_best_word(filtered_words,frequencies)
        guess = best_word
        print('The next best word is: ', guess)
        counter += 1

import random
wordle_solver()

#def get_output(answer, guess):
 #   output = ['B'] * 5
  #  used = [False] * 5  # tracks used letters in answer

    # First pass: greens
   # for i in range(5):
    #    if guess[i] == answer[i]:
     #       output[i] = 'G'
      #      used[i] = True

    # Second pass: yellows
    #for i in range(5):
     #   if output[i] == 'B':
      #      for j in range(5):
       #         if not used[j] and guess[i] == answer[j]:
        #            output[i] = 'Y'
         #           used[j] = True
          #          break

   # return ''.join(output)

#def play_game(answer=None, debug=False):
  #  if answer is None:
   #     answer = random.choice(answer_list)

   # filtered_words = answer_list[:]
   # frequencies = word_frequency(filtered_words)
   # best_word = get_best_word(filtered_words,frequencies)
   # counter = 0

   # if debug:
   #     print(f'Answer is: {answer}')

   # while counter < 6:
    #    guess = best_word

    #    if debug:
    #        print(f'\nGuess {counter + 1}: {guess}')

    #    if guess == answer:
      #      if debug:
     #           print("Correct!")
     #       return answer, counter + 1

     #   output = get_output(answer, guess)
    #    filtered_words = new_list(output, guess, filtered_words)

     #   if not filtered_words:
      #      if debug:
      #          print("No valid words left!")
      #      return answer, 7  # meaning "unsolved"

      #  frequencies = word_frequency(filtered_words)
      #  best_word = get_best_word(filtered_words, frequencies)
       # counter += 1

    #return answer, 7  # failed to solve within 6 guesses


#all_results = []
#for ans in tqdm(answer_list):
  #  all_results.append(play_game(ans, debug=False))

# Analyze results
#solved = [x for x in all_results if x[1] <= 6]
#unsolved = [x for x in all_results if x[1] > 6]

#print(f"Average guesses: {sum(x[1] for x in solved) / len(solved):.2f}")
#print(f"Unsolved: {len(unsolved)} out of {len(answer_list)}")






    



