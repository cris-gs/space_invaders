from game_actions import GameActions
from key_handler import KeyHandler
from setting import Setting
from pynput import keyboard

# Initialize the classes
setting = Setting()
keybindings = setting.read_keybindings()

game_actions = GameActions()
key_handler = KeyHandler(keybindings, game_actions)

# Start keyboard listener
with keyboard.Listener(
    on_press=key_handler.on_press,
    on_release=key_handler.on_release) as listener:
    listener.join()
