import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #.Rect 之所以大写，表示这里是类的实例化操作，而非方法调用。
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

    def update(self):
        self.rect.y -= self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
