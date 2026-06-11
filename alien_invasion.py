"""《外星人入侵》游戏主程序"""

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
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

        #存储游戏统计信息的实例
        self.stats = GameStats(self)

        #实例化一个飞船
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):    
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):

        #飞船数减一
        self.stats.ships_left -= 1

        #清空外星人列表和子弹列表
        self.bullets.empty()
        self.aliens.empty()

        #创建一个新的外星舰队，并将飞船放在屏幕底部中央
        self._create_fleet()
        self.ship.center_ship()

        #暂停
        sleep(1)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """整个舰队下移，并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        alien = Alien(self)
        current_x = alien.rect.width
        current_y = alien.rect.height

        while current_y < (self.settings.screen_height - 5 * alien.rect.height):
            while current_x < (self.settings.screen_width - 2* alien.rect.width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien.rect.width

            current_x = alien.rect.width  
            current_y += 2 * alien.rect.height

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