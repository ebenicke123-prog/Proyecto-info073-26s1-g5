import pygame
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
#FUENTES

fuente     = pygame.font.SysFont("monospace", 16)
fuente_hud = pygame.font.SysFont("monospace", 18, bold=True)
fuente_go  = pygame.font.SysFont("monospace", 60, bold=True)
fuente_sub = pygame.font.SysFont("monospace", 24)
fuente_niv = pygame.font.SysFont("monospace", 48, bold=True)
#TAMAÑOS

TILE  = 40
COLS  = 15
FILAS = 15
ANCHO = TILE * COLS
ALTO  = TILE * FILAS + 70

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Capi: Aventura en el Laberinto")
reloj = pygame.time.Clock()

#COLORES
BLANCO   = (255, 255, 255)
NEGRO    = (0,   0,   0)
AZUL     = (70,  130, 180)
VERDE    = (34,  139,  34)
ROJO     = (200,  30,  30)
AMARILLO = (255, 220,   0)
NARANJA  = (220, 100,  20)

# ─── MAPAS ───────────────────────────────────────────────────────────────────
MAPA1 = [
    [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,2,0,0,2,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [5,5,0,2,0,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,2,0,0,2,0,0,0,2,6,6],
    [0,0,0,2,0,0,0,0,0,2,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,0,0,0,0,2,6,6],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
    [4,4,4,0,0,0,0,0,5,0,0,0,0,0,5],
    [3,3,3,4,0,0,0,0,5,5,5,0,3,0,5],
    [0,0,0,3,4,0,0,0,0,0,5,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
]

# Nivel 2: laberinto (tomado del segundo código)
# Nivel 2: más abierto y fácil que un laberinto (solo islas de obstáculos)
MAPA2 = [
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [4,0,4,4,0,0,0,0,0,0,0,4,4,0,4],
    [4,0,4,4,0,0,0,0,0,0,0,4,4,0,4],
    [4,0,0,0,0,0,4,4,4,0,0,0,0,0,4],
    [4,0,0,0,0,0,4,0,4,0,0,0,0,0,4],
    [4,0,4,4,0,0,4,0,4,0,0,4,4,0,4],
    [4,0,4,4,0,0,0,0,0,0,0,4,4,0,4],
    [4,0,4,4,0,0,4,0,4,0,0,4,4,0,4],
    [4,0,0,0,0,0,4,0,4,0,0,0,0,0,4],
    [4,0,0,0,0,0,4,4,4,0,0,0,0,0,4],
    [4,0,4,4,0,0,0,0,0,0,0,4,4,0,4],
    [4,0,4,4,0,0,0,0,0,0,0,4,4,0,4],
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
]

LOTOS1 = [
    {"col": 12, "fila": 2}, {"col": 13, "fila": 2},
    {"col": 2,  "fila": 0}, {"col": 9,  "fila": 4},
    {"col": 9,  "fila": 13}, {"col": 5,  "fila": 11},
]
LOTOS2 = [
    {"col": 5, "fila": 4},
    {"col": 9, "fila": 4},
    {"col": 7, "fila": 9},
    {"col": 4, "fila": 13},
    {"col": 12, "fila": 1},
    {"col": 2, "fila":4},
    {"col": 2, "fila": 5},
    {"col": 2, "fila": 9},
    {"col": 2, "fila": 10},
    {"col": 13, "fila": 2},
    {"col": 12, "fila": 4},
    {"col": 12, "fila": 5},
    {"col": 12, "fila": 9},
    {"col": 12, "fila": 10},
    {"col": 10, "fila": 13},

]

    
ENEMIGO1_RUTA = [
    (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),
    (11,6),(11,7),(11,8),(11,9),
    (10,9),(9,9),(8,9),(7,9),(6,9),(5,9),(4,9),(3,9),(2,9),(1,9),(0,9),
    (0,8),(0,7),(0,6),(0,5),
]

ENEMIGO3_RUTA = [
    (7,7),(6,7),(5,7),(5,6),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(6,11),(7,11),(8,11),(9,11),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,6),(9,7),(8,7),(7,7),
]

ENEMIGO4_RUTA = [
    (1,6),
    (1,5),(1,4),(1,3),(1,2),(1,1),
    (2,1),(2,3),(2,1),
    (1,1),
    (1,2),(1,3),(1,4),(1,5),
    (1,6),
]
ENEMIGO5_RUTA = [
    (13,6),
    (13,5),(13,4),(13,3),(13,2),(13,1),
    (12,1),(11,1),
    (12,1),(13,1),
    (13,2),(13,3),(13,4),(13,5),
    (13,6),
]
ENEMIGO6_RUTA = [
    (1,8),
    (1,9),(1,10),(1,11),(1,12),(1,13),
    (2,13),(3,13),(2,13),
    (1,13),
    (1,12),(1,11),(1,10),(1,9),
    (1,8),
]
ENEMIGO7_RUTA = [
    (13,8),
    (13,9),(13,10),(13,11),(13,12),(13,13),
    (12,13),(11,13),
    (12,13),(13,13),
    (13,12),(13,11),(13,10),(13,9),
    (13,8),
]

# ─── DATOS POR NIVEL ─────────────────────────────────────────────────────────
niveles = [
    {
        "mapa": MAPA1,
        "lotos": LOTOS1,
        "pesa": {"col": 13, "fila": 13},
        "frutas": [
            {"col": 4,  "fila": 0,  "tipo": "manzana"},
            {"col": 7,  "fila": 2,  "tipo": "sandia"},
            {"col": 2,  "fila": 6,  "tipo": "naranja"},
            {"col": 5,  "fila": 5,  "tipo": "platano"},
            {"col": 11, "fila": 4,  "tipo": "sandia"},
            {"col": 10, "fila": 7,  "tipo": "manzana"},
            {"col": 6,  "fila": 11, "tipo": "naranja"},
            {"col": 5,  "fila": 13, "tipo": "platano"},
        ],
        "llave":       {"col": 14, "fila": 2},
        "puerta":      {"col": 4,  "fila": 14},
        "llave_azul":  {"col": 0, "fila": 13},
        "puerta_azul": {"col": 12, "fila": 7},
        "puerta_nivel":{"col": 14, "fila": 7},  # puerta al nivel 2
        "enemigos": [ENEMIGO1_RUTA],
        "jugador_inicio": (0, 2),
    },
    {
        "mapa": MAPA2,
        "lotos": LOTOS2,
        "pesa": {"col": 7, "fila": 7},
        "frutas": [
            {"col": 3,  "fila": 1,  "tipo": "manzana"},
            {"col": 11, "fila": 4,  "tipo": "sandia"},
            {"col": 4,  "fila": 7,  "tipo": "naranja"},
            {"col": 10, "fila": 7,  "tipo": "platano"},
            {"col": 5,  "fila": 10, "tipo": "sandia"},
            {"col": 9,  "fila": 10, "tipo": "manzana"},
            {"col": 3,  "fila": 13, "tipo": "naranja"},
            {"col": 11, "fila": 13, "tipo": "platano"},
        ],
        "llave":       {"col": 13, "fila": 1},
        "puerta":      {"col": 7,  "fila": 6},
        "llave_azul":  {"col": 7, "fila": 5},
        "puerta_azul": {"col": 7,  "fila": 1},
        "puerta_nivel": None,
        "enemigos": [ENEMIGO3_RUTA, ENEMIGO4_RUTA, ENEMIGO5_RUTA, ENEMIGO6_RUTA, ENEMIGO7_RUTA],
        "jugador_inicio": (1, 1),
    },
]

# ─── ENEMIGO ─────────────────────────────────────────────────────────────────
class Enemigo:
    def __init__(self, ruta):
        self.ruta   = ruta
        self.idx    = 0
        self.col    = ruta[0][0]
        self.fila   = ruta[0][1]
        self.timer  = 0
        self.speed  = 30  # frames entre pasos

    def update(self):
        self.timer += 1
        if self.timer >= self.speed:
            self.timer = 0
            self.idx   = (self.idx + 1) % len(self.ruta)
            self.col   = self.ruta[self.idx][0]
            self.fila  = self.ruta[self.idx][1]

    def toca_jugador(self, jcol, jfila):
        return self.col == jcol and self.fila == jfila

def nuevos_enemigos(nivel_idx):
    n = niveles[nivel_idx]
    rutas = n.get("enemigos", [n.get("enemigo_ruta")])
    return [Enemigo(ruta) for ruta in rutas if ruta is not None]

def frutas_completas():
    return len(estado["frutas"]) == 0

def estado_inicial(nivel_idx=0):
    n = niveles[nivel_idx]
    return {
        "nivel": nivel_idx,
        "jugador_col":  n["jugador_inicio"][0],
        "jugador_fila": n["jugador_inicio"][1],
        "frutas": [dict(f) for f in n["frutas"]],
        "conteo": {"sandia": 0, "manzana": 0, "naranja": 0, "platano": 0},
        "tiene_pesa": False,
        "pesa_activa": True,
        "tiene_llave": False,
        "llave_activa": True,
        "puerta_abierta": False,
        "tiene_llave_azul": False,
        "llave_azul_activa": True,
        "puerta_azul_abierta": False,
        "puerta_nivel_abierta": False,
        "game_over": False,
        "ganaste": False,
        "causa_go": None,  # "loto" o "enemigo"
        "tiempo": 0,       # en frames
        "contando": True,  # para de contar al ganar
    }

estado  = estado_inicial(0)
enemigos = nuevos_enemigos(0)

def nivel_actual():
    return niveles[estado["nivel"]]

def mapa_actual():
    return nivel_actual()["mapa"]

def es_pared(col, fila):
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLS:
        return True
    n = nivel_actual()
    if col == n["puerta"]["col"] and fila == n["puerta"]["fila"]:
        return not estado["tiene_llave"] and not estado["puerta_abierta"]
    if col == n["puerta_azul"]["col"] and fila == n["puerta_azul"]["fila"]:
        if n["puerta_nivel"] is None and not frutas_completas():
            return True
        return not estado["tiene_llave_azul"] and not estado["puerta_azul_abierta"]
    if n["puerta_nivel"] and col == n["puerta_nivel"]["col"] and fila == n["puerta_nivel"]["fila"]:
        return not estado["puerta_azul_abierta"]
    return mapa_actual()[fila][col] in (2, 3, 4, 5, 6)

fuente     = pygame.font.SysFont("monospace", 16)
fuente_hud = pygame.font.SysFont("monospace", 18, bold=True)
fuente_go  = pygame.font.SysFont("monospace", 60, bold=True)
fuente_sub = pygame.font.SysFont("monospace", 24)
fuente_niv = pygame.font.SysFont("monospace", 48, bold=True)

FTILE = 30
FHUD  = 28

img_colum        = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgcolumna.png").convert(),           (TILE, TILE))
img_pasto        = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgPasto.png").convert(),             (TILE, TILE))
img_arbol        = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgarbol.png").convert_alpha(),       (TILE, TILE))
img_roca         = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgroca.png").convert_alpha(),        (TILE, TILE))
img_pino         = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgpino.png").convert_alpha(),        (TILE, TILE))
img_loto         = pygame.transform.scale(pygame.image.load("Assets/Bloques/imglotoPiso.png").convert_alpha(),    (TILE, TILE))
img_arbusto      = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgarbusto.png").convert_alpha(),     (TILE, TILE))
img_pesa         = pygame.transform.scale(pygame.image.load("Assets/Elementos/IMGpesa.png").convert_alpha(),        (FTILE, FTILE))
img_pesa_hud     = pygame.transform.scale(pygame.image.load("Assets/Elementos/IMGpesa.png").convert_alpha(),        (FHUD, FHUD))
img_llave        = pygame.transform.scale(pygame.image.load("Assets/Elementos/IMGllaveamarilla.png").convert_alpha(),(FTILE, FTILE))
img_llave_hud    = pygame.transform.scale(pygame.image.load("Assets/Elementos/IMGllaveamarilla.png").convert_alpha(),(FHUD, FHUD))
img_puerta       = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgpuertamarilla.png").convert_alpha(),(TILE, TILE))
img_llave_azul   = pygame.transform.scale(pygame.image.load("Assets/Elementos/IMGllaveazul.png").convert_alpha(),   (FTILE, FTILE))
img_llave_azul_hud = pygame.transform.scale(pygame.image.load("Assets/Elementos/IMGllaveazul.png").convert_alpha(), (FHUD, FHUD))
img_puerta_azul  = pygame.transform.scale(pygame.image.load("Assets/Bloques/imgpuertaazul.png").convert_alpha(),  (TILE, TILE))
img_capi         = pygame.transform.scale(pygame.image.load("Assets/Entidades/capi.png").convert_alpha(),           (TILE, TILE))

imgs_fruta = {
    t: pygame.transform.scale(pygame.image.load(f"Assets/Elementos/IMG{t}.png").convert_alpha(), (FTILE, FTILE))
    for t in ["sandia", "manzana", "naranja", "platano"]
}
imgs_hud = {
    t: pygame.transform.scale(pygame.image.load(f"Assets/Elementos/IMG{t}.png").convert_alpha(), (FHUD, FHUD))
    for t in ["sandia", "manzana", "naranja", "platano"]
}

transicion_timer = 0  # frames mostrando "NIVEL 2"

def dibujar_game_over():
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    pantalla.blit(overlay, (0, 0))
    pantalla.blit(fuente_go.render("GAME OVER", True, ROJO),
                  fuente_go.render("GAME OVER", True, ROJO).get_rect(center=(ANCHO//2, ALTO//2 - 60)))
    msg = "El enemigo te atrapó" if estado["causa_go"] == "enemigo" else "Pisaste el loto sin la pesa"
    pantalla.blit(fuente_sub.render(msg, True, BLANCO),
                  fuente_sub.render(msg, True, BLANCO).get_rect(center=(ANCHO//2, ALTO//2 + 10)))
    pantalla.blit(fuente_sub.render("Presiona R para reiniciar", True, AMARILLO),
                  fuente_sub.render("Presiona R para reiniciar", True, AMARILLO).get_rect(center=(ANCHO//2, ALTO//2 + 50)))

def dibujar_ganaste():
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    pantalla.blit(overlay, (0, 0))
    seg  = estado["tiempo"] // 60
    mins = seg // 60
    segs = seg % 60
    pantalla.blit(fuente_go.render("GANASTE!", True, AMARILLO),
                  fuente_go.render("GANASTE!", True, AMARILLO).get_rect(center=(ANCHO//2, ALTO//2 - 60)))
    pantalla.blit(fuente_sub.render(f"Tiempo: {mins:02d}:{segs:02d}", True, BLANCO),
                  fuente_sub.render(f"Tiempo: {mins:02d}:{segs:02d}", True, BLANCO).get_rect(center=(ANCHO//2, ALTO//2)))
    pantalla.blit(fuente_sub.render("Presiona R para reiniciar", True, AMARILLO),
                  fuente_sub.render("Presiona R para reiniciar", True, AMARILLO).get_rect(center=(ANCHO//2, ALTO//2 + 50)))

def dibujar_transicion():
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    pantalla.blit(overlay, (0, 0))
    pantalla.blit(fuente_go.render("NIVEL 2", True, AMARILLO),
                  fuente_go.render("NIVEL 2", True, AMARILLO).get_rect(center=(ANCHO//2, ALTO//2)))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if estado["game_over"] or estado["ganaste"]:
                if evento.key == pygame.K_r:
                    estado  = estado_inicial(0)
                    enemigos = nuevos_enemigos(0)
                continue

            if transicion_timer > 0:
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
                n = nivel_actual()

                # Recoger fruta
                for f in estado["frutas"][:]:
                    if f["col"] == nueva_col and f["fila"] == nueva_fila:
                        estado["conteo"][f["tipo"]] += 1
                        estado["frutas"].remove(f)

                # Recoger pesa
                if estado["pesa_activa"] and nueva_col == n["pesa"]["col"] and nueva_fila == n["pesa"]["fila"]:
                    estado["tiene_pesa"] = True
                    estado["pesa_activa"] = False

                # Recoger llave amarilla
                if estado["llave_activa"] and nueva_col == n["llave"]["col"] and nueva_fila == n["llave"]["fila"]:
                    estado["tiene_llave"] = True
                    estado["llave_activa"] = False

                # Recoger llave azul
                if estado["llave_azul_activa"] and nueva_col == n["llave_azul"]["col"] and nueva_fila == n["llave_azul"]["fila"]:
                    estado["tiene_llave_azul"] = True
                    estado["llave_azul_activa"] = False

                # Puerta amarilla
                if nueva_col == n["puerta"]["col"] and nueva_fila == n["puerta"]["fila"]:
                    if estado["tiene_llave"]:
                        estado["puerta_abierta"] = True

                # Puerta azul
                if nueva_col == n["puerta_azul"]["col"] and nueva_fila == n["puerta_azul"]["fila"]:
                    # En el último nivel (sin puerta_nivel) hace falta comerse todas las frutas
                    puede_abrir = estado["tiene_llave_azul"] and (n["puerta_nivel"] is not None or frutas_completas())
                    if puede_abrir:
                        estado["puerta_azul_abierta"] = True
                        # Si es el último nivel, ganar al abrir la puerta azul
                        if not n["puerta_nivel"]:
                            estado["ganaste"] = True
                            estado["contando"] = False

                # Puerta al siguiente nivel
                if n["puerta_nivel"]:
                    if nueva_col == n["puerta_nivel"]["col"] and nueva_fila == n["puerta_nivel"]["fila"]:
                        if estado["puerta_azul_abierta"]:
                            tiempo_guardado = estado["tiempo"]
                            estado = estado_inicial(estado["nivel"] + 1)
                            estado["tiempo"] = tiempo_guardado
                            enemigos = nuevos_enemigos(estado["nivel"])
                            transicion_timer = 120
                for loto in n["lotos"]:
                    if loto["col"] == nueva_col and loto["fila"] == nueva_fila:
                        if not estado["tiene_pesa"]:
                            estado["game_over"] = True
                            estado["causa_go"] = "loto"

    # Actualizar enemigo
    if not estado["game_over"] and not estado["ganaste"] and transicion_timer == 0:
        for enemigo in enemigos:
            enemigo.update()
            if enemigo.toca_jugador(estado["jugador_col"], estado["jugador_fila"]):
                estado["game_over"] = True
                estado["causa_go"] = "enemigo"
                break

    # Contador de transición
    if transicion_timer > 0:
        transicion_timer -= 1

    # Contador de tiempo
    if estado["contando"] and not estado["game_over"] and not estado["ganaste"] and transicion_timer == 0:
        estado["tiempo"] += 1

    # ---- DIBUJAR ----
    n   = nivel_actual()
    mapa = mapa_actual()

    for fila in range(FILAS):
        for col in range(COLS):
            x = col * TILE
            y = fila * TILE
            pantalla.blit(img_pasto, (x, y))
            if   mapa[fila][col] == 2: pantalla.blit(img_arbol,   (x, y))
            elif mapa[fila][col] == 3: pantalla.blit(img_roca,    (x, y))
            elif mapa[fila][col] == 4: pantalla.blit(img_pino,    (x, y))
            elif mapa[fila][col] == 5: pantalla.blit(img_arbusto, (x, y))
            elif mapa[fila][col] == 6: pantalla.blit(img_colum,   (x, y))

    # Lotos
    for loto in n["lotos"]:
        pantalla.blit(img_loto, (loto["col"] * TILE, loto["fila"] * TILE))

    # Pesa
    if estado["pesa_activa"]:
        pantalla.blit(img_pesa, (n["pesa"]["col"] * TILE + 5, n["pesa"]["fila"] * TILE + 5))

    # Frutas
    for f in estado["frutas"]:
        pantalla.blit(imgs_fruta[f["tipo"]],
                      (f["col"] * TILE + 5, f["fila"] * TILE + 5))

    # Llave amarilla
    if estado["llave_activa"]:
        pantalla.blit(img_llave, (n["llave"]["col"] * TILE + 5, n["llave"]["fila"] * TILE + 5))

    # Puerta amarilla
    if not estado["puerta_abierta"]:
        pantalla.blit(img_puerta, (n["puerta"]["col"] * TILE, n["puerta"]["fila"] * TILE))

    # Llave azul
    if estado["llave_azul_activa"]:
        pantalla.blit(img_llave_azul, (n["llave_azul"]["col"] * TILE + 5, n["llave_azul"]["fila"] * TILE + 5))

    # Puerta azul
    if not estado["puerta_azul_abierta"]:
        pantalla.blit(img_puerta_azul, (n["puerta_azul"]["col"] * TILE, n["puerta_azul"]["fila"] * TILE))

    # Puerta al nivel 2 (solo en nivel 1, bloqueada hasta abrir puerta azul)
    if n["puerta_nivel"]:
        if not estado["puerta_azul_abierta"]:
            pantalla.blit(img_puerta_azul, (n["puerta_nivel"]["col"] * TILE, n["puerta_nivel"]["fila"] * TILE))

    # Enemigos — cubos rojos con borde naranja
    for enemigo in enemigos:
        ex = enemigo.col * TILE
        ey = enemigo.fila * TILE
        pygame.draw.rect(pantalla, NARANJA, (ex,     ey,     TILE,   TILE))
        pygame.draw.rect(pantalla, ROJO,    (ex + 4, ey + 4, TILE-8, TILE-8))
        pygame.draw.rect(pantalla, NEGRO,   (ex,     ey,     TILE,   TILE), 2)

    # Capibara
    pantalla.blit(img_capi, (estado["jugador_col"] * TILE, estado["jugador_fila"] * TILE))

    # Barra inferior
    barra_y = FILAS * TILE
    pygame.draw.rect(pantalla, VERDE, (0, barra_y, ANCHO, 70))

    # Nivel actual y tiempo
    txt_niv = fuente_hud.render(f"NIVEL {estado['nivel']+1}", True, AMARILLO)
    pantalla.blit(txt_niv, (ANCHO - txt_niv.get_width() - 8, barra_y + 8))
    seg = estado["tiempo"] // 60
    mins = seg // 60
    segs = seg % 60
    txt_tiempo = fuente_hud.render(f"{mins:02d}:{segs:02d}", True, BLANCO)
    pantalla.blit(txt_tiempo, (ANCHO - txt_tiempo.get_width() - 8, barra_y + 44))

    # Fila 1: pesa y llaves
    x_items = 8
    if estado["tiene_pesa"]:
        pantalla.blit(img_pesa_hud, (x_items, barra_y + 4))
        x_items += FHUD + 6
    if estado["tiene_llave"]:
        pantalla.blit(img_llave_hud, (x_items, barra_y + 4))
        x_items += FHUD + 6
    if estado["tiene_llave_azul"]:
        pantalla.blit(img_llave_azul_hud, (x_items, barra_y + 4))

    # Fila 2: frutas
    x_offset = 8
    for tipo in ["sandia", "manzana", "naranja", "platano"]:
        pantalla.blit(imgs_hud[tipo], (x_offset, barra_y + 38))
        num = fuente_hud.render(f"x{estado['conteo'][tipo]}", True, BLANCO)
        pantalla.blit(num, (x_offset + FHUD + 2, barra_y + 42))
        x_offset += FHUD + 45

    if transicion_timer > 0:
        dibujar_transicion()
    if estado["game_over"]:
        dibujar_game_over()
    if estado["ganaste"]:
        dibujar_ganaste()

    pygame.display.update()
    reloj.tick(60)
