import copy


def terminal(board, board_score, curr_index, targetindex, terminaldata, s_row, ai_column, player, curr_depth, targetdepth):
    from CONN4 import fill
    ai_board = copy.deepcopy(board)  # AI's "imaginative" board
    score = copy.deepcopy(board_score)
    terminal_list = copy.deepcopy(terminaldata)
    opponent = int
    if player == 1:
        opponent = 2
    elif player == 2:
        opponent = 1

    print("PLAYER#######################################################")
    print(player)
    print("CURRENT DEPTH = "+ str(curr_depth))
    print("TARGET DEPTH = " + str(targetdepth))
    print("CURRENT INDEX = "+ str(curr_index))
    print("TARGET INDEX = " + str(targetindex))
    print("LEAF NODE @@@@@@@@@@@@")
    print(len(terminal_list))
    print("SCORE @@@@@@@")
    print(len(score))

    terminal_board = copy.deepcopy(ai_board)
    fill(terminal_board, ai_column, s_row, player)
    terminal_list.append(terminal_board)

    fill(ai_board, ai_column, s_row, player)
    for i in ai_board:
        print('\033[91m'+str(i)+'\033[0m')
    score[ai_column] += scoring(ai_board, ai_column, get_row(ai_board, ai_column), player)
    for index in range(len(ai_board)):
        score.append(score[index])
    print("maximize point = " + str(score[ai_column]))
    ai_board = copy.deepcopy(board)
    score[ai_column] = copy.deepcopy(board_score[ai_column])
    for i in [score[c:c + 7] for c in range(0, len(score), 7) if c % 5 == 0]:
        print(*i)

    if curr_index == targetindex:   # Generate board for the next depth of tree
        del terminal_list[:1]
        del score[:len(ai_board)]
        print("POST PROCESSING")
        print("LEAF NODE @@@@@@@@@@@@")
        print(len(terminal_list))
        for i in terminal_list:
            print(i)
        print("SCORE @@@@@@@")
        print(len(score))
        if curr_depth == targetdepth:
            return minimax(score, 0, True, 0, targetdepth+1)
        else:
            return terminal(terminal_list[0], score, 0, ((targetindex+1) * len(terminal_list)-1),
                        terminal_list, s_row, 0, opponent, curr_depth + 1, targetdepth)
    else:   # Generate boards for the next terminal index
        if curr_index != 0 and (curr_index+1)%len(board) == 0:
            del terminal_list[:1]
            del score[:len(ai_board)]
            return terminal(terminal_list[0], score, curr_index + 1, targetindex, terminal_list, s_row, 0,
                            player, curr_depth, targetdepth)
        else:
            return terminal(terminal_list[0], score, curr_index + 1, targetindex, terminal_list, s_row, ai_column + 1, player, curr_depth, targetdepth)


def minimax(score, index, maxturn, curr_depth, targetdepth):
    print("##########################################################################################################")
    print("index = "+str(index))
    print("current depth = "+str(curr_depth))
    print("target depth = "+str(targetdepth))
    print("len of score = "+str(len(score)))
    if curr_depth == targetdepth:
        print("score = "+ str(score[index]))
        return score[index]
    if maxturn:
        print("MAX")
        # Maximize score, determine the best column to fill
        return max(minimax(score, index * 7, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 1, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 2, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 3, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 4, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 5, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 6, False, curr_depth + 1, targetdepth))
    else:
        print("MIN")
        # Minimize
        return min(minimax(score, index * 7, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 1, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 2, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 3, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 4, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 5, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 6, True, curr_depth + 1, targetdepth))
    # ai_board = copy.deepcopy(board) # Reset AI's board to the real one
    # return score # Give out the score of all columns


def get_row(board, column):
    # Determines where is the bottom of the row
    for curr_row in range(0, len(board[0])):
        if board[column][curr_row] == 0:
            continue
        else:
            # print("curr row", curr_row)
            return curr_row


########################################################################################################################
# Scores every possible array of two and three disks
def scoring(board, column, row, player):  # Calculate the total score of a column
    normal_array = 4
    score = 0

    # Scores the center column
    center_array = [int(i) for i in list(board[:, column // 2])]
    center_count = center_array.count(player)
    score += center_count * 3

    # Scores horizontally
    for r in range(row):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(column - 3):
            array = row_array[c:c + normal_array]
            score += score_array(array, player)

    # Scores vertically
    for c in range(column):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(row - 3):
            array = col_array[r:r + normal_array]
            score += score_array(array, player)

    # Scores diagonally
    for r in range(row - 3):
        for c in range(column - 3):
            array = [board[r + i][c + i] for i in range(normal_array)]
            score += score_array(array, player)

    for r in range(row - 3):
        for c in range(column - 3):
            array = [board[r + 3 - i][c + i] for i in range(normal_array)]
            score += score_array(array, player)

    return score


########################################################################################################################
# Scores every possible array of two and three disks
def score_array(array, player):
    array_score = 0
    opponent = int
    if player == 1:
        opponent = 2
    elif player == 2:
        opponent = 1

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return array_score

########################################################################################################################
# Check four in a row / win move
def four_in_row(board, column, row, player):
    # win_vertical
    for c in range(column):
        for r in range(row - 3):
            if board[c][r] == player and \
                    board[c][r + 1] == player and \
                    board[c][r + 2] == player and \
                    board[c][r + 3] == player:
                return True

    # win_horizontal
    for c in range(column - 3):
        for r in range(row):
            if board[c][r] == player and \
                    board[c + 1][r] == player and \
                    board[c + 2][r] == player and \
                    board[c + 3][r] == player:
                return True

    # win_right_diagonal
    for c in range(column - 3):
        for r in range(row - 3):
            if board[c][r] == player and \
                    board[c + 1][r + 1] == player and \
                    board[c + 2][r + 2] == player and \
                    board[c + 3][r + 3] == player:
                return True

    # win_left_diagonal
    for c in range(column - 3):
        for r in range(3, row):
            if board[c][r] == player and \
                    board[c + 1][r - 1] == player and \
                    board[c + 2][r - 2] == player and \
                    board[c + 3][r - 3] == player:
                return True
    # no four in a row, False
    return False
