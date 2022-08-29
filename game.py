#handling user inputs and printing and inteface part of the game
# creating board
from tic_tac_toe_game import RandomComputerPlayer, UserPlayer, UnbeatableComputerPlayer
from time import sleep

class TicTacToe:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.current_winner = None #To check for winner after every move
        
    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod #decorator
    # https://www.programiz.com/python-programming/methods/built-in/staticmethod
    def print_board_nums():
        number_board =  [[str(position) for position in range(rows * 3, (rows + 1) * 3)] for rows in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |") 

    def available_moves(self):
        return [index for index, spot in enumerate(self.board) if spot == " "]

    def empty_spots(self):
        return " " in self.board #conditional statement(will return True or False)
    
    def num_empty_spots(self):
        return self.board.count(' ')

    def make_move(self, move, letter):
        move = int(move)
        if self.board[move] == " ":
            self.board[move] = letter
            if self.winner(move, letter):
                self.current_winner = letter
            return True
        print("This got executed")
        return False

    def winner(self, move, letter):
        # winner is when same letter in
        # combination at row, column or diagonal
        # checking in rows
        row_index = move // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        #checking in columns
        column_index = move % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # checking diagonals
        if move % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True


        # no winner yet        
        return False


def play(this_game, x_player, o_player, print_game = True):

    if print_game:
        this_game.print_board_nums()

    letter = 'X'

    while this_game.empty_spots():
        #continue executing the game
        if letter == "X":
            spot_move = x_player.get_move(this_game) #passing the full TicTacToe object (this_game) instance
        else:
            spot_move = o_player.get_move(this_game)

        # implementing the move
        # change value in board(viz a list)
        # if you win a game we should declare 
        # winner on that move itself
        # (handled in make_move function)        
        if this_game.make_move(spot_move, letter):
            if print_game:
                print(letter + f' makes a move to spot {spot_move}')
                this_game.print_board()
                print()
            
            if this_game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter #returns to __main__ out of play function

            #changing the turns
            letter = "O" if letter == "X" else "X"
        
        sleep(0.8)

    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
    x_player = UserPlayer('X')
    o_player = UnbeatableComputerPlayer('O')
    this_game = TicTacToe()
    play(this_game, x_player, o_player, print_game = True )
