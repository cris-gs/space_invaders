# Space Invaders

A terminal Space Invaders game built with Python.

## Structure

- `main.py`: game entry point.
- `src/game.py`: central game state and main loop.
- `src/input_handler.py`: listens for keyboard input with `pynput`.
- `src/renderer.py`: draws the ASCII board.
- `src/entities/`: game entities.
- `src/logic/`: movement, actions, and collisions.
- `src/config.py` and `settings.json`: configuration.
- Enemies spawn in a larger formation and change positions on every run.

## Controls

- `W`, `A`, `S`, `D`: move the player.
- `Space`: shoot until ammo runs out.
- `Esc`: open the pause menu.

## Pause Menu

From the pause menu you can:

- Resume the game.
- View a short match summary.
- Open the current configuration.
- Exit the game.

## Ammo

The player starts with a fixed ammo pool. When ammo reaches zero, the run ends and the final score is shown.

## Run

```bash
pip install -r requirements.txt
python main.py
```
