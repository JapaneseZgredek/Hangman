import random

LIVES = 8


def read_from_file() -> list:
    list_of_words = []
    with open('words.txt') as f:
        lines = f.readlines()
        for word in lines:
            list_of_words.append(word.removesuffix('\n'))
    return list_of_words


def main():
    global LIVES
    list_of_words = read_from_file()
    word_to_guess = list_of_words[random.randint(0, len(list_of_words))]
    correct_guesses = 0
    print(word_to_guess)
    while LIVES > 0 and correct_guesses != len(word_to_guess):
        print('WORD: ' + ('-' * len(word_to_guess)))
        user_guess = input('Guess the letter or the whole word: ')
        if len(user_guess) > 1:
            if user_guess == word_to_guess:
                correct_guesses = len(word_to_guess)
                continue
            LIVES -= 1
    
    if LIVES > 0:
        print('CONGRATS YOU WON 👑')
    else:
        print('YOU LOST :(')


if __name__ == '__main__':
    main()
