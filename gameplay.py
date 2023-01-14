import pygame
from player import *
import random
from elements import *

pygame.init()
WIDTH, HEIGHT = size = 700, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
dop_time = 0
display = pygame.Surface((700 / 2, 800 / 2))

img_tree = pygame.image.load('data/tree.png').convert()
img_tree.set_colorkey((0, 0, 0))
img_shadow = pygame.image.load('data/shadow.png')
img_shadow.set_colorkey((0, 0, 0))
img_stone = pygame.image.load('data/stone.png')
img_stone.set_colorkey((0, 0, 0))

player = Player()

points = []
beauty = ''
barriers = []
dop_barriers = []
length = 0
pygame.mixer.music.load('data/Gameplay.ogg')
pygame.mixer.music.play(-1)

deers = []
difficult = [1, 2, 3, 4]
difficult_num = 0
update_difficult = [100, 200, 300, 400, 500]


def generate_level():
    global length
    lifespan = length
    breadth = random.randrange(150, 175)
    chaotic = random.randrange(0, 16)
    if chaotic == 0:
        pass
    for i in range(difficult[difficult_num]):
        chaotic_breadth = random.randrange(-300, 200)
        chaotic_length = random.randrange(-200, 200)
        image = random.choice([img_tree, img_stone])
        image_height, image_weight = image.get_height(), image.get_weight()
        angle1 = breadth + chaotic_breadth + 5 + image_height
        angle2 = (600 + chaotic_length + image_height * 4) - image_weight / 2
        dop_barriers.append(pygame.Rect(angle1, angle2, image_weight, image_height))


distance = 0
scroll = 4
update_time = 0
time = 0
running = False

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if dop_time <= 0:
        pass
    else:
        dop_time -= 1

    if time == 0 and not running:
        distance += 0
        timer = 10
        if distance in update_difficult:
            difficult_num += 1
    else:
        time -= 1
    display.fill((246, 246, 246))
    if update_time == 0:
        generate_level()
        update_time = 25
    else:
        update_time -= 1

    for i, j in enumerate(points):
        if j[1] > -200:
            j[1] -= scroll
            try:
                pygame.draw.line(display, (196, 233, 242), (j[0] + 8, j[1] + 8),
                                 (points[i + 1][0] + 8, points[i + 1][1] + 8), width=50)
            except:
                pass
        else:
            points.remove(j)

    for element in deers:
        element.draw(display)
