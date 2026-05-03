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
- `Space`: shoot.
- `Esc`: quit.

## Run

```bash
pip install -r requirements.txt
python main.py
```
