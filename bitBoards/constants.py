import numpy as np

LIGHT_SQUARES = 0x55AA55AA55AA55AA
DARK_SQUARES  = 0xAA55AA55AA55AA55
    
"Translates squares (algebraic notation) into map positions (integers)"""

HOT = np.uint64(1)

class Square:
    A1 = np.uint(0) 
    B1 = np.uint(1)
    C1 = np.uint(2)
    D1 = np.uint(3)
    E1 = np.uint(4)
    F1 = np.uint(5)
    G1 = np.uint(6)
    H1 = np.uint(7)

    A2 = np.uint(8)
    B2 = np.uint(9)
    C2 = np.uint(10)
    D2 = np.uint(11)
    E2 = np.uint(12)
    F2 = np.uint(13)
    G2 = np.uint(14)
    H2 = np.uint(15)

    A3 = np.uint(16)  
    B3 = np.uint(17)
    C3 = np.uint(18)
    D3 = np.uint(19)
    E3 = np.uint(20)
    F3 = np.uint(21)
    G3 = np.uint(22)
    H3 = np.uint(23)

    A4 = np.uint(24)
    B4 = np.uint(25)
    C4 = np.uint(26)
    D4 = np.uint(27)
    E4 = np.uint(28)
    F4 = np.uint(29)
    G4 = np.uint(30)
    H4 = np.uint(31)

    A5 = np.uint(32)
    B5 = np.uint(33)
    C5 = np.uint(34)
    D5 = np.uint(35)
    E5 = np.uint(36)
    F5 = np.uint(37)
    G5 = np.uint(38)
    H5 = np.uint(39)

    A6 = np.uint(40)
    B6 = np.uint(41)
    C6 = np.uint(42)
    D6 = np.uint(43)
    E6 = np.uint(44)
    F6 = np.uint(45)
    G6 = np.uint(46)
    H6 = np.uint(47)

    A7 = np.uint(48)
    B7 = np.uint(49)
    C7 = np.uint(50)
    D7 = np.uint(51)
    E7 = np.uint(52)
    F7 = np.uint(53)
    G7 = np.uint(54)
    H7 = np.uint(55)

    A8 = np.uint(56)
    B8 = np.uint(57)
    C8 = np.uint(58)
    D8 = np.uint(59)
    E8 = np.uint(60)
    F8 = np.uint(61)
    G8 = np.uint(62)
    H8 = np.uint(63)   


class File:
    """Provides integer representaiton of each file (AN)"""
    
    A = {0,  8, 16, 24, 32, 40, 48, 56}
    B = {1,  9, 17, 25, 33, 41, 49, 57}
    C = {2, 10, 18, 26, 34, 42, 50, 58}
    D = {3, 11, 19, 27, 35, 43, 51, 59}
    E = {4, 12, 20, 28, 36, 44, 52, 60}
    F = {5, 13, 21, 29, 37, 45, 53, 61}
    G = {6, 14, 22, 30, 38, 46, 54, 62}
    H = {7, 15, 23, 31, 39, 47, 55, 63}

    hexA = np.uint64(0x0101010101010101)
    hexB = np.uint64(0x0202020202020202)
    hexC = np.uint64(0x0404040404040404)
    hexD = np.uint64(0x0808080808080808)
    hexE = np.uint64(0x1010101010101010)
    hexF = np.uint64(0x2020202020202020)
    hexG = np.uint64(0x4040404040404040)
    hexH = np.uint64(0x8080808080808080)

    files = [ A, B, C, D, E, F, G, H ]

class Rank:
    """Provides integer representation of each rank (AN)"""

    x1 = { 0,  1,  2,  3,  4,  5,  6,  7}
    x2 = { 8,  9, 10, 11, 12, 13, 14, 15}
    x3 = {16, 17, 18, 19, 20, 21, 22, 23}
    x4 = {24, 25, 26, 27, 28, 29, 30, 31}
    x5 = {32, 33, 34, 35, 36, 37, 38, 39}
    x6 = {40, 41, 42, 43, 44, 45, 46, 47}
    x7 = {48, 49, 50, 51, 52, 53, 54, 55}
    x8 = {56, 57, 58, 59, 60, 61, 62, 63}

    hex1 = np.uint64(0x00000000000000FF)
    hex2 = np.uint64(0x000000000000FF00)
    hex3 = np.uint64(0x0000000000FF0000)
    hex4 = np.uint64(0x00000000FF000000)
    hex5 = np.uint64(0x000000FF00000000)
    hex6 = np.uint64(0x0000FF0000000000)
    hex7 = np.uint64(0x00FF000000000000)
    hex8 = np.uint64(0xFF00000000000000)

    ranks = [ x1, x2, x3, x4, x5, x6, x7, x8]

class Color:
    
    WHITE = 0
    BLACK = 1

class Piece:
    """Provides an enumeration for each type of piece"""
    EMPTY = 0
    
    wP = 1
    wR = 2
    wN = 3
    wB = 4
    wQ = 5
    wK = 6
    
    bP = 7
    bR = 8
    bN = 9
    bB = 10
    bQ = 11
    bK = 12

    white_pieces = {wP, wR, wN, wB, wQ, wK}
    black_pieces = {bP, bR, bN, bB, bQ, bK}
