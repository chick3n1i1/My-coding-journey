# play the game

class Board:
   def __init__(self, dim_size, num_bombs):
       self.dim_size = dim_size
       self.num_bombs = num_bombs

       #create the board
       self.board = self.make_new_board() #plant the bombs

       #initialize a set to keep track of which locations have been uncovered
       #save (row, col) tuples into this set
       self.dug = set() #if we dig at 0,0; then self.dug = {(0,0)}
       pass 


    def make_new_board(self):



def play(dim_size=10, num_bombs=10):
    # Step1: create the board and plant bombs
    # Step2: show the user the board and ask for where they want to dig
    # Step3a: if location is a bomb, show game over message
    # Step3b: if location is not a bomb, dig recursively until each square is at least
    #   next to a bomb
    # Step4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass
