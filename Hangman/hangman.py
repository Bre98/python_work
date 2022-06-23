import random

word_list = []
used_letters = []
with open('words and definitions', 'r') as word_and_def:
    for line in word_and_def:
        colon = line.split(':')
        word_list.append(colon[0].lower())

word = random.choice(word_list)
with open('words and definitions', 'r') as get_def:
    for line in get_def:
        colon = line.split(':')
        if word == colon[0].lower():
            print(f'The definition of the word means: {colon[1]}')
            print(f'The length of the word is: {len(word)}')
            print(word)
counter = 0
each_letter = list(word)
while counter < 6:
    guess = input('enter a letter:')
    used_letters.append(guess)
    print(f'Used letters: {used_letters}')

    if guess in each_letter:
        print('CORRECT')
        while guess in each_letter:
            each_letter.remove(guess)
        if not each_letter:
            print(f'Congrats! You guessed the word: {word}')
            exit()

    else:
        counter += 1
        print('WRONG')
if counter == 6:
    print('You Lose :(')
