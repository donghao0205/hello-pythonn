# 管理游戏的事件
import pygame
import sys

def check_event():
    """响应键盘和鼠标的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
