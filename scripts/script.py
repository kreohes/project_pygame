import random
import pygame

particles = []
pygame.font.init()


def generate_text(display, words, font, dop, color, pos):
    words = font.render(words, dop, color)
    display.blit(words, pos)


class Piece:
    def __init__(self, x, y, x1, y1, rad, color, scale):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.physic = 1
        self.rad = rad
        self.color = color
        self.lifespan = 200
        self.scale = scale

    def draw(self, display):
        self.lifespan -= 1
        self.physic -= self.scale
        self.x += self.x1
        self.y += self.y1 * self.physic
        self.rad -= 0.01

        pygame.draw.rect(display, self.color, (int(self.x), int(self.y), self.rad, self.rad))


def piece_flash():
    for i in range(1):
        particles.append(Piece(random.randrange(0, 400), -15, random.randrange(-1, 1), -0.05, 4, (163, 167, 194), 1))


def cope_piece(display):
    for part in particles:
        if part.lifespan > 0:
            part.draw(display)
        else:
            particles.remove(part)
