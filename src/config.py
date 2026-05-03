import json
from pathlib import Path


SETTINGS_FILE = Path(__file__).resolve().parents[1] / "settings.json"


class Config:
    def read_settings(self) -> dict:
        with SETTINGS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    def read_keybindings(self) -> dict:
        settings = self.read_settings()
        return settings.get("keybindings", {})

    def update_settings(self, settings) -> None:
        with SETTINGS_FILE.open("w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)


Setting = Config
