#!user/bin/env python
"""bitboardInfrastructure.py: initial creation of an infrastructure of bitboardsfor chess engine processing"""

import numpy as np

class bitBoard():

    # Bitboards are a numerical representation of where the pieces are 
    # You can get the "occupied" squares of the chessboard by performing a bitwise-and operation on all the bitboards
    #

    """one bitboard consists of 64 bits. Each bit represents a square on the chessboard.
    There is a different bitboard for each color of each piece, 1 represents that the 
    piece is present, 0 is vacant"""

    #funciton to set staring state
    #function to bitwise-and bitboards
    #function to map fen -> boardstate
    #function to pretty print bitboard for debugging
    #legal move list
    


    def __init__(self):
        
        self.bitboards


        self.white_pawn_bitboard = self.empty_bitboard()
        self.white_knight_bitboard = self.empty_bitboard()
        self.white_bishop_bitboard = self.empty_bitboard()
        self.white_rook_bitboard = self.empty_bitboard()
        self.white_queen_bitboard = self.empty_bitboard()
        self.white_king_bitboard = self.empty_bitboard()

        self.black_pawn_bitboard = self.empty_bitboard()
        self.black_knight_bitboard = self.empty_bitboard()
        self.black_bishop_bitboard = self.empty_bitboard()
        self.black_rook_bitboard = self.empty_bitboard()
        self.black_queen_bitboard = self.empty_bitboard()
        self.black_king_bitboard = self.empty_bitboard()

        self.init_pieces()


    def empty_bitboard(self):
        return np.zeros(64)

    def get_occupied_squares(self):
        return self.white_pawn_bitboard \
            & self.white_knight_bitboard \
            & self.white_bishop_bitboard \
            & self.white_rook_bitboard \
            & self.white_queen_bitboard \
            & self.white_king_bitboard \
            & self.black_pawn_bitboard \
            & self.black_knight_bitboard \
            & self.black_bishop_bitboard \
            & self.black_rook_bitboard \
            & self.black_queen_bitboard \
            & self.black_king_bitboard \

def init_pieces(self):
        #manual entry of starting position... should be a better way to init once FEN
        #conversion is complete

        self.white_rook_bitboard[0] = 1
        self.white_knight_bitboard[1] = 1
        self.white_bishop_bitboard[2] = 1
        self.white_queen_bitboard[3] = 1
        self.white_king_bitboard[4] = 1
        self.white_bishop_bitboard[5] = 1
        self.white_knight_bitboard[6] = 1
        self.white_rook_bitboard[7] = 1
    
        self.black_rook_bitboard[56] = 1
        self.black_knight_bitboard[57] = 1
        self.black_bishop_bitboard[58] = 1
        self.black_queen_bitboard[59] = 1
        self.black_king_bitboard[60] = 1
        self.black_bishop_bitboard[61] = 1
        self.black_knight_bitboard[62] = 1
        self.black_rook_bitboard[63] = 1

        for i in range (8,15):
            self.white_pawn_bitboard[i] = 1
        for i in range (48,55):
            self.black_pawn_bitboard[i] = 1


