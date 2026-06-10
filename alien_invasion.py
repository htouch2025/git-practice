"""《外星人入侵》游戏主程序"""

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源（窗口/画布）"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('外星人入侵')
        #实例化一个飞船
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._creat_fleet()
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            #控制帧率：如果当前循环时间短于 1/60 秒，则延时至1/60秒
            self.clock.tick(60) 

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)                
    
    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key ==pygame.K_RIGHT or event.key ==pygame.K_d:
            self.ship.moving_right = False
        elif event.key ==pygame.K_LEFT or event.key ==pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:
            #此处 self 为 Bullet 类的第二个形参：ai_game
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
            # 删除已飞出屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _creat_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕（翻前）"""
        self.screen.fill(self.settings.bg_color)

        #.sprites()：形成组员列表。
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #画上飞船
        self.ship.blitme()

        self.aliens.draw(self.screen)

        #后台翻前：将最近绘制的屏幕前置
        pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()