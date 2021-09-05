import numpy as np

LIGHT_SQUARES = 0x55AA55AA55AA55AA
DARK_SQUARES  = 0xAA55AA55AA55AA55
    
"Translates squares (algebraic notation) into map positions (integers)"""

HOT = np.uint64(1)

class Square:
    A1 = 0
    B1 = 1
    C1 = 2
    D1 = 3
    E1 = 4
    F1 = 5
    G1 = 6
    H1 = 7

    A2 = 8
    B2 = 9
    C2 = 10
    D2 = 11
    E2 = 12
    F2 = 13
    G2 = 14
    H2 = 15

    A3 = 16
    B3 = 17
    C3 = 18
    D3 = 19
    E3 = 20
    F3 = 21
    G3 = 22
    H3 = 23

    A4 = 24
    B4 = 25
    C4 = 26
    D4 = 27
    E4 = 28
    F4 = 29
    G4 = 30
    H4 = 31

    A5 = 32
    B5 = 33
    C5 = 34
    D5 = 35
    E5 = 36
    F5 = 37
    G5 = 38
    H5 = 39

    A6 = 40
    B6 = 41
    C6 = 42
    D6 = 43
    E6 = 44
    F6 = 45
    G6 = 46
    H6 = 47

    A7 = 48
    B7 = 49
    C7 = 50
    D7 = 51
    E7 = 52
    F7 = 53
    G7 = 54
    H7 = 55

    A8 = 56
    B8 = 57
    C8 = 58
    D8 = 59
    E8 = 60
    F8 = 61
    G8 = 62
    H8 = 63    


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

    hexA = 0x0101010101010101
    hexB = 0x0202020202020202
    hexC = 0x0404040404040404
    hexD = 0x0808080808080808
    hexE = 0x1010101010101010
    hexF = 0x2020202020202020
    hexG = 0x4040404040404040
    hexH = 0x8080808080808080

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

    hex1 = 0x00000000000000FF
    hex2 = 0x000000000000FF00
    hex3 = 0x0000000000FF0000
    hex4 = 0x00000000FF000000
    hex5 = 0x000000FF00000000
    hex6 = 0x0000FF0000000000
    hex7 = 0x00FF000000000000
    hex8 = 0xFF00000000000000

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
