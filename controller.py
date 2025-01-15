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

class Controller:
    def __init__(self, keybindings: dict) -> None:
        """
        Initialize the Controller class.

        Args:
        - keybindings (dict): The keybindings.
        """
        self.move_up = self.get_key(keybindings['move_up'])
        self.move_down = self.get_key(keybindings['move_down'])
        self.move_left = self.get_key(keybindings['move_left'])
        self.move_right = self.get_key(keybindings['move_right'])
        self.shoot = self.get_key(keybindings['shoot'])
        self.exit = self.get_key(keybindings['exit'])

    def get_key(self, key: str) -> keyboard.Key:
        """
        Return the key if it is a special key, otherwise return the key itself.

        Args:
        - key (str): The key to get.

        Returns:
        - keyboard.Key: The key.
        """
        if key in SPECIAL_KEYS_MAP:
            return SPECIAL_KEYS_MAP[key]
        else:
            return key

    def on_press(self, key: keyboard.Key) -> None:
        """
        Handle the key press event.

        Args:
        - key (keyboard.Key): The key that was pressed.
        """
        if isinstance(key, keyboard.Key):
            if key == self.shoot:
                print(f"Key '{self.shoot}' pressed!")
            elif key == self.exit:
                print("Leaving!")
                return False
        elif isinstance(key, keyboard.KeyCode):
            if key.char == self.move_up:
                print(f"Key '{self.move_up}' pressed!")
            elif key.char == self.move_down:
                print(f"Key '{self.move_down}' pressed!")
            elif key.char == self.move_left:
                print(f"Key '{self.move_left}' pressed!")
            elif key.char == self.move_right:
                print(f"Key '{self.move_right}' pressed!")
