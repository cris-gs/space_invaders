from game_actions import GameActions
from pynput import keyboard

SPECIAL_KEYS_MAP = {
    "space": keyboard.Key.space,
    "esc": keyboard.Key.esc,
    "enter": keyboard.Key.enter,
    "up": keyboard.Key.up,
    "down": keyboard.Key.down,
    "left": keyboard.Key.left,
    "right": keyboard.Key.right
}

class KeyHandler:
    def __init__(self, keybindings: dict, game_actions: GameActions) -> None:
        """
        Initialize the KeyHandler class.

        Args:
        -  keybindings (dict): Example:
                {
                    "move_up": "w",
                    "move_down": "s",
                    "move_left": "a",
                    "move_right": "d",
                    "shoot": "space"
                }
        - game_actions (GameActions): An instance of the GameActions class.
        """

        self.bindings = {
            action: self._get_key(key)
            for action, key in keybindings.items()
        }
        self.game_actions = game_actions

    def _get_key(self, key: str) -> keyboard.Key:
        """
        Return the key if it is a special key, otherwise return the key itself.

        Args:
        - key (str): The key to get.

        Returns:
        - keyboard.Key: The key.
        """
        return SPECIAL_KEYS_MAP.get(key, key)

    def _match_key(self, key, action_key) -> bool:
        """
        Check if the pressed key matches the action key.

        Args:
        - key: The pressed key.
        - action_key: The action key to match against.

        Returns:
        - bool: True if they match, False otherwise.
        """
        if isinstance(action_key, str) and hasattr(key, "char"):
            return key.char == action_key
        return key == action_key

    def on_press(self, key) -> None:
        """
        Handle key press events.

        Args:
        - key: The pressed key.
        """
        for action, action_key in self.bindings.items():
            if self._match_key(key, action_key):
                action_method = getattr(self.game_actions, action, None)
                if action_method:
                    action_method("press")

    def on_release(self, key) -> None:
        """
        Handle key release events.

        Args:
        - key: The released key.
        """
        if key == keyboard.Key.esc:
            print("Exiting...")
            return False

        for action, action_key in self.bindings.items():
            if self._match_key(key, action_key):
                action_method = getattr(self.game_actions, action, None)
                if action_method:
                    action_method("release")
