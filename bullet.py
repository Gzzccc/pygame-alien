import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settints, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settints.bullet_width, ai_settints.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settints.bullet_color
        self.speed_factor = ai_settints.bullet_speed_factor

    def update(self, *args):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
