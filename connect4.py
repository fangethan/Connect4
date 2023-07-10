import random
import os
import time
import math


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system("cls" if os.name == "nt" else "clear")


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    user_input = input(prompt)
    invalid_input = True
    while invalid_input:
        if (
            user_input in valid_inputs
        ):  # if function is used to check whether the user input is valid or not
            invalid_input = (
                False  # here invalid_input = False means the end of the loop
            )
        else:
            print("Invalid input, please try again.")
            user_input = input(prompt)

    return user_input


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    board = []  # creating a list "board"
    for row in range(1, 7):  # range(1,7) will runs 6 times creating 6 rows.
        board.append(
            [0] * 7
        )  # everytime the loop is ran, 7x [0] will be append to each row.
    return board


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    print("========== Connect4 =========")  # displays the game title and player info
    print("Player 1: X       Player 2: O")
    print()  # prints a blank line
    print("  1   2   3   4   5   6   7")
    print(" --- --- --- --- --- --- ---")

    for row in board:
        row_str = (
            "|"  # row_str represents the rows using the values from the list board
        )
        for cell in row:  # nested for loops to access each cell of the board
            if cell == 0:
                row_str += "   |"  # if the value is 0 an empty space is added
            elif cell == 1:
                row_str += " X |"  # if the value is 1 X is added
            else:
                row_str += " O |"  # if the value is 2 O is added
        print(row_str)  # prints the complete row
        print(
            " --- --- --- --- --- --- ---"
        )  # displays a horizontal line after each row
    print("=============================")


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player who is dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    success = False  # declaring a variable called "success" to

    for i in range(len(board) - 1, -1, -1):  #
        while success == False:
            if board[i][column - 1] == 0:
                board[i][column - 1] = player
                success = True
            break

    return success


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    # user_column_input responsiblity is to hold the valid column number from validate_input
    user_column_input = validate_input(
        "Player "
        + str(player)
        + ", please enter the column you would like to drop your piece into: ",
        ["1", "2", "3", "4", "5", "6", "7"],
    )
    # is_drop_piece_successful is a boolean to check whether or not the piece was dropped successfully. Starts off as False
    is_drop_piece_successful = False

    # A while loop that continues asking for a column input from the user until user inputs a column number that a drop piece can successfully be placed
    while not is_drop_piece_successful:
        # checks if the drop piece was successful or not in the column
        if drop_piece(board, player, int(user_column_input)):
            # set is_drop_piece_successful to true to end loop as piece can be dropped in the column user requested
            is_drop_piece_successful = True
        else:
            # user chose a column that can no longer have any more pieces dropped into, invalid message to explain user why it failed
            print("That column is full, please try again.")
            # asks the user to re-enter a new column number input, and continue the while loop until successful
            user_column_input = validate_input(
                "Player "
                + str(player)
                + ", please enter the column you would like to drop your piece into: ",
                ["1", "2", "3", "4", "5", "6", "7"],
            )

    # when drop piece is successful, return the column number the user input but as an integer
    return int(user_column_input)


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # both variables are constants since neither value ever changes
    # number of rows in the board
    NUM_ROWS = len(board)
    # number of columns in the board
    NUM_COLUMNS = len(board[1])

    # Check for vertical win
    # rows range is subtracted by 3, so we don't go out of index range
    for row_index in range(NUM_ROWS - 3):
        for col_index in range(NUM_COLUMNS):
            if (
                board[row_index][col_index]
                == board[row_index + 1][col_index]
                == board[row_index + 2][col_index]
                == board[row_index + 3][col_index]
                and board[row_index][col_index] != 0
            ):
                if board[row_index][col_index] == 1:
                    return 1
                else:
                    return 2

    # Check for horizontal win
    # columns range is subtracted by 3, so we don't go out of index range
    for row_index in range(NUM_ROWS):
        for col_index in range(NUM_COLUMNS - 3):
            if (
                board[row_index][col_index]
                == board[row_index][col_index + 1]
                == board[row_index][col_index + 2]
                == board[row_index][col_index + 3]
                and board[row_index][col_index] != 0
            ):
                if board[row_index][col_index] == 1:
                    return 1
                else:
                    return 2

    # Check for diagonal win if its from top-left to bottom right
    # row range is from 0 to 3 because in this instance, this is the only possible combinations of a diagonal
    for row_index in range(0, 3):
        for col_index in range(0, 4):
            if (
                board[row_index][col_index]
                == board[row_index + 1][col_index + 1]
                == board[row_index + 2][col_index + 2]
                == board[row_index + 3][col_index + 3]
                and board[row_index][col_index] != 0
            ):
                if board[row_index][col_index] == 1:
                    return 1
                else:
                    return 2

    # Check for diagonal win if its from bottom-left to top-right
    # rows start at index 3 because that is the beginning of a possible diagonal
    for row_index in range(3, NUM_ROWS):
        for col_index in range(0, 4):
            if (
                board[row_index][col_index]
                == board[row_index - 1][col_index + 1]
                == board[row_index - 2][col_index + 2]
                == board[row_index - 3][col_index + 3]
                and board[row_index][col_index] != 0
            ):
                if board[row_index][col_index] == 1:
                    return 1
                else:
                    return 2

    # checks if the board is over or a draw or is still going
    for row in board:
        if 0 in row:
            return 0
    return 3


def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # is_player_1_turn checks if it player 1 turn or not
    is_player_1_turn = True
    # is_board_blank checks if the board is blank
    is_board_blank = True
    # display_previous_move shows a message of the player dropping a piece in which column
    display_previous_move = ""
    # create blank board
    board = create_board()

    # checks if the game is still going or not
    while end_of_game(board) == 0:
        clear_screen()
        print_board(board)

        if not is_board_blank:
            print(display_previous_move)

        if is_player_1_turn:
            move = execute_player_turn(1, board)
            display_previous_move = "Player 1 dropped a piece into column " + str(move)
            is_player_1_turn = False
            is_board_blank = False
        else:
            move = execute_player_turn(2, board)
            display_previous_move = "Player 2 dropped a piece into column " + str(move)
            is_player_1_turn = True

    # print the board one final time to show the end of the game
    print_board(board)
    if end_of_game(board) == 1:
        print("Player 1 won!")
    elif end_of_game(board) == 2:
        print("Player 2 won!")
    else:
        print("It is a draw!")

    print("Game will be returning to the main lobby in 3 seconds")
    time.sleep(3)
    main()


def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    clear_screen()
    still_playing = True

    while still_playing:
        print("=============== Main Menu ===============")
        print("Welcome to Connect 4!")
        print("1. View Rules")
        print("2. Play a local 2 player game")
        print("3. Play a game against the computer")
        print("4. Exit")
        print("=========================================")
        option = int(input())
        if option == 1:
            clear_screen()
            print_rules()
        elif option == 2:
            local_2_player_game()
        elif option == 3:
            game_against_cpu()
        elif option == 4:
            still_playing = False
    quit()


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    random_column = random.randint(1, 7)
    successful_drop = drop_piece(board, player, random_column)
    if successful_drop == True:
        return random_column

    while successful_drop is False:
        random_column = random.randint(1, 7)
        successful_drop = drop_piece(board, player, random_column)
        if successful_drop == True:
            return random_column


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    for column in range(1, 8):
        board_copy = [
            [cell for cell in row] for row in board
        ]  # makes a copy of the board to simulate the cpu dropping a piece
        if drop_piece(board_copy, player, column):
            if end_of_game(board_copy) == player:  # checks for an immediate win
                drop_piece(
                    board, player, column
                )  # if cpu wins a piece is dropped in the actual board
                return column

    for column in range(1, 8):
        board_copy = [
            [cell for cell in row] for row in board
        ]  # makes a copy of the board to simulate player 1 dropping a piece
        if drop_piece(board_copy, 3 - player, column):
            if (
                end_of_game(board_copy) == 3 - player
            ):  # checks for an immediate win to block
                drop_piece(
                    board, player, column
                )  # if player 1 wins cpu drops a piece in the actual board
                return column

    return cpu_player_easy(board, player)


def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.
    <Insert player strategy here>

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: None

    The strategy of hard is the following:
    1) Check if we can be bottom middle to begin game
    2) Check if cpu can immediately win
    3) Check if player can immediately win to block
    4) Block any chance a player can set up a 2 win way
    5) Check if cpu can form 3 pieces in a row to set up a fourth
    6) Check if player can form 3 pieces in a row to set up a fourth to block
    7) Check if player can form 2 pieces in a row to build a way to 4
    8) Check if cpu can form 2 pieces in a row to build a way to 4
    9) random generator for column
    """

    # to start the game, if user doesn't pick the bottom middle column first
    if board[len(board) - 1][math.floor(len(board[1]) / 2)] == 0 and drop_piece(
        board, player, math.floor(len(board[1]) / 2) + 1
    ):
        return math.floor(len(board[1]) / 2) + 1

    # checks for immediate win
    for column in range(1, 8):
        board_copy = [
            [cell for cell in row] for row in board
        ]  # makes a copy of the board to simulate the cpu dropping a piece
        if drop_piece(board_copy, player, column):
            if end_of_game(board_copy) == player:  # checks for an immediate win
                drop_piece(
                    board, player, column
                )  # if cpu wins a piece is dropped in the actual board
                return column

    # checks for immediate block against player
    for column in range(1, 8):
        board_copy = [
            [cell for cell in row] for row in board
        ]  # makes a copy of the board to simulate player 1 dropping a piece
        if drop_piece(board_copy, 3 - player, column):
            if (
                end_of_game(board_copy) == 3 - player
            ):  # checks for an immediate win to block
                drop_piece(
                    board, player, column
                )  # if player 1 wins cpu drops a piece in the actual board
                return column

    # blocks a 2 way win from the player
    for column in range(1, 8):
        board_copy = [[cell for cell in row] for row in board]
        if drop_piece(board_copy, 3 - player, column):
            if check_cpu_does_not_give_immediate_win(board_copy, column):
                for row in range(len(board)):
                    if board_copy[row][column - 1] != board[row][column - 1]:
                        if prevent_two_way_win_from_user(board_copy, 3 - player):
                            drop_piece(board, player, column)
                            return column

    # can the cpu forms 3 pieces in a row
    for column in range(1, 8):
        board_copy = [[cell for cell in row] for row in board]
        if drop_piece(board_copy, player, column):
            if check_cpu_does_not_give_immediate_win(board_copy, column):
                if form_connect_three(board_copy, player):
                    drop_piece(board, player, column)
                    return column

    # blocks a 3 pieces in a row from player
    for column in range(1, 8):
        board_copy = [[cell for cell in row] for row in board]
        if drop_piece(board_copy, 3 - player, column):
            if form_connect_three(board_copy, 3 - player):
                drop_piece(board, player, column)
                return column

    # blocks a 2 piece in a row from player
    for column in range(1, 8):
        board_copy = [[cell for cell in row] for row in board]
        if drop_piece(board_copy, player, column):
            if check_cpu_does_not_give_immediate_win(board_copy, column):
                if form_connect_two(board_copy, player):
                    drop_piece(board, player, column)
                    return column

    # forms 2 pieces in a row for cpu
    for column in range(1, 8):
        board_copy = [[cell for cell in row] for row in board]
        if drop_piece(board_copy, 3 - player, column):
            if form_connect_two(board_copy, 3 - player):
                drop_piece(board, player, column)
                return column

    return cpu_player_easy(board, player)


# checks cpu does not put a piece down in a column, that gives player the automatic win
def check_cpu_does_not_give_immediate_win(board, column):
    if drop_piece(board, 1, column):
        if end_of_game(board) == 1:
            return False
    return True


# tries to prevent the player having two ways to win the game at the same time
def prevent_two_way_win_from_user(board, player):
    NUM_ROWS = len(board)
    NUM_COLUMNS = len(board[1])

    # check diagonal bottom left to top right
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS):
            if (
                col_index < 4
                and col_index > 0
                and row_index < 5
                and board[row_index][col_index]
                == board[row_index - 1][col_index + 1]
                == board[row_index - 2][col_index + 2]
                and board[row_index - 3][col_index + 3] == 0
                and board[row_index + 1][col_index - 1] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check diagonal bottom right to top left
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS - 1, -1, -1):
            if (
                col_index > 1
                and col_index < 6
                and row_index < 5
                and board[row_index][col_index]
                == board[row_index - 1][col_index - 1]
                == board[row_index - 2][col_index - 2]
                and board[row_index - 3][col_index - 3] == 0
                and board[row_index + 1][col_index + 1] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check horizontal
    for row_index in range(NUM_ROWS):
        for col_index in range(NUM_COLUMNS):
            if (
                col_index + 3 < 7
                and col_index - 1 >= 0
                and board[row_index][col_index]
                == board[row_index][col_index + 1]
                == board[row_index][col_index + 2]
                and board[row_index][col_index + 3] == 0
                and board[row_index][col_index - 1] == 0
                and board[row_index][col_index] == player
            ):
                return True

    return False


# checks if cpu/player can form 3 pieces in a row
def form_connect_three(board, player):
    NUM_ROWS = len(board)
    NUM_COLUMNS = len(board[1])

    # check diagonal bottom left to top right
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS):
            if (
                col_index < 4
                and board[row_index][col_index]
                == board[row_index - 1][col_index + 1]
                == board[row_index - 2][col_index + 2]
                and board[row_index - 3][col_index + 3] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check diagonal bottom right to top left
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS - 1, -1, -1):
            if (
                col_index > 1
                and board[row_index][col_index]
                == board[row_index - 1][col_index - 1]
                == board[row_index - 2][col_index - 2]
                and board[row_index - 3][col_index - 3] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check horizontal
    for row_index in range(NUM_ROWS):
        for col_index in range(NUM_COLUMNS):
            if (
                col_index + 3 < 7
                and board[row_index][col_index]
                == board[row_index][col_index + 1]
                == board[row_index][col_index + 2]
                and board[row_index][col_index + 3] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check vertical
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS):
            if (
                board[row_index][col_index]
                == board[row_index - 1][col_index]
                == board[row_index - 2][col_index]
                and board[row_index - 3][col_index] == 0
                and board[row_index][col_index] == player
            ):
                return True

    return False


# checks if cpu/player can form 2 pieces in a row
def form_connect_two(board, player):
    NUM_ROWS = len(board)
    NUM_COLUMNS = len(board[1])

    # check horizontal
    for row_index in range(NUM_ROWS):
        for col_index in range(NUM_COLUMNS):
            if (
                col_index + 2 < 7
                and board[row_index][col_index] == board[row_index][col_index + 1]
                and board[row_index][col_index + 2] == 0
                and board[row_index][col_index] == player
            ):
                return True
            elif (
                col_index - 1 > 0
                and col_index + 1 < 6
                and board[row_index][col_index] == board[row_index][col_index + 1]
                and board[row_index][col_index - 1] == 0
                and board[row_index][col_index] == player
            ):
                return True

    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS):
            if (
                col_index < 5
                and board[row_index][col_index] == board[row_index - 1][col_index + 1]
                and board[row_index - 2][col_index + 2] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check diagonal bottom right to top left
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS - 1, -1, -1):
            if (
                col_index > 0
                and board[row_index][col_index] == board[row_index - 1][col_index - 1]
                and board[row_index - 2][col_index - 2] == 0
                and board[row_index][col_index] == player
            ):
                return True

    # check vertical
    for row_index in range(NUM_ROWS - 1, -1, -1):
        for col_index in range(NUM_COLUMNS):
            if (
                board[row_index][col_index] == board[row_index - 1][col_index]
                and board[row_index - 2][col_index] == 0
                and board[row_index][col_index] == player
            ):
                return True

    return False


def game_against_cpu():
    """
    Runs a game of Connect 4 against the computer.

    :return: None
    """
    # Implement your solution below

    clear_screen()
    board = create_board()
    valid_option = False

    # is_user_turn checks if it player 1 turn or not
    is_user_turn = True
    # is_board_blank checks if the board is blank
    is_board_blank = True
    # display_previous_move shows a message of the player dropping a piece in which column
    display_previous_move = ""

    display_count = 0

    difficulty_option = int(
        input("Select CPU difficulty level of Easy (1), Medium (2), Hard (3): ")
    )

    while not valid_option:
        if difficulty_option == 1 or difficulty_option == 2 or difficulty_option == 3:
            valid_option = True
        else:
            print("Invalid Option selected. Try again")
            print("Choose an option of the following")
            print("Easy: 1")
            print("Medium: 2")
            print("Hard: 3")
            difficulty_option = int(
                input("Select CPU difficulty level of Easy (1), Medium (2), Hard (3): ")
            )

    while end_of_game(board) == 0:
        clear_screen()
        print_board(board)

        if not is_board_blank and display_count % 2 == 0:
            print(display_previous_move)

        if is_user_turn:
            move = execute_player_turn(1, board)
            display_previous_move = "Player 1 dropped a piece into column " + str(move)
            is_user_turn = False
            is_board_blank = False
            display_count += 1
        else:
            if difficulty_option == 1:
                move = cpu_player_easy(board, 2)
            elif difficulty_option == 2:
                move = cpu_player_medium(board, 2)
            elif difficulty_option == 3:
                move = cpu_player_hard(board, 2)
            display_previous_move += (
                "\nPlayer 2 (CPU) dropped a piece into column " + str(move)
            )
            is_user_turn = True
            display_count += 1

    # print the board one final time to show the end of the game
    print_board(board)
    if end_of_game(board) == 1:
        print("You won against the CPU!")
    elif end_of_game(board) == 2:
        print("Bad luck. You lost to the CPU")
    else:
        print("It is a draw!")

    print("Game will be returning to the main lobby in 3 seconds")
    time.sleep(3)
    main()


if __name__ == "__main__":
    main()
