from controller import Controller
from setting import Setting
from pynput import keyboard

# Initialize the classes
setting = Setting()
keybindings = setting.read_keybindings()

controller = Controller(keybindings)

# Start keyboard listener
with keyboard.Listener(on_press=controller.on_press) as listener:
    listener.join()
