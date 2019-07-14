# 飞船类
import pygame


class Ship():
    """初始化飞船并设置其初始位置"""
    def __init__(self,screen):
        # 定义surface参数
        self.screen = screen
        # 获取飞船的图片
        self.image = pygame.image.load('images/ship.bmp')
        # 获取图片的矩形
        self.rect = self.image.get_rect()
        # 获取屏幕的矩形
        self.sereen_rect = self.screen.get_rect()
        # 设置飞船和屏幕的相对位置
        self.rect.centerx = self.sereen_rect.centerx
        self.rect.bottom = self.sereen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)

