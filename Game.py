import heuristic # For ai_turn
import time

# Variables
# game_board = 2d array to simulate the game board
# player = 1 or 2 based on the player turn. 1 = player1, 2 = player2
# s_column = standard column
# s_row = standard row
# last_column = the column in which the last slot filled
# last_row = the row in which the last slot filled
# General Notes
# Board format = board[column][row]


def test_print(board, s_column, s_row):
    # Print board in raw array format
    # for i in board:
    #   print(str(i))
    # Print board in simulated format
    for row in range(s_row):
        print()
        for column in range(s_column):
            print(board[column][row], "| ", end="")
    print()


def generate_board(s_column, s_row):
    # Populate board, fills the 2d array with 0 as the place holder value
    generated_board = [[0 for i in range(0, s_row)] for x in range(0, s_column)]
    return generated_board


def fill(board, column, s_row, player):
    row = int

    # Determines where is the bottom of the row
    for curr_row in range(0, s_row):
        if board[column][curr_row] != 0:
            continue
        else:
            row = curr_row
    board[column][row] = player


def get_lastcolumn(oldboard, newboard):
    for curr_column in range(0, len(newboard)):
        if newboard[curr_column] != oldboard[curr_column]:
            return curr_column
        else: continue

def get_lastrow(oldboard, newboard):
    for curr_column in range(0, len(newboard)):
        for curr_row in range(0, len(newboard[curr_column])):
            if newboard[curr_column][curr_row] != oldboard[curr_column][curr_row]:
                return curr_row
            else: continue


def check(board,column):  # Checks if the column is full
    # Checks if the top of the column is not 0, meaning a full column
    if board[column][0] != 0:
        return False
    else:
        return True


def player_turn(board, s_column, s_row, player):
    # User input for which column
    while True:
        column = int(input("Player " + str(player) + " select column: ")) - 1
        if column not in range(0, s_column):
            print("Column does not exist")
        if not check(board,column):
            print("Slot is full, try another")
        else:
            break
    if check(board,column):
        fill(board, column, s_row, player)  # 1 meaning player1 for player


####### PASS SCORE TO PROCESS#############
def ai_turn(board, s_row, player, curr_score):
    start = time.time()
    decision = heuristic.terminal(board, curr_score, 0, len(board)-1, [board], s_row, 0, player, 1, 2)
    end = time.time()
    print(end - start)
    # decision = heuristic.minimax(board, s_row, player, curr_score, True, 0, 4)
    column = decision
    print(column)
    # curr_score[column] += decision[column] - curr_score[column]
    if check(board, column):
        fill(board, column, s_row, player)
