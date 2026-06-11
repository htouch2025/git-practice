import pygame

class MyBullet(pygame.sprite.Sprite):
    def __init__(self, mai):
        super().__init__()

        self.screen = mai.screen
        self.settings = mai.settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = mai.myship.rect.midright

    def update(self):
        self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
