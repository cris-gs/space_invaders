from src.logic.movement import move_player


class GameActions:
    def __init__(self, game_state):
        self.game_state = game_state

    def _can_control(self) -> bool:
        return self.game_state.mode == "playing"

    def move_up(self, event: str):
        if event == "press" and self._can_control():
            move_player(self.game_state.player, 0, -1, self.game_state.width, self.game_state.height)

    def move_down(self, event: str):
        if event == "press" and self._can_control():
            move_player(self.game_state.player, 0, 1, self.game_state.width, self.game_state.height)

    def move_left(self, event: str):
        if event == "press" and self._can_control():
            move_player(self.game_state.player, -1, 0, self.game_state.width, self.game_state.height)

    def move_right(self, event: str):
        if event == "press" and self._can_control():
            move_player(self.game_state.player, 1, 0, self.game_state.width, self.game_state.height)

    def shoot(self, event: str):
        if event == "press" and self._can_control():
            self.game_state.shoot()

    def open_menu(self, event: str):
        if event == "press":
            self.game_state.request_menu()
