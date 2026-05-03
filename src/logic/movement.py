from src.entities.player import Player


def move_player(player: Player, dx: int, dy: int, width: int, height: int) -> None:
    player.move(dx, dy, width, height)


def advance_bullets(bullets) -> None:
    for bullet in bullets:
        bullet.move()
