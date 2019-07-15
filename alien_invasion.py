import pygame
from settings import Setting
from ship import Ship
import game_functions as gf


def run_game():

    # 初始化屏幕对象
    pygame.init()
    # 创建一个设置类实例
    ai_settings = Setting()
    # 设置屏幕
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    ship = Ship(ai_settings,screen)
    pygame.display.set_caption("demo")
    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

# 启动游戏
run_game()