import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


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



def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        # muestra el tablero
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))
         
        # se crea lista para indexar letras
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        # si no se encuentra letra no hay indexacion, por
        # defecto se muestra se siguen mostrando las "imagenes"
        if len(letter_indexes) == 0:
            tries += 1


            # al septimo intento se pierde la jugada
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Â¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes: # la letra del usuario es replazada en hidenword
                hidden_word[idx] = current_letter

            # vaciamos esta lista para volver a comenzar el while, ESTUDIAR
            letter_indexes = []

        # encontrar al ganador, terminar el juego 
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Â¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()


input()