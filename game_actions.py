class GameActions:
    """
    This class defines the actions that can be performed in the game.
    """

    def move_up(self, event: str):
        if event == "press":
            print("Moving up")
        else:
            print("Stop moving up")

    def move_down(self, event: str):
        if event == "press":
            print("Moving down")
        else:
            print("Stop moving down")

    def move_left(self, event: str):
        if event == "press":
            print("Moving left")
        else:
            print("Stop moving left")

    def move_right(self, event: str):
        if event == "press":
            print("Moving right")
        else:
            print("Stop moving right")

    def shoot(self, event: str):
        if event == "press":
            print("Shooting")
        else:
            print("Stop shooting")
