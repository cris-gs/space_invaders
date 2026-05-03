from src.logic.movement import move_player


class GameActions:
    def __init__(self, game_state):
        self.game_state = game_state

    def move_up(self, event: str):
        if event == "press":
            move_player(self.game_state.player, 0, -1, self.game_state.width, self.game_state.height)

    def move_down(self, event: str):
        if event == "press":
            move_player(self.game_state.player, 0, 1, self.game_state.width, self.game_state.height)

    def move_left(self, event: str):
        if event == "press":
            move_player(self.game_state.player, -1, 0, self.game_state.width, self.game_state.height)

    def move_right(self, event: str):
        if event == "press":
            move_player(self.game_state.player, 1, 0, self.game_state.width, self.game_state.height)

    def shoot(self, event: str):
        if event == "press":
            self.game_state.shoot()
