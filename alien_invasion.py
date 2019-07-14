import sys
import pygame

def run_game():
    pygame.init()
    pygame.display.set_mode((1200,800))
    pygame.display.set_caption("demo")
    while True:
        """监视鼠标和键盘"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()