import random

def ex_main():
    try:
        main()
    except KeyboardInterrupt:
        print("Program was interrupted. Exiting the program.")
        exit()

def main():
    while True:
        try:
            choice = input("Type 'S' for singleplayer or 'M' for multiplayer: ").upper()[0]
            if choice == "S" or choice == "M":
                break
            else:
                print("Reselect a valid mode.")
                continue
        except IndexError:
            print("Reselect a valid mode.")
            continue
    if choice == "S":
        singleplayer()
    elif choice == "M":
        multiplayer()

def multiplayer():
    get_info(False)
    for _ in range(rounds):
        play(False)
        linebreak()
    display_winner()

def singleplayer():
    get_info(True)
    for i in range(rounds):
        play(True)
        linebreak()
    display_winner()

def create_grid():
    global tttgrid
    tttgrid = list(list(placeholder for _ in range(3)) for _ in range(3))

def play(is_cpu):
    global won, draw
    won = False
    draw = False
    linebreak()
    create_grid()
    print_grid()
    while won == False and draw == False:
        linebreak()
        modify_grid(posput(),name1)
        linebreak()
        print_grid()
        linebreak()
        check_win()
        if won == True:
            break
        check_draw()
        if draw == True:
            break
        if is_cpu:
            modify_grid(cpuput(),name2)
        else:
            modify_grid(posput(),name2)
        print_grid()
        check_win()
        if won == True:
            break
        check_draw()
        if draw == True:
            break

def check_draw():
    global draw, total_draws
    allelements = []
    if won == False:
        for row in tttgrid:
            for i in row:
                allelements.append(i)
    if placeholder not in allelements:
        draw = True
    if draw == True:
        total_draws += 1

def check_win():
    global won
    for row in tttgrid:
        if (row[0] == row[1] == row[2]) and row[0] != placeholder and won == False:
            won = True
            if row[0] == sign1:
                winner(name1)
            elif row[0] == sign2:
                winner(name2)
    for column in range(3):
        if (tttgrid[0][column] == tttgrid[1][column] == tttgrid[2][column]) and tttgrid[2][column] != placeholder and won == False:
            won = True
            if tttgrid[0][column] == sign1:
                winner(name1)
            elif tttgrid[0][column] == sign2:
                winner(name2)
    if won == False:
        if (tttgrid[0][0] == tttgrid[1][1] == tttgrid[2][2]) and tttgrid[0][0] != placeholder and won == False:
            won = True
            if tttgrid[1][1] == sign1:
                winner(name1)
            elif tttgrid[1][1] == sign2:
                winner(name2)
        elif (tttgrid[0][2] == tttgrid[1][1] == tttgrid[2][0]) and tttgrid[1][1]!= placeholder and won == False:
            won = True
            if tttgrid[1][1] == sign1:
                winner(name1)
            elif tttgrid[1][1] == sign2:
                winner(name2)
    
def modify_grid(pos,playerID):
    if playerID == name1:
        replace_element = sign1
    elif playerID == name2:
        replace_element = sign2
    tttgrid[int((pos-1)/3)][(pos%3)-1] = replace_element

def print_grid():
    for row in tttgrid:
        for element in row:
            print(element, sep ="", end = "  ")
        print("\n")

def get_info(is_cpu):
    global p1wins, p2wins, total_draws, won, draw, placeholder, name1, name2, sign1, sign2, rounds

    p1wins = p2wins = total_draws = 0

    if is_cpu:
        p1_placeholder_name = "player"
    else: 
        p1_placeholder_name = "player 1"
        
    name1 = input(f"Enter {p1_placeholder_name} name here: ").capitalize().split()
    name1 = name1[0]

    while True:
        sign1 = input(f"Enter {p1_placeholder_name} element sign here (1 letter/symbol only): ").upper()
        sign1 = sign1[0]
        if sign1 == "":
            print("Sign cannot be empty.")
            continue
        else:
            break

    if not is_cpu:
        name2 = input("Enter player 2 name here: ").capitalize().split()
        name2 = name2[0]
        while True:
            sign2 = input("Enter player 2 element sign here (1 letter/symbol only): ").upper()
            sign2 = sign2[0]
            if sign2 == "":
                print("Element cannot be empty.")
                continue
            elif sign2 == sign1:
                print("Elements cannot be duplicates")
                continue
            else:
                break
    else:
        name2 = "Cpu"
        while True:
            sign2 = input("Enter CPU element sign here (1 letter/symbol only): ").upper()
            sign2 = sign2[0]
            if sign2 == "":
                print("Element cannot be empty.")
                continue
            elif sign2 == sign1:
                print("Elements cannot be duplicates")
                continue
            else:
                break

    while True:
        placeholder = input("Enter grid element here (Press enter to skip): ").upper()
        if placeholder == "":
            placeholder = "_"
            break
        elif placeholder == sign1 or placeholder == sign2:
            print("Grid Element cannot be the same as player elements.")
        else:
          break

    while True:
        try:
            rounds = int(input("Enter the number of rounds you want to play: "))
            if rounds <= 0:
                print("Number of rounds must be a positive integer.")
                continue
        except ValueError:
            print("Number of rounds must be a positive integer.")
        else:
            break

    if name1 == name2:
        name1 = name1+"_1"
        name2 = name2+"_2"
        print(f"To avoid duplicate name conflict, player 1 is now {name1} and player 2 is now {name2}")

def winner(playerID):
    print(f"The winner is {playerID}")
    global p1wins, p2wins
    if playerID == name1:
        p1wins += 1
    elif playerID == name2:
        p2wins += 1

def cpuput():
    # Check for winning moves
    x = -3
    for row in tttgrid:
        x += 3
        if row.count(sign2) == 2 and row.count(placeholder) == 1:
            return row.index(placeholder) + 1 + x
    
    for col in range(3):
        if tttgrid[0][col] == tttgrid[1][col] == sign2 and tttgrid[2][col] == placeholder:
            return col + 7
        elif tttgrid[0][col] == tttgrid[2][col] == sign2 and tttgrid[1][col] == placeholder:
            return col + 4
        elif tttgrid[1][col] == tttgrid[2][col] == sign2 and tttgrid[0][col] == placeholder:
            return col + 1

    if tttgrid[0][0] == tttgrid[1][1] == sign2 and tttgrid[2][2] == placeholder:
        return 9
    elif tttgrid[0][0] == tttgrid[2][2] == sign2 and tttgrid[1][1] == placeholder:
        return 5
    elif tttgrid[1][1] == tttgrid[2][2] == sign2 and tttgrid[0][0] == placeholder:
        return 1

    if tttgrid[0][2] == tttgrid[1][1] == sign2 and tttgrid[2][0] == placeholder:
        return 7
    elif tttgrid[0][2] == tttgrid[2][0] == sign2 and tttgrid[1][1] == placeholder:
        return 5
    elif tttgrid[1][1] == tttgrid[2][0] == sign2 and tttgrid[0][2] == placeholder:
        return 3
    
    # Block opponent's winning moves
    y = -3
    for row in tttgrid:
        y += 3
        if row.count(sign1) == 2 and row.count(placeholder) == 1:
            return row.index(placeholder) + 1 + y
    
    for col in range(3):
        if tttgrid[0][col] == tttgrid[1][col] == sign1 and tttgrid[2][col] == placeholder:
            return col + 7
        elif tttgrid[0][col] == tttgrid[2][col] == sign1 and tttgrid[1][col] == placeholder:
            return col + 4
        elif tttgrid[1][col] == tttgrid[2][col] == sign1 and tttgrid[0][col] == placeholder:
            return col + 1

    # Strategic positioning
    strategic_positions = [5, 1, 3, 7, 9]
    empty_strategic_positions = [pos for pos in strategic_positions if tttgrid[int((pos-1)/3)][(pos%3)-1] == placeholder]
    if empty_strategic_positions:
        return random.choice(empty_strategic_positions)
    
    # Random move
    poslist = [pos for pos in range(1,10) if tttgrid[int((pos-1)/3)][(pos%3)-1] == placeholder]
    if poslist:
        return random.choice(poslist)
    else:
        return None

def posput():
    while True:
        try:
            pos = int(input("Enter position: "))
        except ValueError:
            print("Value must be an integer.")
        else:
            if pos < 1 or pos > 9:
                print("Value must be between 1 and 9.")
                continue
            at_pos = tttgrid[int((pos-1)/3)][(pos%3)-1]
            if at_pos != placeholder:
                print("Position already occupied, please try again.")
                continue
            else:
                return pos

def linebreak():
    print(("_"*46)+"\n")

def display_winner():
    global p1wins, p2wins, total_draws, name1, name2

    if p1wins > p2wins:
        winner_player = name1
    elif p2wins > p1wins:
        winner_player = name2
    elif p1wins == p2wins:
        winner_player = "None"
        print("The game resulted in a draw.")

    print(f"Final Scores:\n   Winner:{winner_player}\n   {name1}'s Score: {p1wins}\n   {name2}'s Score: {p2wins}\n   Draws: {total_draws}\n\nThanks For Playing.")

ex_main()
