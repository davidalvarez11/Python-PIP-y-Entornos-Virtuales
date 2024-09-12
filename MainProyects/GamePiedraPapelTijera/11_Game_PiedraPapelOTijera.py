import random

print('''BIENVENIDO A ESTE JUEGO DE PIEDRA, PAPEL Y TIJERA
JUEGO EN EL QUE SIEMPRE PERDERAS
''')


def choose_optiones():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Elije, piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('OPCIÓN NO VALIDA')
        return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option


def game_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('EMPATE, vuelve a jugar')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('La piedra daña a la tijera')
            print('GANASTE ESTA RONDA')
            user_wins += 1
        else:
            print('El papel envuelve a la piedra')
            print('PERDISTE contra el computador')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('El papel envuelve a la piedra')
            print('GANASTE ESTA RONDA')
            user_wins += 1
        else:
            print('la tijera corta al papel')
            print('PERDISTE contra el computador')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('la tijera corta al papel')
            print('GANASTE ESTA RONDA')
            user_wins += 1
        else:
            print('La piedra daña a la tijera')
            print('PERDISTE contra el computador')
            computer_wins += 1
    
    return user_wins, computer_wins

def game_check_win(user_wins, computer_wins):
    if user_wins == 2:
        print('GANASTE ESTA PARTIDA, INCREIBLE!!!!')
        exit()
    if computer_wins == 2:
        print('Ganó el computador, como siempre')
        exit()

def game_play():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('')
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        rounds += 1

        print('computer_wins =', computer_wins)
        print('user_wins =', user_wins)


        user_option, computer_option = choose_optiones()
        user_wins, computer_wins = game_rules(user_option, computer_option, user_wins, computer_wins)
        game_check_win(user_wins, computer_wins)

game_play()
