import math

FPS = 120
SURFACE_WIDTH = 320*2
SURFACE_HEIGHT = 180*2
WINDOW_CAPTION = "Easter Game"

# Colours
COLOUR_KEY = (255,0,255)

PARTICLE_COLOURS = [(251, 237, 123), (156, 218, 81), (160, 219, 255), (254, 178, 238)]
BLOOD_COLOURS = [(138, 8, 8), (145, 10, 10), (120, 6, 6), (125, 7, 7)]
CHECK_COLOURS = [(60,60,60), (70,70,70)]
SPIDER_COLOURS = [(57, 9, 71), (163, 51, 95)]

#Game prop
MAP_SIZE=(40,40)
TILE_SIZE=40

#Movement
NORMALIZER_CONST = math.sin(math.pi/4)