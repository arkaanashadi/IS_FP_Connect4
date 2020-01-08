import CONN4 as game
import heuristic
import copy

def main():
    # Standard Connect 4 board dimensions
    s_column = 7
    s_row = 6
    game_board = game.generate_board(s_column, s_row)
    game.test_print(game_board, s_column, s_row)
    winner = 0
    turn = 1
    ai_scoring1 = [0] * len(game_board)
    ai_scoring2 = [0] * len(game_board)
    while winner == 0:
        prev_board = copy.deepcopy(game_board)
        if turn == 1:
            game.player_turn(game_board, s_column, s_row, 1)
            # game.ai_turn(game_board, s_row, 1, ai_scoring1)
            last_column = game.get_lastcolumn(prev_board, game_board)
            last_row = game.get_lastrow(prev_board, game_board)
            if heuristic.four_in_row(game_board, s_column, s_row, 1):
                winner = 1
            game.test_print(game_board, s_column, s_row)
            turn = 2
        elif turn == 2:
            print("turn 2")
            game.player_turn(game_board, s_column , s_row, 2)
            #game.ai_turn(game_board, s_row, 2, ai_scoring2)
            last_column = game.get_lastcolumn(prev_board, game_board)
            last_row = game.get_lastrow(prev_board, game_board)
            if heuristic.four_in_row(game_board, s_column, s_row, 2):
                winner = 2
            game.test_print(game_board, s_column, s_row)
            turn = 1
        if winner != 0:
            print("Winner :", winner)
            break

main()
