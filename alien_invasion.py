"""《外星人入侵》游戏主程序"""

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源（窗口/画布）"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigh))
        pygame.display.set_caption('外星人入侵')
        #实例化一个飞船
        self.ship = Ship(self)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            #控制帧率：如果当前循环时间短于 1/60 秒，则延时至1/60秒
            self.clock.tick(60) 

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕（翻前）"""

        #self.screen.fill(self.settings.bg_color)
        #画上飞船
        self.ship.blitme()

        #后台翻前：将最近绘制的屏幕前置
        pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()