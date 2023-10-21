import random

LIVES = 8


def read_from_file() -> list:
    list_of_words = []
    with open('words.txt') as f:
        lines = f.readlines()
        for word in lines:
            list_of_words.append(word.removesuffix('\n'))
    return list_of_words


def get_indexes_of_guessed_letter(user_guess: str, word_to_guess: str) -> list:
    indexes = []
    for i in range(len(word_to_guess)):
        if user_guess == word_to_guess[i]:
            indexes.append(i)
    return indexes


def main():
    global LIVES
    list_of_words = read_from_file()
    word_to_guess = list_of_words[random.randint(0, len(list_of_words))]
    correct_guesses = 0
    did_guess_letter = [False] * len(list_of_words)
    history_user_input = []
    print(word_to_guess)

    while LIVES > 0 and correct_guesses != len(word_to_guess):
        print("Enter 1 to see the history of guesses: ")
        for i in range(len(word_to_guess)):
            if did_guess_letter[i]:
                print(word_to_guess[i], end="")
            else:
                print('-', end="")

        user_guess = input('\nGuess the letter or the whole word: ')

        if user_guess == '1':
            print(history_user_input)
            continue

        if user_guess in history_user_input:
            print('You already tried tha one. try again')
            continue
        history_user_input.append(user_guess)

        if len(user_guess) > 1:
            if user_guess == word_to_guess:
                correct_guesses = len(word_to_guess)
                continue
            LIVES -= 1

        indexes_of_guessed = get_indexes_of_guessed_letter(user_guess, word_to_guess)
        correct_guesses += len(indexes_of_guessed)

        if len(indexes_of_guessed) == 0:
            print("WRONG GUESS")
            LIVES -= 1

        for index in indexes_of_guessed:
            did_guess_letter[index] = True

    if LIVES > 0:
        print('CONGRATS YOU WON 👑')
    else:
        print('YOU LOST :(')


if __name__ == '__main__':
    main()
