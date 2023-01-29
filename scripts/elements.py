import pygame


def animate(image_list, animation_index, time_to_show_image_on_screen):
    if animation_index + 1 >= len(image_list) * time_to_show_image_on_screen:
        animation_index = 0
    animation_index += 1

    return animation_index


class Barrier:
    def __init__(self, pos, picture, speed):
        self.pos = pos
        self.picture = picture
        self.speed = speed
        self.sizes = self.picture.get_rect()
        self.lifespan = 255

    def draw(self, display):
        self.lifespan -= 1
        display.blit(
            pygame.transform.scale(self.picture, (self.picture.get_width() * 4, self.picture.get_height() * 4)),
            (self.pos[0], self.pos[1]))
        self.pos[1] -= self.speed
        self.sizes.topleft = self.pos


class Deer:
    def __init__(self, x, y, speed):
        self.x, self.y, self.speed = x, y, speed
        self.pictures = [pygame.image.load('data/deer1.png'),
                         pygame.image.load('data/deer2.png'),
                         pygame.image.load('data/deer3.png'),
                         pygame.image.load('data/deer4.png')]
        self.num, self.dop = 0, 0
        if self.x == 700:
            self.dop = -4
        elif self.x == 400:
            self.dop == 4
        self.rectangle = None

    def draw(self, display):
        self.rectangle = pygame.Rect(self.x, self.y, self.pictures[self.num // 15].get_width() * 4,
                                     self.pictures[self.num // 15].get_height() * 4)
        self.num = animate(self.pictures, self.num, 15)
        if self.dop == -4:
            display.blit(pygame.transform.scale(self.pictures[self.num // 15], (
                self.pictures[self.num // 15].get_width() * 4,
                self.pictures[self.num // 15].get_height() * 4)), (self.x, self.y))

        elif self.dop == 4:
            display.blit(
                pygame.transform.scale(pygame.transform.flip(self.pictures[self.num // 15], True, False), (
                    self.pictures[self.num // 15].get_width() * 4,
                    self.pictures[self.num // 15].get_height() * 4)), (self.x, self.y))
        self.y -= self.speed
        self.x += self.dop
