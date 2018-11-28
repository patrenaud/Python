# Tic-Tac-Toe

# Constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARE = 9

def display_instruct():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
    )

def ask_yes_no(question):
    """Ask a yes or no question"""
    answer = None
    while answer not in ("y","n"):
        answer = input(question).lower()
    return answer

def ask_number(question, min, max):
    """Ask for a number within a range"""
    answer = None
    while answer not in range(min, max):
        answer = int(input(question))
        return answer

def pieces():
    """Determine if player or computer goes first"""
    goFirst = ask_yes_no("Do you want to play first? (y/n): ")
    if goFirst == "y":
        print("Player plays first")
        human = X
        computer = O
    else:
        print("Computer plays first")
        computer = X
        human = O
    return  computer, human

def new_board():
    """Create a new game board"""
    board = []
    for square in range(NUM_SQUARE):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """Create list of legal moves"""
    moves = []
    for square in range(NUM_SQUARE):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Determines the game winner"""
    WAYS_TO_WIN = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """ Get human move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8)", 0, NUM_SQUARE)
        if move not in legal:
            print("\n That swuare is already occupied, foolish human. Choose another \n")
    print("Good move...")
    return move

def cpu_move(board, computer, human):
    """Make computer move"""
    # Make a copy to work with since function will be changing it (list)
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")
 
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
        
    # if human can win, block his ass
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # Done checking this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick the best possibility
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """ Switch tunrs"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(theWinner, computer, human):
    """ Congratulate the winner"""
    if theWinner == computer:
        print("As I predicted, human, I am triumphant once more! \n" \
              "Proof that computers are superior than humans in all regards.")
    elif theWinner == human:
        print("Noooooooooooo!!!  It cannot be! Somehow you tricked me human! \n")
    elif theWinner == TIE:
        print("You were most lucky human... Somehow you managed to tie the game! \n")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = cpu_move(board, computer, human)
            board[move] = computer
        display_board(board)        
        turn = next_turn(turn)

        theWinner = winner(board)
        congrat_winner(theWinner, computer, human)

# Start the game
main()
input("\n\n Press the enter key to exit ")
