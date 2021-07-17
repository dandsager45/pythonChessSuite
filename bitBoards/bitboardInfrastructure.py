#!user/bin/env python
"""bitboardInfrastructure.py: initial creation of an infrastructure of bitboardsfor chess engine processing"""

import string
import numpy as np

from constants import Piece, FileSqures as fsq, RankSquares as rsq

class Board():

    # Bitboards are a numerical representation of where the pieces are 
    # You can get the "occupied" squares of the chessboard by performing a bitwise-and operation on all the piece bitboards
    #

    """one bitboard consists of 64 bits. Each bit represents a square on the chessboard.
    There is a different bitboard for each color of each piece, 1 represents that the 
    piece is present, 0 is vacant"""

    #function to bitwise-and bitboards <- is this still needed?
    #function to map fen -> boardstate
    #pawn moves
    #legal move list & captures
    #execute moves 
    #refactor moves to own module
    #examine issue with +7 & -9 and revert hack if possible
    #unit tests?


    def __init__(self,board_size=8):
       
        self.board_size = board_size #64 squares 
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

        self.set_rank_file_bb()


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
       

        #board regions
        
        self.queenside_bb = self.file_a_bb | self.file_b_bb | self.file_c_bb | self.file_d_bb
        self.kingside_bb  = self.file_e_bb | self.file_f_bb | self.file_g_bb | self.file_h_bb
        self.center_files_bb = self.file_c_bb | self.file_d_bb | self.file_e_bb | self.file_f_bb
        self.flanks_bb = self.file_a_bb | self.file_h_bb 
        self.center_bb = (self.file_e_bb | self.file_d_bb) & (self.rank_4_bb | self.rank_5_bb)


 
        #put the pieces onto the bitboards
        self.init_pieces()

        self.white_pieces_bb = self.white_P_bb | self.white_N_bb | \
                               self.white_B_bb | self.white_R_bb | \
                               self.white_Q_bb | self.white_K_bb

 
        self.black_pieces_bb = self.black_P_bb | self.black_N_bb | \
                               self.black_B_bb | self.black_R_bb | \
                               self.black_Q_bb | self.black_K_bb 

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
        return np.zeros(self.board_size**2, "byte")

    def get_empty_squares_bb(self):
        return 1 - self.occupied_squares_bb

    def update_occupied_squares_bb(self):
        result = np.zeros(64, dtype="byte")
        for board in self.occupied_squares_bb:
            result = np.bitwise_or(board, result, dtype="byte")
        self.occupied_squares_bb = result
        return result
    
    #mostly used when performing tests on Jupyter Notebook
    def reset_bb(self):
        self.bb = self.empty_bb()

    def init_pieces(self):
        #manual entry of starting position... should be a better way to init once FEN mapping is complete
        self._set_white()
        self._set_black()


    def _set_white(self):
    
        self.white_R_bb[0] = 1
        self.white_N_bb[1] = 1
        self.white_B_bb[2] = 1
        self.white_Q_bb[3] = 1
        self.white_K_bb[4] = 1
        self.white_B_bb[5] = 1
        self.white_N_bb[6] = 1
        self.white_R_bb[7] = 1
        
        for i in range (8,16):
            self.white_P_bb[i] = 1
   
    def _set_black(self):
 
        self.black_R_bb[56] = 1
        self.black_N_bb[57] = 1
        self.black_B_bb[58] = 1
        self.black_Q_bb[59] = 1
        self.black_K_bb[60] = 1
        self.black_B_bb[61] = 1
        self.black_N_bb[62] = 1
        self.black_R_bb[63] = 1

        for i in range (48,56):
            self.black_P_bb[i] = 1

    def set_rank_file_bb(self):
        #todo: faster numpy methods
        for val in fsq.a: self.file_a_bb[val] = 1
        for val in fsq.b: self.file_b_bb[val] = 1
        for val in fsq.c: self.file_c_bb[val] = 1
        for val in fsq.d: self.file_d_bb[val] = 1
        for val in fsq.e: self.file_e_bb[val] = 1
        for val in fsq.f: self.file_f_bb[val] = 1
        for val in fsq.g: self.file_g_bb[val] = 1
        for val in fsq.h: self.file_h_bb[val] = 1


        for val in rsq._1: self.rank_1_bb[val] = 1
        for val in rsq._2: self.rank_2_bb[val] = 1
        for val in rsq._3: self.rank_3_bb[val] = 1
        for val in rsq._4: self.rank_4_bb[val] = 1
        for val in rsq._5: self.rank_5_bb[val] = 1
        for val in rsq._6: self.rank_6_bb[val] = 1
        for val in rsq._7: self.rank_7_bb[val] = 1
        for val in rsq._8: self.rank_8_bb[val] = 1

    def get_white_pieces_bb(self):

        return self.white_P_bb | \
               self.white_R_bb | \
               self.white_N_bb | \
               self.white_B_bb | \
               self.white_Q_bb | \
               self.white_K_bb 
 
    def get_black_pieces_bb(self):

        return self.black_P_bb | \
               self.black_R_bb | \
               self.black_N_bb | \
               self.black_B_bb | \
               self.black_Q_bb | \
               self.black_K_bb 


    ########################################Piece Movement###################################
    def update_position(self, piece_map):
        pass
    
    #Sliding  piece movement (Queen, King, Rook, Bishop)



    #reference for sliding rays: chessprogramming.org/On_an_empty_Board
    def plus1(self, square):
        #East Ray#
        for i in range(square, self.board_size**2, 1):
            self.bb[i] = 1
            if not (i+1) % 8: 
                return
    #Commented out text is broken
    def plus7(self, square):
        #NorthWest Ray#
        for i in range(square, self.board_size**2, 7):
            self.bb[i] = 1
            #if not (i+1) % 8: 
            #    return
            if not i % 8: 
                return


    def plus8(self, square):
        #North Ray#
        for i in range(square, self.board_size**2, 8):
            self.bb[i] = 1
            if not (i+1) % 8: 
                return

    def plus9(self, square):
        #NorthEast Ray#
        for i in range(square, self.board_size**2, 9):
            self.bb[i] = 1
            if not (i+1) % 8: 
                return

    def minus1(self, square):
        #West Ray#
        for i in range(square, 0, -1):
            self.bb[i] = 1
            if not (i+1) % 8: 
                return

    def minus7(self, square):
        #SouthEast Ray#
        for i in range(square, 0, -7):
            self.bb[i] = 1
            if not (i+1) % 8: 
                return

    def minus8(self, square):
        #South Ray#
        for i in range(square, 0, -8):
            self.bb[i] = 1
            if not (i+1) % 8: 
                return
    #Commented Out text is Broken
    def minus9(self, square):
        #SouthWest Ray#
        for i in range(square, 0, -9):
            self.bb[i] = 1
            #if not (i+1) % 8: 
            #    return
            if not i % 8:
                return

    #Knight Movement
    def make_knight_bb(self):
        knight_map = {}
        for i in range(self.board_size**2):
            knight_map[i] = self.knight_attacks(i)
        return knight_map

    def knight_attacks(self,square):
        row_mask = self.empty_bb()
        col_mask = self.empty_bb()
        agg_mask = self.empty_bb()

        #overflow file mask -> block off overflow knight moves
        if square in fsq.a:
            col_mask = self.file_g_bb | self.file_h_bb
        elif square in fsq.b:
            col_mask = self.file_h_bb
        elif square in fsq.g:
            col_mask = self.file_a_bb
        elif square in fsq.h:
            col_mask = self.file_a_bb | self.file_b_bb

        #overflow ranks mask
        if square in rsq._1:
            row_mask = self.rank_8_bb | self.rank_7_bb
        elif square in rsq._2:
            row_mask = self.rank_8_bb
        #elif square in rsq._7:
        #    row_mask = self.rank_1_bb
        #elif square in rsq._8:
        #    row_mask = self.rank_1_bb | self.rank_2_bb
        
        #aggregate mask
        if (row_mask.any() or col_mask.any()):
            agg_mask = row_mask | col_mask

        attacks = self.empty_bb()

        for i in [0,6,15,17,10,-6,-15,-17,-10]:
            if square + i >= self.board_size**2 or square + i < 0:
                #Skip OOB
                continue
            attacks[square + i] = 1
        if agg_mask.any():
            #bit shift the attacks by mask
            attacks = attacks >> agg_mask
        return attacks



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



