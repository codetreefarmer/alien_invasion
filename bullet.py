# _*_coding:UTF-8_*_
# @Time: 2018/3/1 20:39
# @Author: yw s
# @File: bullet.py
# @Software: PyCharm

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船前面创建一个子弹"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 创建一个子弹，并设置在飞船顶部中央
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 存储子弹详细的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """移动子弹到屏幕顶部"""
        # 更新子弹详细的位置
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上显示"""
        pygame.draw.rect(self.screen, self.color, self.rect)
