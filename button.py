# _*_coding:UTF-8_*_
# @Time: 2018/3/1 20:39
# @Author: yw s
# @File: button.py
# @Software: PyCharm

import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化一个按键"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮的尺寸和属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # 创建一个按钮
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 准备按钮需要的信息msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """在按钮中间显示msg"""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # 把按钮显示到屏幕上
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
