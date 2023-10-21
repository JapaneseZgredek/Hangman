

def read_from_file() -> list:
    list_of_words = []
    with open('words.txt') as f:
        lines = f.readlines()
        for word in lines:
            list_of_words.append(word.removesuffix('\n'))
    return list_of_words


def main():
    list_of_words = read_from_file()


if __name__ == '__main__':
    main()

