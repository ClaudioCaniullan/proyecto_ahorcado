# selecciona palabra de la lista WORDS
def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

# imprime pantallas
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)e
    print('--- * --- * --- * --- * --- * --- ')