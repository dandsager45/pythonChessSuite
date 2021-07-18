class Move:   
    """
    Represents the motion of a piece from an origin squre to a target square
    """
    def __init__(self, piece, moves, is_capture, is_promotion):
        self.piece = piece
        self.from_sq = moves[0]
        self.to_sq = moves[1]
        self.is_capture = is_capture
        self.is_promotion = is_promotion
        
    def is_promotoion(self):
    #get the promotion type
        pass
