class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        #飞船设置
        self.ship_speed = 5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 123, 0)
        self.bullets_allowed = 30

        self.alien_speed = 5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1    # 1为向右，-1 为向左移动