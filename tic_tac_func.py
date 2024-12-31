
def print_board(b):

    print(b[0:3])  # prints the board with the actual places
    print(b[3:6])
    print(b[6:9])

def player_turn(b,playerx,win_con):
    if playerx:  # now player 'X'
        print("'X' - turn")
    else:
        print("'O' - turn")

    a = int(input("insert your play in board (0-8): "))
    if a > 8 or a < 0 or b[a] == "X" or b[a] == "O":  # return if user input not in range or taken
        print("Try again, Enter number 0-8, in empty place")
        return player_turn(b,playerx,win_con)
    else:
        b[a] = "X" if playerx else "O"

        for list in win_con: # change the square in win_condition list to "X" or "O"
            for square in range(len(list)):
                if list[square] == a:
                    list[square] = 'X' if playerx else 'O'

        did_win = check_win(win_con)
        return win_con, did_win

def check_win(win_cond):
    for list in win_cond:
        if all_equal(list):
            print(f'{list[0]} WON')
            return True
    return False


def all_equal(list):
    for i in list:
        if i != list[0]:
            return False
    return True



