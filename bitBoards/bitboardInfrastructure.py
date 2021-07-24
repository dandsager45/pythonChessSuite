#!user/bin/env python
"""bitboardInfrastructure.py: initial creation of an infrastructure of bitboardsfor chess engine processing"""

import string
import numpy as np

from constants import Piece, File, Rank

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

#function to bitwise-and bitboards <- is this still needed?
#function to map fen -> boardstate
#pawn moves
#legal move list & captures
#execute moves 
#refactor moves to own module
#examine issue with +7 & -9 and revert hack if possible
#unit tests?

def make_empty_uint64_bitmap():
    """
    Returns a numpy array of one uint64 zero value 
    :return:
    """
    return np.zeros(1, dtype=np.uint64)

def get_bitboard_as_bytyes(bitboard):
    return bitboard.tobytes()

def get_binary_string(bitboard):
    return format(bitboard, 'b').zfill(BOARD_SQURES)

def set_bit(bitboard, bit):
    return bitboard | ( 1 << bit )

def clear_bit(bitboard, bit):
    return bitboard & ~(1 << bit )

def pretty_print_bb(bitboard):
    bb = get_binary_string(bitboard)    
    val = ''
    display_rank = BOARD_SIZE
    board = [bb[i:i + 8] for i in range( 0, len(bb), BOARD_SIZE)]
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
    for char in string.ascii_uppercase[:BOARD_SIZE]:
        val += f' {char}'
    print(val)



class Board:

    def __init__(self):
       
        self.board_size = BOARD_SIZE #64 squares 
                
        #white piece bitboards
        self.white_P_bb = make_empty_uint64_bitmap()#[0]
        self.white_N_bb = make_empty_uint64_bitmap()#[0]
        self.white_B_bb = make_empty_uint64_bitmap()#[0]
        self.white_R_bb = make_empty_uint64_bitmap()#[0]
        self.white_Q_bb = make_empty_uint64_bitmap()#[0]
        self.white_K_bb = make_empty_uint64_bitmap()#[0]
        
        #black piece bitboards
        self.black_P_bb = make_empty_uint64_bitmap()#[0]
        self.black_N_bb = make_empty_uint64_bitmap()#[0]
        self.black_B_bb = make_empty_uint64_bitmap()#[0]
        self.black_R_bb = make_empty_uint64_bitmap()#[0]
        self.black_Q_bb = make_empty_uint64_bitmap()#[0]
        self.black_K_bb = make_empty_uint64_bitmap()#[0]
                            
        #put the pieces onto the bitboards
        self.init_pieces()

        #rank & file bitboards
        self.rank_1_bb = make_empty_uint64_bitmap()#[0]
        self.rank_2_bb = make_empty_uint64_bitmap()#[0]
        self.rank_3_bb = make_empty_uint64_bitmap()#[0]
        self.rank_4_bb = make_empty_uint64_bitmap()#[0]
        self.rank_5_bb = make_empty_uint64_bitmap()#[0]
        self.rank_6_bb = make_empty_uint64_bitmap()#[0]
        self.rank_7_bb = make_empty_uint64_bitmap()#[0] 
        self.rank_8_bb = make_empty_uint64_bitmap()#[0] 
        self.file_a_bb = make_empty_uint64_bitmap()#[0] 
        self.file_b_bb = make_empty_uint64_bitmap()#[0]
        self.file_c_bb = make_empty_uint64_bitmap()#[0]
        self.file_d_bb = make_empty_uint64_bitmap()#[0] 
        self.file_e_bb = make_empty_uint64_bitmap()#[0] 
        self.file_f_bb = make_empty_uint64_bitmap()#[0] 
        self.file_g_bb = make_empty_uint64_bitmap()#[0] 
        self.file_h_bb = make_empty_uint64_bitmap()#[0] 

        self.set_rank_file_bb()

        
        #static knight attacks (should this be independent?)
        self.knight_bbs = self._make_knight_bb()


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
        return 1 - self.occupied_squares_bb
    
    @property
    def queenside_bb(self):
        return self.file_a_bb | self.file_b_bb | self.file_c_bb | self.file_d_bb

    @property
    def kingside_bb(self):
        return self.file_e_bb | self.file_f_bb | self.file_g_bb | self.file_h_bb

    @property
    def center_files_bb(self):
        return self.file_c_bb | self.file_d_bb | self.file_e_bb | self.file_f_bb

    @property
    def flanks_bb(self):
        return self.file_a_bb | self.file_h_bb

    @property
    def center_squares_bb(self):
        return (self.file_d_bb | self.file_e_bb ) & (self.rank_4_bb | self.rank_5_bb)

    
    @property
    def white_P_east_attacks(self):
        #white pawn east attacks are north east (+9) AND NOT the A file
        return (self.white_P_bb << 9 ) & (~self.file_a_bb)
            
    @property
    def white_P_west_attacks(self):
        #white pawn west attacks are north west (+7) AND NOT the H file
        return (self.white_P_bb << 7) & (~self.file_h_bb)

    @property
    def white_pawn_attacks(self):
        return self.white_P_east_attacks | self.white_P_west_attacks

    @property
    def black_P_east_attacks(self):
        #white pawn east attacks are south east (-7) AND NOT the A file
        return (self.black_P_bb >> 7 ) & (~self.file_a_bb)

    @property
    def black_P_west_attacks(self):
        #white pawn west attacks are north west (-9) AND NOT the H file
        return (self.black_P_bb >> 9) & (~self.file_h_bb)
    
    @property
    def black_pawn_attacks(self):
        return self.black_P_east_attacks | self.black_P_west_attacks




    #not sure if I will need this later, or if is completely obsolete
    def update_occupied_squares_bb(self):
        result = np.zeros(64, dtype="byte")
        for board in self.occupied_squares_bb:
            result = np.bitwise_or(board, result, dtype="byte")
        self.occupied_squares_bb = result
        return result
    

    def init_pieces(self):
        #manual entry of starting position... should be a better way to init once FEN mapping is complete
        self._set_white()
        self._set_black()


    def update_position(self, piece_map):
        for key, val in piece_map.items():
            if key == Piece.wP: 
                self.white_P_bb.fill(0)
                np.put(self.white_P_bb, list(val), 1)
            elif key == Piece.wR: 
                self.white_R_bb.fill(0)
                np.put(self.white_R_bb, list(val), 1)
            elif key == Piece.wN: 
                self.white_N_bb.fill(0)
                np.put(self.white_N_bb, list(val), 1)
            elif key == Piece.wB: 
                self.white_B_bb.fill(0)
                np.put(self.white_B_bb, list(val), 1)
            elif key == Piece.wQ: 
                self.white_Q_bb.fill(0)
                np.put(self.white_Q_bb, list(val), 1)
            elif key == Piece.wK: 
                self.white_K_bb.fill(0)
                np.put(self.white_K_bb, list(val), 1)
            elif key == Piece.bP: 
                self.black_P_bb.fill(0)
                np.put(self.black_P_bb, list(val), 1)
            elif key == Piece.bR: 
                self.black_R_bb.fill(0)
                np.put(self.black_R_bb, list(val), 1)
            elif key == Piece.bN: 
                self.black_N_bb.fill(0)
                np.put(self.black_N_bb, list(val), 1)
            elif key == Piece.bB: 
                self.black_B_bb.fill(0)
                np.put(self.black_B_bb, list(val), 1)
            elif key == Piece.bQ: 
                self.black_Q_bb.fill(0)
                np.put(self.black_Q_bb, list(val), 1)
            elif key == Piece.bK: 
                self.black_K_bb.fill(0)
                np.put(self.black_K_bb, list(val), 1)


    ########################################Piece Movement###################################
    #Sliding  piece movement (Queen, King, Rook, Bishop)

    #reference for sliding rays: chessprogramming.org/On_an_empty_Board
    def make_east_ray(self, square):
        for i in range(square, BOARD_SQUARES, 1):
            self.attack_bb[i] = 1
            if not (i+1) % 8: 
                return
    #Commented out text is broken
    def make_northwest_ray(self, square):
        for i in range(square, BOARD_SQUARES, 7):
            self.attack_bb[i] = 1
            #if not (i+1) % 8: 
            #    return
            if not i % 8: 
                return

    def make_north_ray(self, square):
        for i in range(square, BOARD_SQUARES, 8):
            self.attack_bb[i] = 1
            if not (i+1) % 8: 
                return

    def make_northeast_ray(self, square):
        for i in range(square, BOARD_SQUARES, 9):
            self.attack_bb[i] = 1
            if not (i+1) % 8: 
                return

    def make_west_ray(self, square):
        for i in range(square, 0, -1):
            self.attack_bb[i] = 1
            if not (i+1) % 8: 
                return

    def make_southeast_ray(self, square):
        for i in range(square, 0, -7):
            self.attack_bb[i] = 1
            if not (i+1) % 8: 
                return

    def make_south_ray(self, square):
        for i in range(square, 0, -8):
            self.attack_bb[i] = 1
            if not (i+1) % 8: 
                return
    #Commented Out text is Broken
    def make_southwest_ray(self, square):
        for i in range(square, 0, -9):
            self.attack_bb[i] = 1
            #if not (i+1) % 8: 
            #    return
            if not i % 8:
                return
    ###############################################Generate piece attacking BBs######################
    #Queen (& potentially king) attack maps can be created by combining bishop & rook attack maps
    ###PAWN ATTACKS###
    def _make_pawn_attack_bb(self):
        wP_east_attack_map = {}
        wP_west_attack_map = {}
        bP_east_attack_map = {}
        bP_west_attack0_map = {}

        for i in range(BOARD_SQUARES):
            wP_east_attack_map[i] = self._white_pawn_east_attack(i)
            wP_west_attack_map[i] = self._white_pawn_west_attack(i)
            bP_east_attack_map[i] = self._black_pawn_east_attack(i)
            bP_west_attack_map[i] = self._black_pawn_west_attack(i)
        
        return wP_east_attack_map, wP_west_attack_map, bP_east_attack_map, bP_west_attack_map 

    @staticmethod
    def _white_pawn_east_attack(self, square):
        if sqaure in File.H:
            pass
        return np.array(square + 9)

    def _white_pawn_west_attack(self, square):
        if sqaure in File.A:
            pass
        return np.array(square + 7)

    def _black_pawn_east_attack(self, square):
        if sqaure in File.H:
            pass
        return np.array(square - 9)

    def _black_pawn_west_attack(self, square):
        if sqaure in File.A:
            pass
        return np.array(square - 7)


    ###BISHOP ATTACKS###

    def get_bishop_attack_from(self, square):
        pass

    ###ROOK ATTACKS###
    def get_rook_attack_from(self, square):
        pass
        



    #Knight Movement
    def _make_knight_bb(self):
        knight_attack_map = {}
        for i in range(BOARD_SQUARES):
            knight_attack_map[i] = self._knight_attacks(i)
        return knight_attack_map

    def _knight_attacks(self,square):
        row_mask = make_empty_uint64_bitmap()#[0]
        col_mask = make_empty_uint64_bitmap()#[0]
        agg_mask = make_empty_uint64_bitmap()#[0]

        #overflow file mask -> block off overflow knight moves
        if square in File.A:
            col_mask = self.file_g_bb | self.file_h_bb
        elif square in File.B:
            col_mask = self.file_h_bb
        elif square in File.G:
            col_mask = self.file_a_bb
        elif square in File.H:
            col_mask = self.file_a_bb | self.file_b_bb

        #overflow ranks mask
        if square in Rank.x1:
            row_mask = self.rank_8_bb | self.rank_7_bb
        elif square in Rank.x2:
            row_mask = self.rank_8_bb
        #aggregate mask
        if row_mask.any() or col_mask.any():
            agg_mask = row_mask | col_mask

        attacks = make_empty_uint64_bitmap() 

        for i in [0,6,15,17,10,-6,-15,-17,-10]:
            if square + i >= BOARD_SQUARES or square + i < 0:
                #Skip OOB
                continue
            attacks[square + i] = 1
        if agg_mask.any():
            #bit shift the attacks by mask
            attacks = attacks >> agg_mask
        return attacks


    def _empty_bb(self):
        return np.zeros(BOARD_SQUARES, "byte")

    def set_rank_file_bb(self):
        #todo: faster numpy methods
        for val in File.A: self.file_a_bb |= set_bit(self.file_a_bb, val)
        for val in File.B: self.file_b_bb |= set_bit(self.file_b_bb, val)
        for val in File.C: self.file_c_bb |= set_bit(self.file_c_bb, val)
        for val in File.D: self.file_d_bb |= set_bit(self.file_d_bb, val)
        for val in File.E: self.file_e_bb |= set_bit(self.file_e_bb, val) 
        for val in File.F: self.file_f_bb |= set_bit(self.file_f_bb, val) 
        for val in File.G: self.file_g_bb |= set_bit(self.file_g_bb, val) 
        for val in File.H: self.file_h_bb |= set_bit(self.file_h_bb, val) 

        for val in Rank.x1: self.rank_1_bb |= set_bit(self.rank_1_bb, val)
        for val in Rank.x2: self.rank_2_bb |= set_bit(self.rank_2_bb, val)
        for val in Rank.x3: self.rank_3_bb |= set_bit(self.rank_3_bb, val)
        for val in Rank.x4: self.rank_4_bb |= set_bit(self.rank_4_bb, val)
        for val in Rank.x5: self.rank_5_bb |= set_bit(self.rank_5_bb, val)
        for val in Rank.x6: self.rank_6_bb |= set_bit(self.rank_6_bb, val)
        for val in Rank.x7: self.rank_7_bb |= set_bit(self.rank_7_bb, val)
        for val in Rank.x8: self.rank_8_bb |= set_bit(self.rank_8_bb, val)

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
    



