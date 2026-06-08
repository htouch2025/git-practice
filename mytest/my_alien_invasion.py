"""主程序"""

import sys
import pygame

from my_settings import Settings
from my_ship import Ship

class MyAlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.myship = Ship(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.myship.update()
            self.screen.fill(self.settings.bg_color)
            self.myship.blitme()
            pygame.display.flip()
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

    def _check_keyup_event(self,event):
        if event.key == pygame.K_UP:
            self.myship.up_flag = False
        elif event.key == pygame.K_DOWN:
            self.myship.down_flag = False



if __name__ == '__main__':
    mai = MyAlienInvasion()
    mai.run_game()