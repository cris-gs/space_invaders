# Space Invaders

Juego de Space Invaders en terminal hecho con Python.

## Estructura

- `main.py`: arranque del juego.
- `src/game.py`: estado central y loop principal.
- `src/input_handler.py`: escucha teclas con `pynput`.
- `src/renderer.py`: dibuja el tablero ASCII.
- `src/entities/`: entidades del juego.
- `src/logic/`: movimiento, acciones y colisiones.
- `src/config.py` y `settings.json`: configuracion.
- Los enemigos aparecen en una formacion mas grande y cambian de posicion en cada partida.

## Controles

- `W`, `A`, `S`, `D`: mover al jugador.
- `Space`: disparar.
- `Esc`: salir.

## Ejecutar

```bash
pip install -r requirements.txt
python main.py
```
