import pygame
import sys
 
pygame.init()
 
TILE = 40
COLS = 15
FILAS = 15
ANCHO = TILE * COLS
ALTO = TILE * FILAS
 
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa 15x15")
reloj = pygame.time.Clock()
 
# Colores
BLANCO  = (255, 255, 255)
NEGRO   = (0,   0,   0)
AZUL    = (70,  130, 180)
GRIS    = (200, 200, 200)
GRIS2   = (180, 180, 180)
 
# Mapa: 0 = piso, 2 = arbol (colision)
MAPA = [
    [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
    [4,4,4,0,0,0,0,0,5,0,0,0,0,0,5],
    [3,3,3,4,0,0,0,0,5,5,5,0,3,0,5],
    [0,0,0,3,4,0,0,0,0,0,5,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
]
 
# Posición del jugador en casillas (columna, fila)
jugador_col = 0
jugador_fila = 2
 
def es_pared(col, fila):
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLS:
        return True
    return MAPA[fila][col] in (2, 3, 4)  # 2=arbol, 3=roca, 4=pino
 
fuente = pygame.font.SysFont("monospace", 16)
 
# Cargar imágenes
img_pasto = pygame.image.load(r"C:\Users\ebeni\Downloads\imgPasto (1).png").convert()
img_pasto = pygame.transform.scale(img_pasto, (TILE, TILE))
 
img_arbol = pygame.image.load(r"C:\Users\ebeni\Downloads\imgarbol.png").convert_alpha()
img_arbol = pygame.transform.scale(img_arbol, (TILE, TILE))
 
img_roca = pygame.image.load(r"C:\Users\ebeni\Downloads\imgroca.png").convert_alpha()
img_roca = pygame.transform.scale(img_roca, (TILE, TILE))
 
img_pino = pygame.image.load(r"C:\Users\ebeni\Downloads\imgPino.png").convert_alpha()
img_pino = pygame.transform.scale(img_pino, (TILE, TILE))
 
img_arbusto = pygame.image.load(r"C:\Users\ebeni\Downloads\imgarbusto.png").convert_alpha()
img_arbusto = pygame.transform.scale(img_arbusto, (TILE, TILE))
 

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        if evento.type == pygame.KEYDOWN:
 
            nueva_col = jugador_col
            nueva_fila = jugador_fila
 
            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                nueva_fila -= 1
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                nueva_fila += 1
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                nueva_col -= 1
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                nueva_col += 1
 
            # Solo mueve si la casilla destino no es pared
            if not es_pared(nueva_col, nueva_fila):
                jugador_col = nueva_col
                jugador_fila = nueva_fila
 
    # Dibujar mapa
    for fila in range(FILAS):
        for col in range(COLS):
            x = col * TILE
            y = fila * TILE
            pantalla.blit(img_pasto, (x, y))
            if MAPA[fila][col] == 2:
                pantalla.blit(img_arbol, (x, y))
            elif MAPA[fila][col] == 3:
                pantalla.blit(img_roca, (x, y))
            elif MAPA[fila][col] == 4:
                pantalla.blit(img_pino, (x, y))
            elif MAPA[fila][col] == 5:
                pantalla.blit(img_arbusto, (x, y))
 
    # Dibujar jugador
    px = jugador_col * TILE
    py = jugador_fila * TILE
    pygame.draw.rect(pantalla, AZUL, (px + 4, py + 4, TILE - 8, TILE - 8), border_radius=6)
 
    # HUD
    texto = fuente.render(f"Col: {jugador_col}  Fila: {jugador_fila}  |  WASD para mover", True, NEGRO, BLANCO)
    pantalla.blit(texto, (4, 4))
 
    pygame.display.update()
    reloj.tick(60) 0, 255), (x, y, 40, 40))

    pygame.display.update()
