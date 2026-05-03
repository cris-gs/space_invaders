from pynput import keyboard


SPECIAL_KEYS_MAP = {
    "space": keyboard.Key.space,
    "esc": keyboard.Key.esc,
    "enter": keyboard.Key.enter,
    "up": keyboard.Key.up,
    "down": keyboard.Key.down,
    "left": keyboard.Key.left,
    "right": keyboard.Key.right,
}


class InputHandler:
    def __init__(self, keybindings: dict, game_actions) -> None:
        self.bindings = {action: self._get_key(key) for action, key in keybindings.items()}
        self.game_actions = game_actions

    def start_listener(self):
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()

    def _get_key(self, key: str):
        return SPECIAL_KEYS_MAP.get(key, key)

    def _match_key(self, key, action_key) -> bool:
        if isinstance(action_key, str) and hasattr(key, "char"):
            return key.char == action_key
        return key == action_key

    def _on_press(self, key) -> None:
        if key == keyboard.Key.esc:
            action_method = getattr(self.game_actions, "open_menu", None)
            if action_method:
                action_method("press")
            return

        for action, action_key in self.bindings.items():
            if self._match_key(key, action_key):
                action_method = getattr(self.game_actions, action, None)
                if action_method:
                    action_method("press")

    def _on_release(self, key) -> None:
        for action, action_key in self.bindings.items():
            if self._match_key(key, action_key):
                action_method = getattr(self.game_actions, action, None)
                if action_method:
                    action_method("release")
