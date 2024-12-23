# Tic - Tac - Toe - Game
# Start
b = [i for i in range(0, 9)]
turns = 0  # count turns to stop after tie
playerx = True  # switch turns between 'X' and 'O'
win_condition = [
    [b[0], b[1], b[2]],  # possibilities for win
    [b[3], b[4], b[5]],
    [b[6], b[7], b[8]],
    [b[0], b[3], b[6]],
    [b[1], b[4], b[7]],
    [b[2], b[5], b[8]],
    [b[0], b[4], b[8]],
    [b[2], b[4], b[6]]
]
while turns < len(b):
    try:
        print(b[0:3])  # prints the board with the actual places
        print(b[3:6])
        print(b[6:9])

        if playerx:  # now player 'X'
            print("'X' - turn")
        else:
            print("'O' - turn")

        a = int(input("insert your play in board (0-8): "))
        if  a > 8 or b[a] == "X" or b[a] == "O":  # return if user input not in range or taken
            print("Try again, Enter number 0-8, in empty place")
            continue
        b[a] = "X" if playerx else "O"
    except NameError as e:
        print(e)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

    for i in b: # start check for Win
        if isinstance(i, str) and i.isalpha():  # check if there is str in [b]
            pass
        for l in win_condition:  # search on all the lists in win_condition
            for indx in range(len(l)):  # check in all indexs in the lists of win_condition
                if l[indx] == a:  # if find str
                    l[indx] = b[a]  # replace to "a"

    for i in win_condition:  # in each list
        if len(set(i)) == 1:  # if there is only 1 value in list
            print(f"Player {b[a]} - WIN")
            print(b[0:3])  # prints the board with the actual places
            print(b[3:6])
            print(b[6:9])
            exit()

    playerx = not playerx
    turns += 1

print("It's a tie!")

# End
