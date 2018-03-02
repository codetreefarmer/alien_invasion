# _*_coding:UTF-8_*_
# @Time: 2018/3/1 20:39
# @Author: yw s
# @File: alien.py
# @Software: PyCharm

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置开始的位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 转化成图片
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 开始每个外星人放在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人详细位置
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """如果外星人到达边缘返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """左右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """在当前位置显示外星人"""
        self.screen.blit(self.image, self.rect)
