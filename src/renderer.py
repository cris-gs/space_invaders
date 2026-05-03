from src.ui.terminal import clear_screen


class Renderer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.canvas = self._create_canvas()

    def _create_canvas(self):
        return [[" " for _ in range(self.width)] for _ in range(self.height)]

    def clear_canvas(self):
        self.canvas = self._create_canvas()

    def draw_player(self, player):
        self.draw_object(player.x, player.y, player.symbol)

    def draw_enemies(self, enemies):
        for enemy in enemies:
            self.draw_object(enemy.x, enemy.y, enemy.symbol)

    def draw_bullets(self, bullets):
        for bullet in bullets:
            self.draw_object(bullet.x, bullet.y, bullet.symbol)

    def draw_object(self, x: int, y: int, symbol: str):
        if 0 <= y < self.height and 0 <= x < self.width:
            self.canvas[y][x] = symbol

    def render(self, game_state):
        self.clear_canvas()
        self.draw_player(game_state.player)
        self.draw_enemies(game_state.enemies)
        self.draw_bullets(game_state.bullets)
        clear_screen()
        self._print_border_top()
        for row in self.canvas:
            print(f"|{''.join(row)}|")
        self._print_border_bottom()
        print()
        print(f"Score: {game_state.score}")
        print(f"Ammo: {game_state.ammo}/{game_state.max_ammo}")

    def _print_border_top(self):
        print(f"+{'-' * self.width}+")

    def _print_border_bottom(self):
        print(f"+{'-' * self.width}+")
