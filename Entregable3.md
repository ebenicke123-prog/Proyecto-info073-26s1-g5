# Entregable 3

## Proyecto
Las Aventuras de Capi

## Descripción general
Este documento resume los cambios hechos en el proyecto desde el avance 2 hasta el entregable 3.

## Cambios implementados desde Avance 2

### 1. Sistema de pantallas y flujo de juego
- Se implementó una pantalla de inicio con `ESPACIO` para comenzar el juego.
- Se agregó una pantalla de instrucciones accesible con la tecla `I`.
- Se añadió un estado de transición entre niveles con un contador visual.
- Se incluyeron pantallas de `Game Over` y `Victoria` con diseño gráfico propio.
- Se integró la tecla `ESC` para volver al menú principal desde el juego o desde cualquier pantalla.

### 2. Reglas de avance y condiciones de nivel
- En el primer nivel, el jugador debe recolectar todas las frutas antes de poder avanzar.
- Se agregó una puerta de nivel (`levelup`) que solo permite el paso una vez cumplida la condición del nivel.
- La condición de avance del segundo nivel depende de la apertura de la puerta azul y la recolección de llaves.

### 3. Mecánicas de objetos y obstáculos
- Se añadió la `pesa` como objeto necesario para poder caminar sobre los `lotos`.
- Si el jugador pisa un loto sin tener la pesa, se activa el `Game Over`.
- Se agregaron llaves amarillas y azules con puertas correspondientes.
- La puerta azul permanece visible en el mapa aunque se abra.

### 4. Enemigos y colisiones
- Se incluyeron enemigos con rutas predefinidas y movimiento automático.
- Si un enemigo toca al jugador, se activa el `Game Over`.
- Se mantuvo la lógica de colisión con paredes y elementos del mapa.

### 5. Mejora visual y de código
- Se usaron imágenes para las pantallas de inicio, instrucciones y victoria.
- Se sustituyeron los bloques anteriores por sprites de roca y otros elementos más coherentes.
- Se creó una función genérica `cargar_imagen` para limpiar la carga de recursos.
- Se reorganizó el dibujo del mapa y del HUD en funciones separadas (`dibujar_mapa`, `dibujar_hud`).
- Se mejoró la legibilidad y la estructura del código con funciones y menos repetición.

## Archivos modificados
- `Main.py`
- `README.md`

## Cómo probar
1. Abrir el proyecto en el directorio `Proyecto-info073-26s1-g5`.
2. Ejecutar:

```bash
python Main.py
```

3. Usar `ESPACIO` para iniciar, `I` para ver instrucciones, `ESC` para volver al inicio, y `R` para reiniciar tras perder o ganar.

