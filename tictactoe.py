# Creating a game to play Tic Tac Toe

board = [None, None, None, None, None, None, None, None, None]
winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def check_board_scores(current_player):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == current_player:
            return True
    return False


def display_board(board):
    print "\n"
    for row_idx in [(0,1,2), (3,4,5), (6,7,8)]:
        row = []
        for i in row_idx:
            if board[i] == 1:
                row.append("X")
            elif board[i] == 2:
                row.append("O")
            else:
                row.append("%s" % i)
        print " | ".join(row)
        print "---------"
    print "\n"



current_player = 1
game_won = False
display_board(board)
while game_won is not True:
    position = input("Player %s: Enter your position:" % current_player)
    position = int(position)
    if position > 8:
        print "Your choice is not valid"
        continue
    elif board[position] is not None:
        print "This position is already marked, you need to choose another one"
        continue
    else:
        board[position] = current_player
    display_board(board)
    game_won = check_board_scores(current_player)
    if game_won:
        print "Player %s WON !!!!!!" % current_player
        break
    elif None not in board:
        print "Game Over, There are no winners"
        break
    else:
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1