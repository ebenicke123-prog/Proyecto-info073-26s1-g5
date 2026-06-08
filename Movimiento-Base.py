#Ideas Para el Movimiento

import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

x = 0
y = 0

while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_w:
                y = y - 40

            if evento.key == pygame.K_s:
                y = y + 40

            if evento.key == pygame.K_a:
                x = x - 40

            if evento.key == pygame.K_d:
                x = x + 40

            if x < 0:
                x = 0

            if x > 760:
                x = 760

            if y < 0:
                y = 0

            if y > 560:
                y = 560

    pantalla.fill((255, 255, 255))

    pygame.draw.rect(pantalla, (0, 0, 0), (0, 0, 800, 600), 3)

    pygame.draw.rect(pantalla, (0, 0, 255), (x, y, 40, 40))

    pygame.display.update()