class Bullet:
    def __init__(self, x: int, y: int, direction: int = -1, symbol: str = "│"):
        self.x = x
        self.y = y
        self.direction = direction
        self.symbol = symbol

    def move(self) -> None:
        self.y += self.direction
