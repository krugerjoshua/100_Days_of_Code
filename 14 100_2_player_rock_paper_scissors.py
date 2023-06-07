from getpass import getpass as input
# The players options
print("Please enter R(rock), P(paper) or S(Scissor)")
# Both players enter their choice
player_1 = input(": ")
player_2 = input(": ")
# Determining the winner
if player_1 == player_2:
    print("It's a Tie")
elif (player_1 == 'r' and player_2 == 's') or (player_1 == 'p' and player_2 == 'r') or (player_1 == 's' and player_2 == 'p'):
    print('Player 1 wins')
else:
    print('Player 2 wins')
