import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.currentWinner = None
    
    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == ' ':
                    moves.append((i,j))
        return moves
    
    def empty_squares(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return True
        return False
    
    def make_move(self, square, letter):
        if self.board[square[0]][square[1]] == ' ':
            self.board = letter
        
    def winner(self, square, letter):
        if all(spot == letter for spot in self.board[square[0]]):
            return True
        if all(spot == letter for spot in (self.board[i][square[1]] for i in range(3))):
            return True
        
        diagonal1 = [(0,0), (1,1), (2,2)]
        diagonal2 = [(0,2), (1,1), (2,0)]
        
        if all(spot == letter for spot in (self.board[i][j] for i,j in diagonal1)):
            return True
        if all(spot == letter for spot in (self.board[i][j] for i,j in diagonal2)):
            return True

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            print(f"{self.letter}'s turn! Input row and column index (0-2)")
            try:
                row = int(input("Row: "))
                col = int(input("Column: "))
                val = (row, col)
                if val not in game.available_moves():
                    raise ValueError
            except:
                print("Invalid entry! Try again please.")
        
        return val 

class ComputerPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.availavle_moves())
        return square

def play(game: TicTacToe, x_player: Player, o_player: Player):
    
    game.print_board()
    letter = 'X'
    
    while game.empty_squares():
        square = o_player.get_move() if letter == 'O' else x_player.get_move()
        game.make_move(square, letter)
        game.print_board()
        
        letter = 'O' if letter == 'X' else 'X'        

# toe = TicTacToe()