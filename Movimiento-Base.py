import pygame
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

TILE = 40
COLS = 15
FILAS = 15
ANCHO = TILE * COLS
ALTO  = TILE * FILAS + 60  # 60px extra para la barra de frutas

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa 15x15")
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO  = (0,   0,   0)
AZUL   = (70,  130, 180)
VERDE  = (34,  139,  34)

# Mapa: 0=piso, 2=arbol, 3=roca, 4=pino
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

# Frutas: lista de (col, fila, tipo)
# tipo: "sandia", "manzana", "naranja", "platano"
frutas = [
    {"col": 2,  "fila": 0,  "tipo": "naranja"},
    {"col": 1,  "fila": 10,  "tipo": "manzana"},
    {"col": 12, "fila": 2,  "tipo": "naranja"},
    {"col": 7,  "fila": 11, "tipo": "platano"},
    {"col": 3,  "fila": 6,  "tipo": "sandia"},
    {"col": 11, "fila": 13, "tipo": "manzana"},
    {"col": 6,  "fila": 9,  "tipo": "naranja"},
    {"col": 14, "fila": 5,  "tipo": "platano"},
]

# Contador de frutas recogidas
conteo = {"sandia": 0, "manzana": 0, "naranja": 0, "platano": 0}

# Posición del jugador
jugador_col  = 0
jugador_fila = 2

def es_pared(col, fila):
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLS:
        return True
    return MAPA[fila][col] in (2, 3, 4, 5)

fuente      = pygame.font.SysFont("monospace", 16)
fuente_hud  = pygame.font.SysFont("monospace", 18, bold=True)

# Cargar imágenes del mapa
img_pasto = pygame.image.load("imgPasto.png").convert()
img_pasto = pygame.transform.scale(img_pasto, (TILE, TILE))

img_arbol = pygame.image.load("imgarbol.png").convert_alpha()
img_arbol = pygame.transform.scale(img_arbol, (TILE, TILE))

img_roca = pygame.image.load("imgroca.png").convert_alpha()
img_roca = pygame.transform.scale(img_roca, (TILE, TILE))

img_pino = pygame.image.load("imgpino.png").convert_alpha()
img_pino = pygame.transform.scale(img_pino, (TILE, TILE))

img_arbusto = pygame.image.load("imgarbusto.png").convert_alpha()
img_arbusto = pygame.transform.scale(img_arbusto, (TILE, TILE))

# Cargar imágenes de frutas (tamaño en mapa y tamaño en HUD)
FTILE = 30  # tamaño fruta en el mapa
FHUD  = 28  # tamaño fruta en la barra

imgs_fruta = {
    "sandia":  pygame.transform.scale(pygame.image.load("IMGsandia.png").convert_alpha(),  (FTILE, FTILE)),
    "manzana": pygame.transform.scale(pygame.image.load("IMGmanzana.png").convert_alpha(), (FTILE, FTILE)),
    "naranja": pygame.transform.scale(pygame.image.load("IMGnaranja.png").convert_alpha(), (FTILE, FTILE)),
    "platano": pygame.transform.scale(pygame.image.load("IMGplatano.png").convert_alpha(), (FTILE, FTILE)),
}
imgs_hud = {
    "sandia":  pygame.transform.scale(pygame.image.load("IMGsandia.png").convert_alpha(),  (FHUD, FHUD)),
    "manzana": pygame.transform.scale(pygame.image.load("IMGmanzana.png").convert_alpha(), (FHUD, FHUD)),
    "naranja": pygame.transform.scale(pygame.image.load("IMGnaranja.png").convert_alpha(), (FHUD, FHUD)),
    "platano": pygame.transform.scale(pygame.image.load("IMGplatano.png").convert_alpha(), (FHUD, FHUD)),
}

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            nueva_col  = jugador_col
            nueva_fila = jugador_fila

            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                nueva_fila -= 1
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                nueva_fila += 1
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                nueva_col -= 1
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                nueva_col += 1

            if not es_pared(nueva_col, nueva_fila):
                jugador_col  = nueva_col
                jugador_fila = nueva_fila

                # Revisar si hay fruta en la nueva casilla
                for f in frutas[:]:
                    if f["col"] == jugador_col and f["fila"] == jugador_fila:
                        conteo[f["tipo"]] += 1
                        frutas.remove(f)

    # --- Dibujar mapa ---
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

    # --- Dibujar frutas en el mapa ---
    for f in frutas:
        fx = f["col"] * TILE + (TILE - FTILE) // 2
        fy = f["fila"] * TILE + (TILE - FTILE) // 2
        pantalla.blit(imgs_fruta[f["tipo"]], (fx, fy))

    # --- Dibujar jugador ---
    px = jugador_col * TILE
    py = jugador_fila * TILE
    pygame.draw.rect(pantalla, AZUL, (px + 4, py + 4, TILE - 8, TILE - 8), border_radius=6)

    # --- Barra de frutas ---
    barra_y = FILAS * TILE
    pygame.draw.rect(pantalla, VERDE, (0, barra_y, ANCHO, 60))

    label = fuente_hud.render("Frutas:", True, BLANCO)
    pantalla.blit(label, (8, barra_y + 18))

    x_offset = 90
    for tipo in ["sandia", "manzana", "naranja", "platano"]:
        pantalla.blit(imgs_hud[tipo], (x_offset, barra_y + 16))
        num = fuente_hud.render(f"x{conteo[tipo]}", True, BLANCO)
        pantalla.blit(num, (x_offset + FHUD + 2, barra_y + 20))
        x_offset += FHUD + 45

    pygame.display.update()
    reloj.tick(60)
