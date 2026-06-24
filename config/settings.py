import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
GRAY = (80, 80, 80)

FONT_NAME = "arial"


def load_font(size: int) -> pygame.font.Font:
    return pygame.font.SysFont(FONT_NAME, size)
