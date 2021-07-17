#!user/bin/env python
"""bitboardInfrastructure.py: initial creation of an infrastructure of bitboardsfor chess engine processing"""

import string
import numpy as np

from constants import Piece, FileSqures as fsq, RankSquares as rsq

class Board():

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
    


    def __init__(self,board_size=8):
        
        self.bb = self.empty_bb()
        #rank & file bitboards
        self.rank_1_bb = self.empty_bb()
        self.rank_2_bb = self.empty_bb()
        self.rank_3_bb = self.empty_bb()
        self.rank_4_bb = self.empty_bb()
        self.rank_5_bb = self.empty_bb()
        self.rank_6_bb = self.empty_bb()
        self.rank_7_bb = self.empty_bb()
        self.rank_8_bb = self.empty_bb()
        self.file_a_bb = self.empty_bb()
        self.file_b_bb = self.empty_bb()
        self.file_c_bb = self.empty_bb()
        self.file_d_bb = self.empty_bb()
        self.file_e_bb = self.empty_bb()
        self.file_f_bb = self.empty_bb()
        self.file_g_bb = self.empty_bb()
        self.file_h_bb = self.empty_bb()

        #TODO Remember to uncomment me :)
        #self.set_rank_file_bitboard()


        #white piece bitboards
        self.white_P_bb = self.empty_bb()
        self.white_N_bb = self.empty_bb()
        self.white_B_bb = self.empty_bb()
        self.white_R_bb = self.empty_bb()
        self.white_Q_bb = self.empty_bb()
        self.white_K_bb = self.empty_bb()
        
        #black piece bitboards
        self.black_P_bb = self.empty_bb()
        self.black_N_bb = self.empty_bb()
        self.black_B_bb = self.empty_bb()
        self.black_R_bb = self.empty_bb()
        self.black_Q_bb = self.empty_bb()
        self.black_K_bb = self.empty_bb()
        
        #put the pieces onto the bitboards
        self.init_pieces()

        self.white_pieces_bb = self.white_P_bb | self.white_N_bb | self.white_B_bb | self.white_R_bb | self.white_Q_bb | self.white_K_bb 
        self.black_pieces_bb = self.black_P_bb | self.black_N_bb | self.black_B_bb | self.black_R_bb | self.black_Q_bb | self.black_K_bb 
    


        self.occupied_squares_bb = np.vstack( 
                (self.white_P_bb,
                self.white_N_bb, 
                self.white_B_bb, 
                self.white_R_bb, 
                self.white_Q_bb,
                self.white_K_bb, 
                self.black_P_bb, 
                self.black_N_bb,
                self.black_B_bb,
                self.black_R_bb, 
                self.black_Q_bb, 
                self.black_K_bb)
            )


    def empty_bb(self):
        return np.zeros(64, "byte")
        #TODO update getEmptySquares
    def get_empty_squares_bb(self):
        return 1 - self.occupied_squares_bb

    def update_occupied_squares_bb(self):
        result = np.zeros(64, dtype="byte")
        for board in self.occupied_squares_bb:
            result = np.bitwise_or(board, result, dtype="byte")
        self.occupied_squares_bb = result
        return result

    def pretty_print_bitboard(self, bitboard):
        val = ' '        
        for i, square in enumerate(bitboard):
            if not i % 8:
                val += '\n'
            if square:
                val += 'X'
                continue
            val += '-'
        print(val)


    def init_pieces(self):
        #manual entry of starting position... should be a better way to init once FEN
        #conversion is complete

        self.white_R_bb[0] = 1
        self.white_N_bb[1] = 1
        self.white_B_bb[2] = 1
        self.white_Q_bb[3] = 1
        self.white_K_bb[4] = 1
        self.white_B_bb[5] = 1
        self.white_N_bb[6] = 1
        self.white_R_bb[7] = 1
    
        self.black_R_bb[56] = 1
        self.black_K_bb[57] = 1
        self.black_B_bb[58] = 1
        self.black_Q_bb[59] = 1
        self.black_K_bb[60] = 1
        self.black_B_bb[61] = 1
        self.black_N_bb[62] = 1
        self.black_R_bb[63] = 1

        for i in range (8,16):
            self.white_P_bb[i] = 1
        for i in range (48,56):
            self.black_P_bb[i] = 1


def pretty_print_bb(bb, board_size=8):
    """Prettified representation of the board.
    ..TODO:: Refactor into a dedicated module.
    """
    val = ''
    display_rank = board_size
    board = np.reshape(np.flip(bb), (board_size, board_size))
    for i, row in enumerate(board):
        val += f'{display_rank} '
        display_rank -= 1
        for square in np.flip(row):
            if square:
                val += ' ▓'
                continue
            val += ' ░'
        val += '\n'
    val += '  '
    for char in string.ascii_uppercase[:board_size]:
        val += f' {char}'
    print(val)



