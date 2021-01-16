#!usr/bin/env python
"""stockfishDemo.py: quick engine demo to A)show stockfish works B) create new python REPO"""

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

board = chess.Board()
while not board.is_game_over():
	result = engine.play(board,chess.engine.Limit(time=0.1))
	board.push(result.move)
	print(board.peek())

engine.quit()

