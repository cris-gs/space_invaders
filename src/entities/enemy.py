class Enemy:
    def __init__(self, x: int, y: int, symbol: str = "M"):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.alive = True
