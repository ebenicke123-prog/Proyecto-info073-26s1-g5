import pygame
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

fuente     = pygame.font.SysFont("monospace", 16)
fuente_hud = pygame.font.SysFont("monospace", 18, bold=True)
fuente_go  = pygame.font.SysFont("monospace", 60, bold=True)
fuente_sub = pygame.font.SysFont("monospace", 24)

TILE  = 40
COLS  = 15
FILAS = 15
ANCHO = TILE * COLS
ALTO  = TILE * FILAS + 70

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Las Aventuras con Capi")
reloj = pygame.time.Clock()


def cargar_imagen(ruta, tamano=None):
    imagen = pygame.image.load(ruta).convert_alpha()
    if tamano is not None:
        imagen = pygame.transform.scale(imagen, tamano)
    return imagen


BLANCO   = (255, 255, 255)
NEGRO    = (0,   0,   0)
VERDE    = (34,  139,  34)
ROJO     = (200,  30,  30)
AMARILLO = (255, 220,   0)

MAPA1 = [
    [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,2,0,0,2,0,0,0,0,0],
    [2,2,3,0,0,0,0,0,0,0,0,0,0,2,2],
    [5,5,0,2,0,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,2,0,0,2,0,0,0,2,3,3],
    [0,0,0,2,0,0,0,0,0,2,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,0,0,0,0,2,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
    [4,4,4,0,0,0,0,0,5,0,0,0,0,0,5],
    [3,3,3,4,0,0,0,0,5,5,5,0,3,0,5],
    [0,0,0,3,4,0,0,0,0,0,5,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5],
]

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
    (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(11,6),(11,7),(11,8),(11,9),(10,9),(9,9),(8,9),(7,9),(6,9),(5,9),(4,9),(3,9),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),
]

ENEMIGO3_RUTA = [
    (7,7),(6,7),(5,7),(5,6),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(6,11),(7,11),(8,11),(9,11),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,6),(9,7),(8,7),(7,7),
]

ENEMIGO4_RUTA = [
    (1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(2,1),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
]
ENEMIGO5_RUTA = [
    (13,6),(13,5),(13,4),(13,3),(13,2),(13,1),(12,1),(11,1),(12,1),(13,1),(13,2),(13,3),(13,4),(13,5),(13,6),
]
ENEMIGO6_RUTA = [
    (1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(2,13),(3,13),(2,13),(1,13),(1,12),(1,11),(1,10),(1,9),(1,8),
]
ENEMIGO7_RUTA = [
    (13,8),(13,9),(13,10),(13,11),(13,12),(13,13),(12,13),(11,13),(12,13),(13,13),(13,12),(13,11),(13,10),(13,9),(13,8),
]

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
        "puerta_nivel":{"col": 14, "fila": 7},
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

class Enemigo:
    def __init__(self, ruta):
        self.ruta   = ruta
        self.idx    = 0
        self.col    = ruta[0][0]
        self.fila   = ruta[0][1]
        self.timer  = 0
        self.speed  = 30  

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
        "causa_go": None,  
        "tiempo": 0,       
        "contando": True,  
    }

estado  = estado_inicial(0)
enemigos = nuevos_enemigos(0)

def reiniciar_juego():
    global estado, enemigos, transicion_timer
    estado = estado_inicial(0)
    enemigos = nuevos_enemigos(0)
    transicion_timer = 0


def nivel_actual():
    return niveles[estado["nivel"]]

def mapa_actual():
    return nivel_actual()["mapa"]

def puede_avanzar_nivel():
    n = nivel_actual()
    if n["puerta_nivel"] is None:
        return False
    if estado["nivel"] == 0:
        return frutas_completas()
    return estado["puerta_azul_abierta"]


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
        return not puede_avanzar_nivel()
    return mapa_actual()[fila][col] in (2, 3, 4, 5, 6)

fuente     = pygame.font.SysFont("monospace", 16)
fuente_hud = pygame.font.SysFont("monospace", 18, bold=True)
fuente_go  = pygame.font.SysFont("monospace", 60, bold=True)
fuente_sub = pygame.font.SysFont("monospace", 24)
fuente_niv = pygame.font.SysFont("monospace", 48, bold=True)

FTILE = 30
FHUD  = 28

img_pasto        = cargar_imagen("Assets/Bloques/imgPasto.png", (TILE, TILE))
img_arbol        = cargar_imagen("Assets/Bloques/imgarbol.png", (TILE, TILE))
img_roca         = cargar_imagen("Assets/Bloques/imgroca.png", (TILE, TILE))
img_pino         = cargar_imagen("Assets/Bloques/imgpino.png", (TILE, TILE))
img_loto         = cargar_imagen("Assets/Bloques/imglotoPiso.png", (TILE, TILE))
img_arbusto      = cargar_imagen("Assets/Bloques/imgarbusto.png", (TILE, TILE))
img_pesa         = cargar_imagen("Assets/Elementos/IMGpesa.png", (FTILE, FTILE))
img_pesa_hud     = cargar_imagen("Assets/Elementos/IMGpesa.png", (FHUD, FHUD))
img_llave        = cargar_imagen("Assets/Elementos/IMGllaveamarilla.png", (FTILE, FTILE))
img_llave_hud    = cargar_imagen("Assets/Elementos/IMGllaveamarilla.png", (FHUD, FHUD))
img_puerta       = cargar_imagen("Assets/Bloques/imgpuertamarilla.png", (TILE, TILE))
img_llave_azul   = cargar_imagen("Assets/Elementos/IMGllaveazul.png", (FTILE, FTILE))
img_llave_azul_hud = cargar_imagen("Assets/Elementos/IMGllaveazul.png", (FHUD, FHUD))
img_puerta_azul  = cargar_imagen("Assets/Bloques/imgpuertaazul.png", (TILE, TILE))
img_levelup      = cargar_imagen("Assets/Bloques/levelup.png", (TILE, TILE))
img_capi         = cargar_imagen("Assets/Entidades/capi.png", (TILE, TILE))
img_enemigo      = cargar_imagen("Assets/Entidades/enemigo.png", (TILE, TILE))
imgs_fruta = {
    tipo: cargar_imagen(f"Assets/Elementos/IMG{tipo}.png", (FTILE, FTILE))
    for tipo in ["sandia", "manzana", "naranja", "platano"]
}
imgs_hud = {
    tipo: cargar_imagen(f"Assets/Elementos/IMG{tipo}.png", (FHUD, FHUD))
    for tipo in ["sandia", "manzana", "naranja", "platano"]
}

transicion_timer = 0
transicion_mensaje = "NIVEL 2"
escena_actual = "principal"

img_pantalla_principal = pygame.transform.scale(pygame.image.load("Assets\pantallas\principal.png").convert_alpha(),(ANCHO, ALTO))
img_pantalla_instrucciones = pygame.transform.scale(pygame.image.load("Assets\pantallas\Intrucciones_de_capi.png").convert_alpha(),(ANCHO, ALTO))
img_pantalla_victoria = pygame.transform.scale(pygame.image.load("Assets\pantallas\Victoria.png").convert_alpha(),(ANCHO, ALTO))


def dibujar_pantalla_principal():
    pantalla.blit(img_pantalla_principal, (0, 0))


def dibujar_instrucciones():
    pantalla.blit(img_pantalla_instrucciones, (0, 0))


def dibujar_game_over():
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    pantalla.blit(overlay, (0, 0))

    texto_game_over = fuente_go.render("GAME OVER", True, ROJO)
    pantalla.blit(texto_game_over, texto_game_over.get_rect(center=(ANCHO // 2, ALTO // 2 - 60)))

    mensaje = "El enemigo te atrapó" if estado["causa_go"] == "enemigo" else "Pisaste el loto sin la pesa"
    texto_mensaje = fuente_sub.render(mensaje, True, BLANCO)
    pantalla.blit(texto_mensaje, texto_mensaje.get_rect(center=(ANCHO // 2, ALTO // 2 + 10)))

    texto_reiniciar = fuente_sub.render("Presiona R para reiniciar", True, AMARILLO)
    pantalla.blit(texto_reiniciar, texto_reiniciar.get_rect(center=(ANCHO // 2, ALTO // 2 + 50)))

def dibujar_ganaste():
    pantalla.blit(img_pantalla_victoria, (0, 0))

def dibujar_transicion():
    overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 220))
    pantalla.blit(overlay, (0, 0))

    txt_nivel = fuente_go.render(transicion_mensaje, True, AMARILLO)
    pantalla.blit(txt_nivel, txt_nivel.get_rect(center=(ANCHO // 2, ALTO // 2 - 20)))

    txt_prep = fuente_sub.render("Prepárate", True, BLANCO)
    pantalla.blit(txt_prep, txt_prep.get_rect(center=(ANCHO // 2, ALTO // 2 + 40)))


def dibujar_mapa():
    n = nivel_actual()
    mapa = mapa_actual()

    for fila in range(FILAS):
        for col in range(COLS):
            x = col * TILE
            y = fila * TILE
            pantalla.blit(img_pasto, (x, y))

            if mapa[fila][col] == 2:
                pantalla.blit(img_arbol, (x, y))
            elif mapa[fila][col] == 3:
                pantalla.blit(img_roca, (x, y))
            elif mapa[fila][col] == 4:
                pantalla.blit(img_pino, (x, y))
            elif mapa[fila][col] == 5:
                pantalla.blit(img_arbusto, (x, y))

    for loto in n["lotos"]:
        pantalla.blit(img_loto, (loto["col"] * TILE, loto["fila"] * TILE))

    if estado["pesa_activa"]:
        pantalla.blit(img_pesa, (n["pesa"]["col"] * TILE + 5, n["pesa"]["fila"] * TILE + 5))

    for fruta in estado["frutas"]:
        pantalla.blit(imgs_fruta[fruta["tipo"]], (fruta["col"] * TILE + 5, fruta["fila"] * TILE + 5))

    if estado["llave_activa"]:
        pantalla.blit(img_llave, (n["llave"]["col"] * TILE + 5, n["llave"]["fila"] * TILE + 5))

    if not estado["puerta_abierta"]:
        pantalla.blit(img_puerta, (n["puerta"]["col"] * TILE, n["puerta"]["fila"] * TILE))

    if estado["llave_azul_activa"]:
        pantalla.blit(img_llave_azul, (n["llave_azul"]["col"] * TILE + 5, n["llave_azul"]["fila"] * TILE + 5))

    pantalla.blit(img_puerta_azul, (n["puerta_azul"]["col"] * TILE, n["puerta_azul"]["fila"] * TILE))

    if n["puerta_nivel"] and not estado["puerta_azul_abierta"]:
        pantalla.blit(img_levelup, (n["puerta_nivel"]["col"] * TILE, n["puerta_nivel"]["fila"] * TILE))

    for enemigo in enemigos:
        pantalla.blit(img_enemigo, (enemigo.col * TILE, enemigo.fila * TILE))

    pantalla.blit(img_capi, (estado["jugador_col"] * TILE, estado["jugador_fila"] * TILE))


def dibujar_hud():
    barra_y = FILAS * TILE
    pygame.draw.rect(pantalla, VERDE, (0, barra_y, ANCHO, 70))

    txt_niv = fuente_hud.render(f"NIVEL {estado['nivel'] + 1}", True, AMARILLO)
    pantalla.blit(txt_niv, (ANCHO - txt_niv.get_width() - 8, barra_y + 8))

    seg = estado["tiempo"] // 60
    mins = seg // 60
    segs = seg % 60
    txt_tiempo = fuente_hud.render(f"{mins:02d}:{segs:02d}", True, BLANCO)
    pantalla.blit(txt_tiempo, (ANCHO - txt_tiempo.get_width() - 8, barra_y + 44))

    x_items = 8
    if estado["tiene_pesa"]:
        pantalla.blit(img_pesa_hud, (x_items, barra_y + 4))
        x_items += FHUD + 6
    if estado["tiene_llave"]:
        pantalla.blit(img_llave_hud, (x_items, barra_y + 4))
        x_items += FHUD + 6
    if estado["tiene_llave_azul"]:
        pantalla.blit(img_llave_azul_hud, (x_items, barra_y + 4))

    x_offset = 8
    for tipo in ["sandia", "manzana", "naranja", "platano"]:
        pantalla.blit(imgs_hud[tipo], (x_offset, barra_y + 38))
        num = fuente_hud.render(f"x{estado['conteo'][tipo]}", True, BLANCO)
        pantalla.blit(num, (x_offset + FHUD + 2, barra_y + 42))
        x_offset += FHUD + 45


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                escena_actual = "principal"
                reiniciar_juego()
                continue

            if escena_actual == "principal":
                if evento.key == pygame.K_SPACE:
                    escena_actual = "juego"
                    reiniciar_juego()
                elif evento.key == pygame.K_i:
                    escena_actual = "instrucciones"
                continue

            if escena_actual == "instrucciones":
                if evento.key == pygame.K_i:
                    escena_actual = "principal"
                continue

            if escena_actual == "transicion":
                continue

            if estado["game_over"] or estado["ganaste"]:
                if evento.key == pygame.K_r:
                    reiniciar_juego()
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

                for f in estado["frutas"][:]:
                    if f["col"] == nueva_col and f["fila"] == nueva_fila:
                        estado["conteo"][f["tipo"]] += 1
                        estado["frutas"].remove(f)

                if estado["pesa_activa"] and nueva_col == n["pesa"]["col"] and nueva_fila == n["pesa"]["fila"]:
                    estado["tiene_pesa"] = True
                    estado["pesa_activa"] = False

                if estado["llave_activa"] and nueva_col == n["llave"]["col"] and nueva_fila == n["llave"]["fila"]:
                    estado["tiene_llave"] = True
                    estado["llave_activa"] = False

                if estado["llave_azul_activa"] and nueva_col == n["llave_azul"]["col"] and nueva_fila == n["llave_azul"]["fila"]:
                    estado["tiene_llave_azul"] = True
                    estado["llave_azul_activa"] = False

                if nueva_col == n["puerta"]["col"] and nueva_fila == n["puerta"]["fila"]:
                    if estado["tiene_llave"]:
                        estado["puerta_abierta"] = True

                if nueva_col == n["puerta_azul"]["col"] and nueva_fila == n["puerta_azul"]["fila"]:
                    
                    puede_abrir = estado["tiene_llave_azul"] and (n["puerta_nivel"] is not None or frutas_completas())
                    if puede_abrir:
                        estado["puerta_azul_abierta"] = True
                        if not n["puerta_nivel"]:
                            estado["ganaste"] = True
                            estado["contando"] = False

                if n["puerta_nivel"]:
                    if nueva_col == n["puerta_nivel"]["col"] and nueva_fila == n["puerta_nivel"]["fila"]:
                        if puede_avanzar_nivel():
                            tiempo_guardado = estado["tiempo"]
                            siguiente_nivel = estado["nivel"] + 1
                            estado = estado_inicial(siguiente_nivel)
                            estado["tiempo"] = tiempo_guardado
                            enemigos = nuevos_enemigos(estado["nivel"])
                            transicion_timer = 90
                            transicion_mensaje = f"NIVEL {estado['nivel'] + 1}"
                            escena_actual = "transicion"
                for loto in n["lotos"]:
                    if loto["col"] == nueva_col and loto["fila"] == nueva_fila:
                        if not estado["tiene_pesa"]:
                            estado["game_over"] = True
                            estado["causa_go"] = "loto"

    if escena_actual == "principal":
        pantalla.fill(NEGRO)
        dibujar_pantalla_principal()
        pygame.display.update()
        reloj.tick(60)
        continue

    if escena_actual == "instrucciones":
        pantalla.fill(NEGRO)
        dibujar_instrucciones()
        pygame.display.update()
        reloj.tick(60)
        continue

    if escena_actual == "transicion":
        pantalla.fill(NEGRO)
        dibujar_transicion()
        pygame.display.update()
        reloj.tick(60)
        if transicion_timer > 0:
            transicion_timer -= 1
        if transicion_timer <= 0:
            escena_actual = "juego"
        continue

    if not estado["game_over"] and not estado["ganaste"] and transicion_timer == 0:
        for enemigo in enemigos:
            enemigo.update()
            if enemigo.toca_jugador(estado["jugador_col"], estado["jugador_fila"]):
                estado["game_over"] = True
                estado["causa_go"] = "enemigo"
                break

    if transicion_timer > 0:
        transicion_timer -= 1

    if estado["contando"] and not estado["game_over"] and not estado["ganaste"] and transicion_timer == 0:
        estado["tiempo"] += 1

    dibujar_mapa()
    dibujar_hud()

    if transicion_timer > 0:
        dibujar_transicion()
    if estado["game_over"]:
        dibujar_game_over()
    if estado["ganaste"]:
        dibujar_ganaste()

    pygame.display.update()
    reloj.tick(60)
