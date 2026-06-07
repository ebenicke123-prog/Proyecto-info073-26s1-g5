import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

jugador = pygame.Rect(400, 300, 40, 40)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        jugador.y -= 5
    if teclas[pygame.K_s]:
        jugador.y += 5
    if teclas[pygame.K_a]:
        jugador.x -= 5
    if teclas[pygame.K_d]:
        jugador.x += 5

    pantalla.fill((200, 200, 200))
    pygame.draw.rect(pantalla, (0, 0, 255), jugador)

    pygame.display.update()
    reloj.tick(60)