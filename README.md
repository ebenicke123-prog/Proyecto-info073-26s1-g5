# Las Aventuras de Capi

`Las Aventuras de Capi` es un juego de aventura y laberinto hecho con Python y Pygame. El jugador controla a Capi, una capibara que debe recolectar frutas, encontrar llaves, usar la pesa y escapar de los enemigos.

## Qué incluye este proyecto

- Juego principal en `Main.py`
- Mapas y niveles en el código
- Sprites y pantallas en `Assets/`
- Menú inicial, instrucciones, transición entre niveles y pantalla de victoria
- Dos niveles con condiciones de avance distintas

## Cómo jugar

### Objetivo

- Nivel 1: recoge todas las frutas para poder avanzar.
- Nivel 2: usa llaves y evita enemigos hasta llegar a la salida.
- Si un enemigo te atrapa o pisas un loto sin la pesa, pierdes.

### Controles

- `ESPACIO`: iniciar el juego desde el menú principal
- `I`: abrir/cerrar la pantalla de instrucciones
- `ESC`: volver al menú principal
- `W` / `↑`: mover hacia arriba
- `A` / `←`: mover hacia la izquierda
- `S` / `↓`: mover hacia abajo
- `D` / `→`: mover hacia la derecha
- `R`: reiniciar después de un Game Over o al ganar

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Abre una terminal en la carpeta del proyecto.
2. Instala Pygame:

```bash
pip install pygame
```

3. Ejecuta el juego:

```bash
python Main.py
```

> Si tu sistema usa `python3` en lugar de `python`, usa `python3 Main.py`.

## Estructura del proyecto

```
Proyecto-info073-26s1-g5/
├── Assets/
│   ├── Bloques/       # Tiles del mapa y bloques del terreno
│   ├── Elementos/     # Frutas, llaves, pesa y sprites HUD
│   ├── Entidades/     # Jugador y enemigos
│   └── pantallas/     # Menú, instrucciones y victoria
├── bin/               # Archivos secundarios o ejecutables
├── Main.py            # Lógica principal del juego
├── README.md          # Documentación del proyecto
└── .gitignore
```

## Mecánicas principales

- `Frutas`: recolección obligatoria en el primer nivel.
- `Llaves`: abren puertas amarillas y puertas azules.
- `Pesa`: permite subir a los lotos sin morir.
- `Lotos`: solo se pueden pisar si tienes la pesa activa.
- `Puerta azul`: puede bloquear el camino hasta que obtengas la llave azul.
- `Puerta nivel`: aparece solo cuando se cumplen los requisitos del nivel.
- `Enemigos`: patrullan rutas fijas.

## Pantallas del juego

- **Pantalla principal**: inicio del juego y acceso a instrucciones.
- **Instrucciones**: muestra objetivos y controles.
- **Juego**: partida activa.
- **Transición**: breve pantalla entre nivel 1 y nivel 2.
- **Victoria**: se muestra al completar el último nivel.
- **Game Over**: aparece al perder.

## Mejoras posibles

Este juego es una base lista para expandir con:

- más niveles
- enemigos nuevos
- animaciones del personaje
- sonidos y música
- sistema de puntuación
- guardado de récords
