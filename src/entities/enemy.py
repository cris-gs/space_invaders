import random


ENEMY_SYMBOLS = ("☠", "◆", "■", "✦")


class Enemy:
    def __init__(self, x: int, y: int, symbol: str | None = None):
        self.x = x
        self.y = y
        self.symbol = symbol or random.choice(ENEMY_SYMBOLS)
        self.alive = True
