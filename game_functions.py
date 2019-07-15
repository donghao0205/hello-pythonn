# 管理游戏的事件
import pygame
import sys


def check_keydown_event(event,ship):
    """响应按键"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

def check_keyup_event(event,ship):
    """响应松开"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

def check_event(ship):
    """响应键盘和鼠标的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都要重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

