import pygame
from pygame.locals import *
from src.color import *

PROJECT_NAME = "rocket(IA)"

ON_FULLSCREEN = True

FPS = 60

HEIGHT = 1200
WIDTH  = 600

SIZE_SCREEN = [HEIGHT, WIDTH]

RUN = True
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

if ON_FULLSCREEN:
    SCREEN = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()

FS_HEIGHT, FS_WIDTH = list(SCREEN.get_size())

FULL_SCREEN = [FS_HEIGHT, FS_WIDTH]




