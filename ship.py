# 飞船类
import pygame


class Ship():
    """初始化飞船并设置其初始位置"""
    def __init__(self,ai_settings,screen):
        # 定义surface参数
        self.screen = screen
        # 获取飞船的图片
        self.image = pygame.image.load('images/ship.bmp')
        # 获取图片的矩形
        self.rect = self.image.get_rect()
        # 获取屏幕的矩形
        self.screen_rect = self.screen.get_rect()
        # 设置飞船和屏幕的相对位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 移动速度
        self.ai_settings = ai_settings
        # 在飞船的center中存储小数值
        self.center = float(self.rect.centerx)


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.centerx 更新rect对象
        self.rect.centerx = self.center
