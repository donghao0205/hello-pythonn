import sys
import pygame
from settings import Setting

def run_game():

    # 初始化屏幕对象
    pygame.init()
    # 创建一个设置类实例
    settings = Setting()
    # 设置屏幕
    screen = pygame.display.set_mode((settings.width,settings.height))
    pygame.display.set_caption("demo")
    while True:
        """监视鼠标和键盘"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(settings.bg_color)
        pygame.display.flip()


run_game()