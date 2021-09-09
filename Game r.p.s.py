import random
import time
import os
import pyfiglet
from colorama import Fore, init

init()

while True:
    try:
# banner
        os.system('cls' or 'clear')

        result = pyfiglet.figlet_format('Game  R . P . S', font='big')

        print(Fore.LIGHTMAGENTA_EX+result +
              ' v => 1.0  ,  Coded By => V.Ezraeil\n')
        print(Fore.RESET+'')

        gametype = input(
            ' Please choose Gametype : [1] - Double Game / [2] - Play Single => ')

# Double Game
        if gametype == '1':
            user1 = input('player 1 Enter your name => ')
            user2 = input('player 2 Enter your name => ')
            print('\nRock => 1 , Paper => 2 , Scissors => 3\n')
            player1 = input(f'{user1} , make your move : ')
            player2 = input(f'{user2} , make your move : ')

            if player1 == player2:
                print('\nThats a tie ... ')
            if player1 == '1':
                if player2 == '2':
                    print(f'{user2} , you wins! ')
                elif player2 == '3':
                    print(f'{user1} , you wins!')
            if player1 == '2':
                if player2 == '1':
                    print(f'{user1} , you wins! ')
                elif player2 == '3':
                    print(f'{user2} , you wins!')
            if player1 == '3':
                if player2 == '1':
                    print(f'{user2} , you wins! ')
                elif player2 == '2':
                    print(f'{user1} , you wins!')

            n = input(' \nThe Double Game begins again  y/n ? ')
            if n == 'y':
                print(Fore.LIGHTGREEN_EX+'\nGame Run again !')
                time.sleep(2)
                continue
            elif n == 'n':
                print(Fore.LIGHTCYAN_EX +' \n Game Ended , Please Run Game again ... \n')
                time.sleep(2)
                break

# Play Single
        while True:
            if gametype != '2':
                print(' Please Enter 1 or 2 ... ')
                time.sleep(2)
                break

            if gametype == '2':

                randomnumber = random.randint(0, 2)
                computermove = 'rock'

                if randomnumber == 0:
                    computermove = '1'
                elif randomnumber == 1:
                    computermove = '2'
                elif randomnumber == 2:
                    computermove = '3'

                user1 = input('\nplayer 1 Enter your name => ')
                print('\nRock => 1 , Paper => 2 , Scissors => 3\n')
                player1 = input(f'{user1} , make your move : ')
                print(f'The Player 2 moved : {computermove}')
                player2 = computermove

                if player1 == player2:
                    print('\nThats a tie ... ')
                if player1 == '1':
                    if player2 == '2':
                        print('player 2 won! ')
                    elif player2 == '3':
                        print(f'{user1} , you wins!')
                if player1 == '2':
                    if player2 == '1':
                        print(f'{user1} you wins! ')
                    elif player2 == '3':
                        print('player 2 won!')
                if player1 == '3':
                    if player2 == '1':
                        print('player 2 won! ')
                    elif player2 == '2':
                        print(f'{user1} , you wins!')

# exit or strat again
            b = input(' \nThe Play Single begins again  y/n ? ')
            if b == 'y':
                print('\n------ Play Single Started ! ------')
                continue
            elif b == 'n':
                print(Fore.LIGHTGREEN_EX+' \n Game RUN again ... ')
                time.sleep(2)
                break

# Errors
    except KeyboardInterrupt:
        n = input('\nDo you want exit ? y/n => ')
        if n == 'y':
            os.system('cls' or 'clear')
            print(Fore.LIGHTRED_EX+' \nCome back again , Good Bye ;)\n')
            break
        elif n == 'n':
            print(Fore.LIGHTGREEN_EX+' \nGame RUN again ... ')
            time.sleep(2)
            continue
    except EOFError:
        n = input('\nDo you want exit ? y/n => ')
        if n == 'y':
            os.system('cls' or 'clear')
            print(Fore.LIGHTRED_EX+' \nCome back again , Good Bye ;)\n')
            time.sleep(2)
            break
        elif n == 'n':
            print(Fore.LIGHTGREEN_EX+' \nGame RUN again')
            time.sleep(2)
            continue
