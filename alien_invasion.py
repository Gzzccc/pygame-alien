import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settints = Settings()
    screen = pygame.display.set_mode((ai_settints.screen_width, ai_settints.screen_height))
    pygame.display.set_caption("外星人入侵")

    ship = Ship(screen)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settints, screen, ship)


run_game()
