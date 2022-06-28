# Welcome to the best game ever invented since we created Lizards!
# 1. Ask the user for their name and use it during the game.
#
# 2. Create a list of weapons (rock, paper, scissors, lizard, Spock)
#
# 3. Display the list to the users and ask them to choose their weapon.
#
# 4. Store a random weapon to use against the player's choice.
#
# 5. Using conditions and the reference below, create the game.
#
# 6. Make sure each time a battle occurs, there will be a full explanation about the fight like the following example:
# - User chose Lizard.
# - The computer chose Paper.
# Lizard eats Paper - User wins!
#
# 7. Use full error handling
#
# 8. Use comments and docstrings to inform future programmers.
#
#
# BONUS 9. Ask the users if they want to play again, if so- activate the script again (make sure that there is a new weapon for the computer).
#
# BONUS 10. After the users end the game, ask them if they want to store their score, if they choose yes, store the result in a text file using the following format:
# [timestamp] - [user name] - wins:[num] - loses:[num]


def rps():
    import time
    import random
    from datetime import date
    from datetime import datetime
    global pc_wins
    global player_wins
    global score_board
                                                                    #USER Inputs for the intro section.
    user_name = input('Please eneter your full name: ')
    age = int(input('Please enter your age: '))

                                                                    #Game Intro
    def intro():
        print(f'Hello {user_name}! Welcome to the best game ever invented since Bar wrote it.\n')
        print('We are going to play 5 rounds\n'
              '\nThe game rules:\n'
              '\t 1. Rock beats scissors and lizard\n'
              '\t 2. Paper beats rock and spock\n'
              '\t 3. Scissors beats paper and lizard\n'
              '\t 4. Lizard beats spock and paper\n'
              '\t 8. Spock beats scissors and rock\n'
              '\t 5. Who ever has the most points, wins.\n'
              '\t 6. PG-18, do not play if you are underage.\n')
    intro()

    round = 6
    _round = 5
    wanna = True
    if age < 18:
        print('Sheesh you are underage, who are you trying to fool?!')
        exit()
    else:
        while wanna == 1:
            # Points system
            the_date = date.today()
            today_date = the_date.strftime("%d/%m/%Y")
            the_time = datetime.now()
            today_time = the_time.strftime("%H:%M")
            pc_wins = 0
            player_wins = 0
            score_board = f'\tSTATS:\n\tROUNDS: {_round}/5\nPC: {pc_wins}\t\t{user_name}: {player_wins}\n\t{today_time}\n\t{today_date}'
            # LIST OF WEAPONS
            weapons = ['rock', 'paper', 'scissors', 'lizard', 'spock']
            print('This is your arsenal for today.')
            print(f'{weapons}')
            player_choice = input('Chooce your weapon: ')
            print(f'{user_name} chose {player_choice}!')
            _pc_choice = random.randint(0,4)
            pc_choice = weapons[_pc_choice]
            print(f'The computer chose {pc_choice}')
            if round == 1:
                if pc_wins > player_wins:
                    print(f'{score_board}')
                    rematch = input('You lost.\nDo you want a rematch?')
                                                                                         # HE WANTS TO REMATCH #
                    if rematch.lower() == 'yes':
                        print('Coolcooolcoollll')
                        again = input('Do you want to save the results of the last match? ')
                                                                                        # HE WANTS TO SAVE RESULTS #
                        if again.lower() == 'yes':
                            print('Saving the last match results.\nJust because you are that LAZY')
                            results_file = open('Results.txt','a')
                            results_file.write('-------------------------------------------------------------\n')
                            results_file.write(f'{score_board}\n')
                            results_file.close()
                            pc_wins = 0
                            player_wins = 0
                            round = 6
                            _round = 5

                        else:
                            print('k bye')
                    else:
                        print('Understandable')

                else:
                    print('YOU WON!')
                    print(score_board)
                    again = input('Do you want to save the results of the last match? ')
                    if again.lower() == 'yes':
                        print('Saving the last match results.\nJust because you are that LAZY')
                        results_file = open('Results.txt','a')
                        results_file.write('-------------------------------------------------------------\n')
                        results_file.write(f'score_board\n')
                        results_file.close()
                        exit()
                    else:
                        print('Bye bye')
                        exit()

            if player_choice.lower() == 'rock' and pc_choice.lower() == 'scissors' or 'lizard':
                print('-------------------------------------------------------------\n')
                print(f'Smashing the {pc_choice}')
                player_wins += 1
                _round -= 1
                round -= 1
                print(f'{score_board}')
                player_choice = input('Chooce your weapon: ')
            if player_choice.lower() == 'paper' and pc_choice.lower() == 'rock' or 'spock':
                print('-------------------------------------------------------------\n')
                print(f'Covering the {pc_choice}')
                player_wins += 1
                _round -= 1
                round -= 1
                print(f'{score_board}')
                player_choice = input('Chooce your weapon: ')
            if player_choice.lower() == 'scissors' and pc_choice.lower() == 'paper' or 'lizard':
                print('-------------------------------------------------------------\n')
                print(f'Cutting the {pc_choice}')
                player_wins += 1
                _round -= 1
                round -= 1
                print(f'{score_board}')
                player_choice = input('Chooce your weapon: ')
            if player_choice.lower() == 'lizard' and pc_choice.lower() == 'spock' or 'paper':
                print('-------------------------------------------------------------\n')
                print(f'Poisioning the {pc_choice}')
                player_wins += 1
                _round -= 1
                round -= 1
                print(f'{score_board}')
                player_choice = input('Chooce your weapon: ')
            if player_choice.lower() == 'spock' and pc_choice.lower() == 'paper' or 'scissors':
                print('-------------------------------------------------------------\n')
                print(f'Vaporizing the {pc_choice}')
                player_wins += 1
                _round -= 1
                round -= 1
                print(f'{score_board}')
                player_choice = input('Chooce your weapon: ')
            if player_choice.lower() == pc_choice.lower():
                print('-------------------------------------------------------------\n')
                print('ITS A TIE!')
                _round =- 1
                round =- 1
                print(score_board)
                player_choice = input('Chooce your weapon: ')
            else:
                print('-------------------------------------------------------------\n')
                print('HAHA! You lost')
                pc_wins += 1
                _round -= 1
                round -= 1
                print(f'{score_board}')
                player_choice = input('Chooce your weapon: ')
rps()