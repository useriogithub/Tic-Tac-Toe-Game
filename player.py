import math
import random


class Player:
     def __init__(self, letter):
          self.letter = letter
          
     def get_move(self, game):
          pass
     

class RandomComputerPlayer(Player):
     def __init__(self, letter):
          super().__init__(letter)
          
     def get_move(self, game):
          sqaure = random.choice(game.available.moves())
          return sqaure
     
class HumanPlayer(Player):
     def __init__(self, letter):
          super().__init__(letter)
          
     def get_move(self, game):
          vaild_sqaure = False
          val = None
          while not vaild_sqaure:
               sqaure = input(self.letter + '\'s turn.  Input move (0-9)')
               try:
                    val = int(sqaure)
                    if val is not game.available_moves():
                         raise ValueError
               except ValueError:
                    print('Invaild square.  Try again')
          return val
                    
