import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], 'classes'))
from tic_tac_toe import TicTacToe

def start():
    game = TicTacToe()
    game.setting()
    while (not game.is_end):
        try:
            game.show()
        except ValueError as ve:
            print(ve)