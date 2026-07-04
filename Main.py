import pygame
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

TILE  = 40
COLS  = 15
FILAS = 15
ANCHO = TILE * COLS
ALTO  = TILE * FILAS + 70

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa 15x15")
reloj = pygame.time.Clock()

BLANCO  = (255, 255, 255)
NEGRO   = (0,   0,   0)
AZUL    = (70,  130, 180)
VERDE   = (34,  139,  34)
ROJO    = (200,  30,  30)
AMARILLO= (255, 220,   0)

# Mapa: 0=piso, 2=arbol, 3=roca, 4=pino
MAPA = [
    [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,6,6],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,6,6],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
    [4,4,4,0,0,0,0,0,5,0,0,0,0,0,5],
    [3,3,3,4,0,0,0,0,5,5,5,0,3,0,5],
    [0,0,0,3,4,0,0,0,0,0,5,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
]

# Lotos: posiciones fijas en el mapa
LOTOS = [
    {"col": 12, "fila": 2},
    {"col": 13, "fila": 2},
]

# Pesa: posición en el mapa
pesa = {"col": 10, "fila": 2, "activa": True}

# Frutas
frutas_iniciales = [
    {"col": 5,  "fila": 3,  "tipo": "sandia"},
    {"col": 9,  "fila": 7,  "tipo": "manzana"},
    {"col": 12, "fila": 4,  "tipo": "naranja"},
    {"col": 7,  "fila": 11, "tipo": "platano"},
    {"col": 3,  "fila": 6,  "tipo": "sandia"},
    {"col": 11, "fila": 13, "tipo": "manzana"},
    {"col": 6,  "fila": 9,  "tipo": "naranja"},
    {"col": 14, "fila": 5,  "tipo": "platano"},
]

# Llave amarilla: última columna (14), fila 2
llave = {"col": 14, "fila": 2}
# Puerta amarilla: columna 5, última fila (14)
puerta = {"col": 4, "fila": 14}

# Llave azul: columna 0, fila 13
llave_azul = {"col": 0, "fila": 13}
# Puerta azul: columna 12, fila 8
puerta_azul = {"col": 12, "fila": 7}

def estado_inicial():
    return {
        "jugador_col":  0,
        "jugador_fila": 2,
        "frutas": [dict(f) for f in frutas_iniciales],
        "conteo": {"sandia": 0, "manzana": 0, "naranja": 0, "platano": 0},
        "tiene_pesa": False,
        "pesa_activa": True,
        "tiene_llave": False,
        "llave_activa": True,
        "puerta_abierta": False,
        "tiene_llave_azul": False,
        "llave_azul_activa": True,
        "puerta_azul_abierta": False,
        "game_over": False,
        "ganaste": False,
    }

estado = estado_inicial()

def es_pared(col, fila):
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLS:
        return True
    # La puerta bloquea si no está abierta y no tienes la llave
    if col == puerta["col"] and fila == puerta["fila"]:
        return not estado["tiene_llave"] and not estado["puerta_abierta"]
    if col == puerta_azul["col"] and fila == puerta_azul["fila"]:
        return not estado["tiene_llave_azul"] and not estado["puerta_azul_abierta"]
    return MAPA[fila][col] in (2, 3, 4, 5, 6)

fuente      = pygame.font.SysFont("monospace", 16)
fuente_hud  = pygame.font.SysFont("monospace", 18, bold=True)
fuente_go   = pygame.font.SysFont("monospace", 60, bold=True)
fuente_sub  = pygame.font.SysFont("monospace", 24)

FTILE = 30
FHUD  = 28
img_colum = pygame.transform.scale(pygame.image.load("imgcolumna.png").convert(),        (TILE, TILE))
img_pasto = pygame.transform.scale(pygame.image.load("imgPasto.png").convert(),        (TILE, TILE))
img_arbol = pygame.transform.scale(pygame.image.load("imgarbol.png").convert_alpha(),  (TILE, TILE))
img_roca  = pygame.transform.scale(pygame.image.load("imgroca.png").convert_alpha(),   (TILE, TILE))
img_pino  = pygame.transform.scale(pygame.image.load("imgpino.png").convert_alpha(),   (TILE, TILE))
img_loto   = pygame.transform.scale(pygame.image.load("imglotoPiso.png").convert_alpha(), (TILE, TILE))
img_arbusto = pygame.transform.scale(pygame.image.load("imgarbusto.png").convert_alpha(), (TILE, TILE))
img_pesa  = pygame.transform.scale(pygame.image.load("IMGpesa.png").convert_alpha(),   (FTILE, FTILE))

imgs_fruta = {
    t: pygame.transform.scale(pygame.image.load(f"IMG{t}.png").convert_alpha(), (FTILE, FTILE))
    for t in ["sandia", "manzana", "naranja", "platano"]
}
imgs_hud = {
    t: pygame.transform.scale(pygame.image.load(f"IMG{t}.png").convert_alpha(), (FHUD, FHUD))
    for t in ["sandia", "manzana", "naranja", "platano"]
}
img_pesa_hud = pygame.transform.scale(pygame.image.load("IMGpesa.png").convert_alpha(), (FHUD, FHUD))
img_llave     = pygame.transform.scale(pygame.image.load("IMGllaveamarilla.png").convert_alpha(), (FTILE, FTILE))
img_llave_hud = pygame.transform.scale(pygame.image.load("IMGllaveamarilla.png").convert_alpha(), (FHUD, FHUD))
img_puerta    = pygame.transform.scale(pygame.image.load("imgpuertamarilla.png").convert_alpha(), (TILE, TILE))
img_llave_azul     = pygame.transform.scale(pygame.image.load("IMGllaveazul.png").convert_alpha(), (FTILE, FTILE))
img_llave_azul_hud = pygame.transform.scale(pygame.image.load("IMGllaveazul.png").convert_alpha(), (FHUD, FHUD))
img_puerta_azul    = pygame.transform.scale(pygame.image.load("imgpuertaazul.png").convert_alpha(), (TILE, TILE))

def dibujar_ganaste():
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    pantalla.blit(overlay, (0, 0))
    txt_g  = fuente_go.render("GANASTE!", True, AMARILLO)
    txt_r  = fuente_sub.render("Presiona R para reiniciar", True, BLANCO)
    pantalla.blit(txt_g, txt_g.get_rect(center=(ANCHO//2, ALTO//2 - 40)))
    pantalla.blit(txt_r, txt_r.get_rect(center=(ANCHO//2, ALTO//2 + 30)))
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    pantalla.blit(overlay, (0, 0))

    txt_go  = fuente_go.render("GAME OVER", True, ROJO)
    txt_sub = fuente_sub.render("Pisaste el loto sin la pesa", True, BLANCO)
    txt_r   = fuente_sub.render("Presiona R para reiniciar", True, AMARILLO)

    pantalla.blit(txt_go,  txt_go.get_rect(center=(ANCHO//2, ALTO//2 - 60)))
    pantalla.blit(txt_sub, txt_sub.get_rect(center=(ANCHO//2, ALTO//2 + 10)))
    pantalla.blit(txt_r,   txt_r.get_rect(center=(ANCHO//2, ALTO//2 + 50)))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            # Reiniciar con R en game over
            if estado["game_over"] or estado["ganaste"]:
                if evento.key == pygame.K_r:
                    estado = estado_inicial()
                continue

            nueva_col  = estado["jugador_col"]
            nueva_fila = estado["jugador_fila"]

            if evento.key == pygame.K_w or evento.key == pygame.K_UP:    nueva_fila -= 1
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:  nueva_fila += 1
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:  nueva_col  -= 1
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT: nueva_col  += 1

            if not es_pared(nueva_col, nueva_fila):
                estado["jugador_col"]  = nueva_col
                estado["jugador_fila"] = nueva_fila

                # Recoger fruta
                for f in estado["frutas"][:]:
                    if f["col"] == nueva_col and f["fila"] == nueva_fila:
                        estado["conteo"][f["tipo"]] += 1
                        estado["frutas"].remove(f)

                # Recoger pesa
                if (estado["pesa_activa"] and
                        nueva_col == pesa["col"] and nueva_fila == pesa["fila"]):
                    estado["tiene_pesa"] = True
                    estado["pesa_activa"] = False

                # Recoger llave amarilla
                if (estado["llave_activa"] and
                        nueva_col == llave["col"] and nueva_fila == llave["fila"]):
                    estado["tiene_llave"] = True
                    estado["llave_activa"] = False

                # Recoger llave azul
                if (estado["llave_azul_activa"] and
                        nueva_col == llave_azul["col"] and nueva_fila == llave_azul["fila"]):
                    estado["tiene_llave_azul"] = True
                    estado["llave_azul_activa"] = False

                # Revisar puerta amarilla
                if nueva_col == puerta["col"] and nueva_fila == puerta["fila"]:
                    if estado["tiene_llave"]:
                        estado["puerta_abierta"] = True

                # Revisar puerta azul
                if nueva_col == puerta_azul["col"] and nueva_fila == puerta_azul["fila"]:
                    if estado["tiene_llave_azul"]:
                        estado["puerta_azul_abierta"] = True
                # Revisar loto
                for loto in LOTOS:
                    if loto["col"] == nueva_col and loto["fila"] == nueva_fila:
                        if not estado["tiene_pesa"]:
                            estado["game_over"] = True
                        # Con pesa puede pasar sin perderla

    # ---- DIBUJAR ----
    # Mapa
    for fila in range(FILAS):
        for col in range(COLS):
            x = col * TILE
            y = fila * TILE
            pantalla.blit(img_pasto, (x, y))
            if MAPA[fila][col] == 2: pantalla.blit(img_arbol, (x, y))
            elif MAPA[fila][col] == 3: pantalla.blit(img_roca, (x, y))
            elif MAPA[fila][col] == 4: pantalla.blit(img_pino, (x, y))
            elif MAPA[fila][col] == 5: pantalla.blit(img_arbusto, (x, y))
            elif MAPA[fila][col] == 6: pantalla.blit(img_colum, (x, y))

    # Lotos (siempre visibles, peligrosos al peso >= 5)
    for loto in LOTOS:
        pantalla.blit(img_loto, (loto["col"] * TILE, loto["fila"] * TILE))

    # Pesa en el mapa
    if estado["pesa_activa"]:
        px_p = pesa["col"] * TILE + (TILE - FTILE) // 2
        py_p = pesa["fila"] * TILE + (TILE - FTILE) // 2
        pantalla.blit(img_pesa, (px_p, py_p))

    # Frutas en el mapa
    for f in estado["frutas"]:
        fx = f["col"] * TILE + (TILE - FTILE) // 2
        fy = f["fila"] * TILE + (TILE - FTILE) // 2
        pantalla.blit(imgs_fruta[f["tipo"]], (fx, fy))

    # Llave amarilla en el mapa
    if estado["llave_activa"]:
        lx = llave["col"] * TILE + (TILE - FTILE) // 2
        ly = llave["fila"] * TILE + (TILE - FTILE) // 2
        pantalla.blit(img_llave, (lx, ly))

    # Puerta amarilla en el mapa
    if not estado["puerta_abierta"]:
        pantalla.blit(img_puerta, (puerta["col"] * TILE, puerta["fila"] * TILE))

    # Llave azul en el mapa
    if estado["llave_azul_activa"]:
        lx2 = llave_azul["col"] * TILE + (TILE - FTILE) // 2
        ly2 = llave_azul["fila"] * TILE + (TILE - FTILE) // 2
        pantalla.blit(img_llave_azul, (lx2, ly2))

    # Puerta azul en el mapa
    if not estado["puerta_azul_abierta"]:
        pantalla.blit(img_puerta_azul, (puerta_azul["col"] * TILE, puerta_azul["fila"] * TILE))

    # Jugador
    px = estado["jugador_col"] * TILE
    py = estado["jugador_fila"] * TILE
    pygame.draw.rect(pantalla, AZUL, (px + 4, py + 4, TILE - 8, TILE - 8), border_radius=6)

    # Barra inferior (más alta para dos filas)
    barra_y = FILAS * TILE
    pygame.draw.rect(pantalla, VERDE, (0, barra_y, ANCHO, 60))

    # --- Fila 1: pesa y llaves (y=barra_y + 4) ---
    x_items = 8

    if estado["tiene_pesa"]:
        pantalla.blit(img_pesa_hud, (x_items, barra_y + 4))
        txt_p = fuente_hud.render("x1", True, AMARILLO)
        pantalla.blit(txt_p, (x_items + FHUD + 2, barra_y + 8))
        x_items += FHUD + 28

    if estado["tiene_llave"]:
        pantalla.blit(img_llave_hud, (x_items, barra_y + 4))
        x_items += FHUD + 6

    if estado["tiene_llave_azul"]:
        pantalla.blit(img_llave_azul_hud, (x_items, barra_y + 4))
        x_items += FHUD + 6

    # --- Fila 2: frutas (y=barra_y + 32) ---
    x_offset = 8
    for tipo in ["sandia", "manzana", "naranja", "platano"]:
        pantalla.blit(imgs_hud[tipo], (x_offset, barra_y + 32))
        num = fuente_hud.render(f"x{estado['conteo'][tipo]}", True, BLANCO)
        pantalla.blit(num, (x_offset + FHUD + 2, barra_y + 36))
        x_offset += FHUD + 45

    if estado["game_over"]:
        dibujar_game_over()

    if estado["ganaste"]:
        dibujar_ganaste()

    pygame.display.update()
    reloj.tick(60)
