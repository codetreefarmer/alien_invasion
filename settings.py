# _*_coding:UTF-8_*_
# @Time: 2018/3/1 20:39
# @Author: yw s
# @File: settings.py
# @Software: PyCharm

class Settings():
    """初始化<Alien Invasion>所有的类"""

    def __init__(self):
        """初始化游戏的标准设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        
        # 飞船设置
        self.ship_limit = 3
            
        # 子弹设置
        self.bullet_width = 6
        self.bullet_height = 10
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5
        
        # 外星人设置
        self.fleet_drop_speed = 20
            
        # 游戏整体速度提高比列，并外星人点数提高比例
        self.speedup_scale = 1.1
        self.score_scale = 1.2
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """重新开始游戏的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        
        # 外星人点数
        self.alien_points = 50
    
        # 外星人移动方向，1是向右.-1是向左
        self.fleet_direction = 1
        
    def increase_speed(self):
        """加速设置和增加外星人的点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
