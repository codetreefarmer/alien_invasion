# _*_coding:UTF-8_*_
# @Time: 2018/3/1 20:39
# @Author: yw s
# @File: ship.py
# @Software: PyCharm

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船，设置开始的位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 把飞船转换成矩形图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #飞船开始的位置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 飞船移动设置一个更详尽的值
        self.center = float(self.rect.centerx)
        
        # 移动标志位
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """在屏幕上创造飞船"""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """通过移动标志位更新飞船的位置"""
        # 更新飞船中心位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        #从详细的值返回到实际位置
        self.rect.centerx = self.center

    def blitme(self):
        """在屏幕上显示飞船"""
        self.screen.blit(self.image, self.rect)
