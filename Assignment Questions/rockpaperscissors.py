p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

# ...now fill in the rest
rock = "rock"
scissors = "scissors"
paper = "paper"

if p1_move == rock:
    if p2_move == scissors:
        print("Winner: Player 1")
    elif p2_move == rock:
        print("It's a draw")
    else:
        print("Winner: Player 2")

if p1_move == scissors:
    if p2_move == paper:
        print("Winner: Player 1")
    elif p2_move == scissors:
        print("It's a draw")
    else:
        print("Winner: Player 2")

if p1_move == paper:
    if p2_move == rock:
        print("Winner: Player 1")
    elif p2_move == paper:
        print("It's a draw")
    else:
        print("Winner: Player 2")