def reverse_string(word):
    word.lower()
    reverse_word = word[::-1]
    print(f'The  reversed word of {word} is {reverse_word}')

if __name__ == '__main__':
    while True:
        word = input('Please provide a word to reverse :')
        reverse_string(word)
        shall_continue = input('Do you want to continue ([y]/[n])?:')
        if shall_continue.lower() != 'y':
            break
