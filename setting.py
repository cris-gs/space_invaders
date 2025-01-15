import json

class Setting:
    def read_settings(self) -> dict:
        """
        Read the settings from the settings file.

        Returns:
        - dict: The settings.
        """
        settings = {}
        with open("space_invaders/settings.json", "r") as file:
            settings = json.load(file)
        return settings

    def read_keybindings(self) -> dict:
        """
        Read the keybindings from the settings file.

        Returns:
        - dict: The keybindings.
        """
        keybindings = {}
        with open("space_invaders/settings.json", "r") as file:
            settings = json.load(file)
            keybindings = settings['keybindings']
        return keybindings

    def update_settings(self, settings) -> None:
        """
        Update the settings in the settings file.

        Args:
        - settings (dict): The settings.
        """
        with open('space_invaders/settings.json', 'w') as f:
            for key, value in settings.items():
                f.write(f'{key}={value}\n')
