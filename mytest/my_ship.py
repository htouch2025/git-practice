import pygame
from my_settings import Settings 

class Ship:
    def __init__(self,mai):
        self.settings = mai.settings
        self.screen = mai.screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('images/ship_r01.png')
        self.rect = self.ship.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.up_flag = False
        self.down_flag = False

    def update(self):
        if self.up_flag and self.rect.top >= self.screen_rect.top:
            self.rect.y -= self.settings.ship_speed
        elif self.down_flag and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

    def blitme(self):
        self.screen.blit(self.ship, self.rect)