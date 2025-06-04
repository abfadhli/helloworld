import random


def play_game():
    moves = ['rock', 'paper', 'scissors']
    computer_move = random.choice(moves)
    player_move = input('Choose rock, paper, or scissors: ').strip().lower()
    if player_move not in moves:
        print('Invalid move!')
        return

    if player_move == computer_move:
        print(f"It's a tie. We both chose {player_move}.")
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'paper' and computer_move == 'rock') or \
         (player_move == 'scissors' and computer_move == 'paper'):
        print(f'You win! {player_move} beats {computer_move}.')
    else:
        print(f'You lose. {computer_move} beats {player_move}.')


if __name__ == '__main__':
    while True:
        play_game()
        again = input('Play again? (y/n): ').strip().lower()
        if again != 'y':
            break
