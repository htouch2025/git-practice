"""主程序"""

import sys
import pygame

class MyAlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (80, 80, 80)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()
        
if __name__ == '__main__':
    mai = MyAlienInvasion()
    mai.run_game()