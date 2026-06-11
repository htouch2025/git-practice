"""主程序"""

import sys
import pygame

from my_settings import Settings
from my_ship import Ship
from my_bullet import MyBullet

class MyAlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.myship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        while True:
            self._check_events()
            self.myship.update()
            self._update_bullets()
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_UP:
            self.myship.up_flag = True
        elif event.key == pygame.K_DOWN:
            self.myship.down_flag = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_event(self,event):
        if event.key == pygame.K_UP:
            self.myship.up_flag = False
        elif event.key == pygame.K_DOWN:
            self.myship.down_flag = False

    def _fire_bullet(self):
        new_bullet = MyBullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.myship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    mai = MyAlienInvasion()
    mai.run_game()