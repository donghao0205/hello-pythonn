import pygame
from settings import Setting
from ship import Ship
import game_functions as gf


def run_game():

    # 初始化屏幕对象
    pygame.init()
    # 创建一个设置类实例
    settings = Setting()
    # 设置屏幕
    screen = pygame.display.set_mode((settings.width,settings.height))
    ship = Ship(screen)
    pygame.display.set_caption("demo")
    while True:
        gf.check_event()
        screen.fill(settings.bg_color)
        ship.blitme()

        # 让最近绘制屏幕可见
        pygame.display.flip()


run_game()