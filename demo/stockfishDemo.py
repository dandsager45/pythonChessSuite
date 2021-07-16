#!usr/bin/env python
"""stockfishDemo.py: quick engine demo to A)show stockfish works B) create new python REPO"""

import chess
import chess.engine

from chessboard import display
from time import sleep

def start(fen=''):
	global gameboard


engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

board = chess.Board()
display.start(board.fen())

while not board.is_game_over():
	result = engine.play(board,chess.engine.Limit(time=1.01))
	board.push(result.move)
	print(board.peek())
	print(board.fen)
	print("test")
	display.update(board.board_fen())

engine.quit()
display.terminate()
