# _*_coding:UTF-8_*_
# @Time: 2018/3/1 20:39
# @Author: yw s
# @File: game_stats.py
# @Software: PyCharm

class GameStats():
    """<Alien Invasion>的统计信息类"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 让游戏一开始处于非活跃状态
        self.game_active = False
        
        # 最高分不应该被重置
        self.high_score = 0
        
    def reset_stats(self):
        """初始化游戏期间的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
