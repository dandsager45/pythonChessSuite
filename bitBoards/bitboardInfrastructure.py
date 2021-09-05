#!user/bin/env python
"""bitboardInfrastructure.py: initial creation of an infrastructure of bitboardsfor chess engine processing"""

import numpy as np

from bitboard_helpers import make_empty_uint64_bitmap, set_bit, make_knight_attack_bbs, make_king_attack_bbs, \
    make_white_pawn_attack_bbs, make_black_pawn_attack_bbs, file_h_bb, file_a_bb, make_diag_attack_bbs, \
    make_rook_attack_bbs, make_white_pawn_motion_bbs, make_black_pawn_motion_bbs
from constants import Piece

BOARD_SIZE = 8
BOARD_SQUARES = BOARD_SIZE ** 2

#Bitboards are a numerical representation of where the pieces are 
# You can get the "occupied" squares of the chessboard by performing a bitwise-and operation on all the piece bitboards
#

"""
one bitboard consists of 64 bits. Each bit represents a square on the chessboard.
There is a different bitboard for each color of each piece, 1 represents that the 
piece is present, 0 is vacant
"""

class Board:

    def __init__(self):
       
        self.board_size = BOARD_SIZE #64 squares 
                
        #white piece bitboards
        self.white_P_bb = make_empty_uint64_bitmap()
        self.white_N_bb = make_empty_uint64_bitmap()
        self.white_B_bb = make_empty_uint64_bitmap()
        self.white_R_bb = make_empty_uint64_bitmap()
        self.white_Q_bb = make_empty_uint64_bitmap()
        self.white_K_bb = make_empty_uint64_bitmap()
        
        #black piece bitboards
        self.black_P_bb = make_empty_uint64_bitmap()
        self.black_N_bb = make_empty_uint64_bitmap()
        self.black_B_bb = make_empty_uint64_bitmap()
        self.black_R_bb = make_empty_uint64_bitmap()
        self.black_Q_bb = make_empty_uint64_bitmap()
        self.black_K_bb = make_empty_uint64_bitmap()
                            
        #put the pieces onto the bitboards
        self.init_pieces()

        #static bitboards
        self.knight_bbs = make_knight_attack_bbs()
        self.bishop_bbs = make_diag_attack_bbs()
        self.rook_attack_bbs = make_rook_attack_bbs()
        self.king_attack_bbs = make_king_attack_bbs()
        self.white_pawn_attack_bbs = make_white_pawn_attack_bbs()
        self.black_pawn_attack_bbs = make_black_pawn_attack_bbs()
        self.white_pawn_motion_bbs = make_white_pawn_motion_bbs()
        self.black_pawn_motion_bbs = make_black_pawn_motion_bbs()

    # -----------------------------------------------------
    #  BITBOARD ACCESS: PIECE LOCATIONS
    # -----------------------------------------------------


    @property
    def white_pieces_bb(self):
        return  self.white_P_bb | self.white_N_bb | \
                self.white_B_bb | self.white_R_bb | \
                self.white_Q_bb | self.white_K_bb
    @property
    def black_pieces_bb(self):
        return  self.black_P_bb | self.black_N_bb | \
                self.black_B_bb | self.black_R_bb | \
                self.black_Q_bb | self.black_K_bb
    @property
    def occupied_squares_bb(self):
        return self.white_pieces_bb | self.black_pieces_bb
    
    @property
    def empty_squares_bb(self):
        return ~self.occupied_squares_bb

    @property
    def white_P_east_attacks(self):
        #white pawn east attacks are north east (+9) AND NOT the A file
        return (self.white_P_bb << 9 ) & (~file_a_bb)
            
    @property
    def white_P_west_attacks(self):
        #white pawn west attacks are north west (+7) AND NOT the H file
        return (self.white_P_bb << 7) & (~file_h_bb)

    @property
    def white_pawn_attacks(self):
        return self.white_P_east_attacks | self.white_P_west_attacks

    @property
    def black_P_east_attacks(self):
        #white pawn east attacks are south east (-7) AND NOT the A file
        return (self.black_P_bb >> 7 ) & (~file_a_bb)

    @property
    def black_P_west_attacks(self):
        #white pawn west attacks are north west (-9) AND NOT the H file
        return (self.black_P_bb >> 9) & (~file_h_bb)
    
    @property
    def black_pawn_attacks(self):
        return self.black_P_east_attacks | self.black_P_west_attacks


    # -----------------------------------------------------
    #  BITBOARD ACCESS: RANKS AND FILES
    # -----------------------------------------------------


    def init_pieces(self):
        #manual entry of starting position... should be a better way to init once FEN mapping is complete
        self._set_white()
        self._set_black()

    def _set_white(self):
    
        self.white_R_bb |= set_bit(self.white_R_bb, 0)
        self.white_N_bb |= set_bit(self.white_N_bb, 1)
        self.white_B_bb |= set_bit(self.white_B_bb, 2)
        self.white_Q_bb |= set_bit(self.white_Q_bb, 3)
        self.white_K_bb |= set_bit(self.white_K_bb, 4)
        self.white_B_bb |= set_bit(self.white_B_bb, 5)
        self.white_N_bb |= set_bit(self.white_N_bb, 6)
        self.white_R_bb |= set_bit(self.white_R_bb, 7)
        
        for i in range (8,16):
            self.white_P_bb |= set_bit(self.white_P_bb, i)
   
    def _set_black(self):
 
        self.black_R_bb |= set_bit(self.black_R_bb, 56)
        self.black_N_bb |= set_bit(self.black_N_bb, 57)
        self.black_B_bb |= set_bit(self.black_B_bb, 58)
        self.black_Q_bb |= set_bit(self.black_Q_bb, 59)
        self.black_K_bb |= set_bit(self.black_K_bb, 60)
        self.black_B_bb |= set_bit(self.black_B_bb, 61)
        self.black_N_bb |= set_bit(self.black_N_bb, 62)
        self.black_R_bb |= set_bit(self.black_R_bb, 63)
        
        for i in range (48,56):
            self.black_P_bb |= set_bit(self.black_P_bb, i)
    

    # -----------------------------------------------------
    #  BOARD UPDATES
    # -----------------------------------------------------

    def update_bitboards(self, piece_map):
        for key, val in piece_map.items():

            # White Pieces
            if key == Piece.wP:
                self.white_P_bb = np.uint64(0)
                for bit in val:
                    self.white_P_bb |= set_bit(self.white_P_bb, np.uint64(bit))

            elif key == Piece.wR:
                self.white_R_bb = np.uint64(0)
                for bit in val:
                    self.white_R_bb |= set_bit(self.white_R_bb, np.uint64(bit))

            elif key == Piece.wN:
                self.white_N_bb = np.uint64(0)
                for bit in val:
                    self.white_N_bb |= set_bit(self.white_N_bb, np.uint64(bit))

            elif key == Piece.wB:
                self.white_B_bb = np.uint64(0)
                for bit in val:
                    self.white_B_bb |= set_bit(self.white_B_bb, np.uint64(bit))

            elif key == Piece.wQ:
                self.white_Q_bb = np.uint64(0)
                for bit in val:
                    self.white_Q_bb |= set_bit(self.white_Q_bb, np.uint64(bit))

            elif key == Piece.wK:
                self.white_K_bb = np.uint64(0)
                for bit in val:
                    self.white_K_bb |= set_bit(self.white_K_bb, np.uint64(bit))

            # Black Pieces
            if key == Piece.bP:
                self.black_P_bb = np.uint64(0)
                for bit in val:
                    self.black_P_bb |= set_bit(self.black_P_bb, np.uint64(bit))

            elif key == Piece.bR:
                self.black_R_bb = np.uint64(0)
                for bit in val:
                    self.black_R_bb |= set_bit(self.black_R_bb, np.uint64(bit))

            elif key == Piece.bN:
                self.black_N_bb = np.uint64(0)
                for bit in val:
                    self.black_N_bb |= set_bit(self.black_N_bb, np.uint64(bit))

            elif key == Piece.bB:
                self.black_B_bb = np.uint64(0)
                for bit in val:
                    self.black_B_bb |= set_bit(self.black_B_bb, np.uint64(bit))

            elif key == Piece.bQ:
                self.black_Q_bb = np.uint64(0)
                for bit in val:
                    self.black_Q_bb |= set_bit(self.black_Q_bb, np.uint64(bit))

            elif key == Piece.bK:
                self.black_K_bb = np.uint64(0)
                for bit in val:
                    self.black_K_bb |= set_bit(self.black_K_bb, np.uint64(bit))

    # -------------------------------------------------------------
    #  SLIDING PIECE MOVEMENT
    # -------------------------------------------------------------

    def get_bishop_attack_from(self, square):
        return
    def get_rook_attack_from(self, square):
        pass
    def get_queen_attack_from(self, square):
        pass

    # -------------------------------------------------------------
    #  PAWN MOVEMENTS
    # -------------------------------------------------------------

    def get_pawn_attack_from(self, square):
        pass

    # -------------------------------------------------------------
    #  KNIGHT MOVEMENTS
    # -------------------------------------------------------------

    def get_knight_attack_from(self, square):
        pass

    # -------------------------------------------------------------
    #  KING MOVEMENTS
    # -------------------------------------------------------------

    def get_king_attack_from(self, square):
        pass
