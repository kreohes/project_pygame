import sys

import pygame

import scripts.script
from scripts.player import *
import random
from scripts.elements import *

pygame.font.init()
pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()
WIDTH, HEIGHT = size = (700, 720)
name = ''
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
dop_time = 0
display = pygame.Surface((700 / 2, 800 / 2))

img_tree = pygame.image.load('data/tree.png').convert()
img_tree.set_colorkey((0, 0, 0))
img_shadow = pygame.image.load('data/shadow.png').convert()
img_shadow.set_colorkey((0, 0, 0))
img_stone = pygame.image.load('data/stone.png').convert()
img_stone.set_colorkey((0, 0, 0))

player = Player([size[0] // 4, 50])

points = []
beauty = []
barriers = []
dop_barriers = []
length = 0
pygame.mixer.music.load('data/Gameplay.ogg')
pygame.mixer.music.play(-1)
death = pygame.mixer.Sound('data/death.wav')

deers = []
difficult = [1, 2, 3, 4]
difficult_num = 0
update_difficult = [100, 200, 300, 400, 500]


def generate_level():
    global length
    lifespan = length
    breadth = random.randrange(150, 175)
    points.append([breadth, 600, lifespan])
    chaotic = random.randrange(0, 16)
    if chaotic == 1:
        deers.append(Deer(random.choice([700, -300]), random.choice([700, 600, 500]), 4))
    for i in range(difficult[difficult_num]):
        chaotic_breadth = random.randrange(-300, 200)
        chaotic_length = random.randrange(-200, 200)
        image = random.choice([img_tree, img_stone])
        dop_barriers.append(pygame.Rect(breadth + chaotic_breadth + 5 + image.get_width() / 2,
                                        (600 + chaotic_length + image.get_height() * 4) - image.get_height() / 2,
                                        image.get_width(),
                                        image.get_height()))
        barriers.append(Barrier([breadth - 8 + chaotic_breadth, 600 + chaotic_length], image, 4))


distance = 0
scroll = 4
update_time = 0
time = 0
running = False
font = pygame.font.Font('data/dpcomic.ttf', 32)

while True:
    fps = str(int(clock.get_fps()))
    if time == 0 and not running:
        distance += 0.05
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

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse = (mouse_x / 2, mouse_y / 2)

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

    player.draw(display, mouse, running)

    for element in deers:
        element.draw(display)
        if element.rectangle.colliderect(
                pygame.Rect(player.pramoyg.x + 20, player.pramoyg.y + 32, player.pramoyg.width / 4,
                            player.pramoyg.height / 4)):
            death.play()
            dop_barriers = []
            deers = []
            running = True
    for i, barrier in enumerate(barriers):
        display.blit(img_shadow,
                     (barrier.pos[0] + barrier.picture.get_width(),
                      barrier.pos[1] + barrier.picture.get_height() * 4 - 20))
        barrier.draw(display)

    for rect in dop_barriers:
        rect[1] -= scroll
        if rect.colliderect(pygame.Rect(player.pramoyg.x + 20, player.pramoyg.y + 32, player.pramoyg.width / 4,
                                        player.pramoyg.height / 4)):
            death.play()
            dop_barriers = []
            running = True
            barriers = []

    scripts.script.piece_flash()
    if running:
        scripts.script.generate_text(display, 'GAME OVER!', font, True, (0, 0, 0), (107, 100))
        scripts.script.generate_text(display, 'DISTANCE:' + str(int(distance)), font, True, (0, 0, 0), (100, 150))
        scripts.script.generate_text(display, 'PRESS SPACE TO RESTART!', font, True, (0, 0, 0), (30, 200))
    else:
        scripts.script.generate_text(display, "Distance:" + str(int(distance)), font, True, (0, 0, 0), (20, 25))

    scripts.script.cope_piece(display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if running:
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load('data/Gameplay.ogg')
                    pygame.mixer.music.play(-1)
                    points = []
                    barriers = []
                    dop_barriers = []
                    difficult_num = 0
                    time = 0
                    distance = 0
                    player.present = [size[0] // 4, 50]
                    running = False

    clock.tick(FPS)
    screen.blit(pygame.transform.scale(display, size), (0, 0))
    pygame.display.update()
