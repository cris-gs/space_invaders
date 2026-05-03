import threading
import time
import random
import json

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
        self.enemies = self._create_enemies()
        self.bullets: list[Bullet] = []
        self.running = True
        self.mode = "playing"
        self.score = 0
        self.max_ammo = 20
        self.ammo = self.max_ammo
        self.game_over_message = ""

    def _create_enemies(self) -> list[Enemy]:
        columns = list(range(2, self.width - 1, 2))
        rows = list(range(1, min(5, self.height // 2)))
        spawn_points = [(x, y) for y in rows for x in columns]
        enemy_count = min(12, len(spawn_points))

        selected_positions = random.sample(spawn_points, enemy_count)
        return [Enemy(x, y) for x, y in selected_positions]

    def update(self) -> None:
        if self.mode != "playing":
            return

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
            self.end_game("You cleared all enemies.")

    def shoot(self) -> None:
        if self.mode != "playing":
            return
        if self.ammo <= 0:
            return

        bullet_y = self.player.y - 1
        if bullet_y >= 0:
            self.bullets.append(Bullet(self.player.x, bullet_y))
            self.ammo -= 1
            if self.ammo == 0:
                self.end_game("You ran out of ammo.")

    def request_menu(self) -> None:
        self.mode = "menu"

    def resume(self) -> None:
        self.mode = "playing"

    def exit_game(self, message: str = "Game exited from menu.") -> None:
        self.end_game(message)

    def end_game(self, message: str) -> None:
        self.game_over_message = f"{message} Total points: {self.score}"
        self.running = False


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
            if self.state.mode == "menu":
                self._handle_menu()
                continue

            self.state.update()
            self.renderer.render(self.state)
            time.sleep(0.1)

        print()
        if self.state.game_over_message:
            print(self.state.game_over_message)

    def _handle_menu(self) -> None:
        while self.state.running and self.state.mode == "menu":
            self._print_menu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.state.resume()
            elif choice == "2":
                self._show_summary()
            elif choice == "3":
                self._show_configuration()
            elif choice == "4":
                self.state.exit_game()
            else:
                print("Invalid option. Press Enter to continue.")
                input()

    def _print_menu(self) -> None:
        from src.ui.terminal import clear_screen

        clear_screen()
        print("=== PAUSE MENU ===")
        print("1. Resume")
        print("2. Summary")
        print("3. Configuration")
        print("4. Exit")

    def _show_summary(self) -> None:
        from src.ui.terminal import clear_screen

        clear_screen()
        print("=== SUMMARY ===")
        print(f"Score: {self.state.score}")
        print(f"Ammo: {self.state.ammo}/{self.state.max_ammo}")
        print(f"Enemies remaining: {len(self.state.enemies)}")
        print(f"Bullets on screen: {len(self.state.bullets)}")
        print(f"Mode: {self.state.mode}")
        input("\nPress Enter to return to the menu...")

    def _show_configuration(self) -> None:
        from src.ui.terminal import clear_screen

        clear_screen()
        settings = self.config.read_settings()
        print("=== CONFIGURATION ===")
        print(json.dumps(settings, indent=4))
        input("\nPress Enter to return to the menu...")
