import sys

import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 5


def update_screen(ai_settints,screen,ship):
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settints.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()



