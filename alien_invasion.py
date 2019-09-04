import pygame
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        bullets.update()

        # 删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
