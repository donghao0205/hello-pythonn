import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():

    # 初始化屏幕对象
    pygame.init()
    # 创建一个设置类实例
    ai_settings = Setting()
    # 设置屏幕
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    ship = Ship(ai_settings,screen)
    pygame.display.set_caption("demo")
    # 创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        gf.check_event(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

# 启动游戏
run_game()