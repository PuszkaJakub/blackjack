import pygame
import sys

from hud import *
from blackjack_game import *

pygame.init()

# load save
gambler_balance = 100


def menu_font(size):
    return pygame.font.SysFont('consolas', size)


# display window settings
screen_resolution = (1280, 720)

SCREEN = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("Blackjack")


def main_menu():
    while True:
        SCREEN.fill("Black")
        MOUSE_POSITION = pygame.mouse.get_pos()

        BUTTON_BJ_GAME = Button(image=None, position=(640, 360),
                             text="BLACKJACK", font=menu_font(48), color_normal="#d7fcd4", color_onclick="Gray")
        BUTTON_QUIT = Button(image=None, position=(640, 460),
                             text="QUIT", font=menu_font(48), color_normal="#d7fcd4", color_onclick="Gray")

        for button in [BUTTON_BJ_GAME, BUTTON_QUIT]:
            button.change_color(MOUSE_POSITION)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_BJ_GAME.check_input(MOUSE_POSITION):
                    blackjack_game(SCREEN)
                if BUTTON_QUIT.check_input(MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
