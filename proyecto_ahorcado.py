import random
import paquete_cientifico as pc


def run():
    word = pc.random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        # muestra el tablero
        pc.display_board(hidden_word, tries)
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
                pc.display_board(hidden_word, tries)
                print('')
                print('Â¡Perdiste! La palabra correcta era ' + word)
                break
        else:
            for idx in letter_indexes: # la letra del usuario es replazada en hidenword
                hidden_word[idx] = current_letter

            # vaciamos esta lista para volver a comenzar el while
            letter_indexes = []

        # encontrar al ganador, terminar el juego // INTENTAR MODIFICAR ESTO POR UN IF/ELSE
        try:
            hidden_word.index('-') #este metodo recibe un elemento como argumento y devuelve un indeci de su primera aparicion en su lista
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: ' + word)
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()


input()