# 游戏初始化设置

import pygame

class Setting():
    def __init__(self):
        # 设置屏幕宽度
        self.width = 1200
        # 设置屏幕高度
        self.height = 800
        # 设置屏幕背景色
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_speed_factor = 1.5