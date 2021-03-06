class SquarePosition:
    
    "Translates squares (algebraic notation) into map positions (integers)"""
    a1 = 0
    b1 = 1
    c1 = 2
    d1 = 3
    e1 = 4
    f1 = 5
    g1 = 6
    h1 = 7
    
    a2 = 8
    b2 = 9
    c2 = 10
    d2 = 11
    e2 = 12
    f2 = 13
    g2 = 14
    h2 = 15

    a3 = 16
    b3 = 17
    c3 = 18
    d3 = 19
    e3 = 20
    f3 = 21
    g3 = 22
    h3 = 23

    a4 = 24
    b4 = 25
    c4 = 26
    d4 = 27
    e4 = 28
    f4 = 29
    g4 = 30
    h4 = 31

    a5 = 32
    b5 = 33
    c5 = 34
    d5 = 35
    e5 = 36
    f5 = 37
    g5 = 38
    h5 = 39

    a6 = 40
    b6 = 41
    c6 = 42
    d6 = 43
    e6 = 44
    f6 = 45
    g6 = 46
    h6 = 47

    a7 = 48
    b7 = 49
    c7 = 50
    d7 = 51
    e7 = 52
    f7 = 53
    g7 = 54
    h7 = 55

    a8 = 56
    b8 = 57
    c8 = 58
    d8 = 59
    e8 = 60
    f8 = 61
    g8 = 62
    h8 = 63


class FileSqures:
    """Provides integer representaiton of each file (AN)"""
    
    a = {0,  8, 16, 24, 32, 40, 48, 56}
    b = {1,  9, 17, 25, 33, 41, 49, 57}
    c = {2, 10, 18, 26, 34, 42, 50, 58}
    d = {3, 11, 19, 27, 35, 43, 51, 59}
    e = {4, 12, 20, 28, 36, 44, 52, 60}
    f = {5, 13, 21, 29, 37, 45, 53, 61}
    g = {6, 14, 22, 30, 38, 46, 54, 62}
    h = {7, 15, 23, 31, 39, 47, 55, 63}

    files = [a,b,c,d,e,f,g,h,g]

class RankSquares:
    """Provides integer representation of each rank (AN)"""

    _1 = { 0,  1,  2,  3,  4,  5,  6,  7}
    _2 = { 8,  9, 10, 11, 12, 13, 14, 15}
    _3 = {16, 17, 18, 19, 20, 21, 22, 23}
    _4 = {24, 25, 26, 27, 28, 29, 30, 31}
    _5 = {32, 33, 34, 35, 36, 37, 38, 39}
    _6 = {40, 41, 42, 43, 44, 45, 46, 47}
    _7 = {48, 49, 50, 51, 52, 53, 54, 55}
    _8 = {56, 57, 58, 59, 60, 61, 62, 63}

    ranks = [_1,_2,_3,_4,_5,_6,_7,_8]

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
