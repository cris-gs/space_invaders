import threading
import time

from src.config import Config
from src.entities.bullet import Bullet
from src.entities.enemy import Enemy
from src.entities.player import Player
from src.input_handler import InputHandler
from src.logic.actions import GameActions
from src.logic.collisions import bullet_hits_enemy
from src.renderer import Renderer


class GameState:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.player = Player(width // 2, height - 1)
        self.enemies = [Enemy(5, 2), Enemy(10, 2), Enemy(15, 2)]
        self.bullets: list[Bullet] = []
        self.running = True
        self.score = 0

    def update(self) -> None:
        updated_bullets: list[Bullet] = []

        for bullet in self.bullets:
            bullet.move()
            if bullet.y < 0:
                continue

            hit_enemy = None
            for enemy in self.enemies:
                if bullet_hits_enemy(bullet, enemy):
                    hit_enemy = enemy
                    break

            if hit_enemy:
                hit_enemy.alive = False
                self.score += 1
                continue

            updated_bullets.append(bullet)

        self.bullets = updated_bullets
        self.enemies = [enemy for enemy in self.enemies if enemy.alive]

        if not self.enemies:
            self.running = False

    def shoot(self) -> None:
        bullet_y = self.player.y - 1
        if bullet_y >= 0:
            self.bullets.append(Bullet(self.player.x, bullet_y))


class Game:
    def __init__(self):
        self.config = Config()
        self.keybindings = self.config.read_keybindings()
        self.state = GameState(width=30, height=15)
        self.actions = GameActions(self.state)
        self.input_handler = InputHandler(self.keybindings, self.actions)
        self.renderer = Renderer(self.state.width, self.state.height)

    def run(self) -> None:
        listener_thread = threading.Thread(target=self.input_handler.start_listener, daemon=True)
        listener_thread.start()

        while self.state.running:
            self.state.update()
            self.renderer.render(self.state)
            time.sleep(0.1)

        print()
        print(f"Ganaste. Score final: {self.state.score}")
