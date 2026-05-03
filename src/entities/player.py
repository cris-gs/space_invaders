class Player:
    def __init__(self, x: int, y: int, symbol: str = "A"):
        self.x = x
        self.y = y
        self.symbol = symbol

    def move(self, dx: int, dy: int, width: int, height: int) -> None:
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < width:
            self.x = new_x
        if 0 <= new_y < height:
            self.y = new_y
