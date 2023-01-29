import math
import random

import pygame


class Road:
    def __init__(self, color):
        self.color = color
        self.presents = [[[300, 0], [330, 0]]]
        self.speed = 4

    def draw(self, monitor):
        num = 0
        for element in self.presents:
            element[1][1] -= self.speed
            element[0][1] -= self.speed
            pygame.draw.line(monitor, self.color, element[0], self.presents[num + 1][0], width=3)
            pygame.draw.line(monitor, self.color, element[1], self.presents[num + 1][1], width=3)
            if num < len(self.presents) - 2:
                num += 1
            if element[0][1] < -100:
                self.presents.pop(self.presents.index(element))


class Player():
    def __init__(self, present):
        self.present, self.angle = present, 0
        self.road = Road((170, 170, 170))
        self.road_timer = 6
        self.image = pygame.image.load('data/player.png')
        self.pramoyg = self.image.get_rect()
        self.pramoyg.topleft = self.present

        self.dop_angle, self.timer, self.add = 0, 0, None

    def draw(self, present, mp, end):
        if not end:
            if random.randint(0, 100) == 10:
                self.timer = 30
                self.add = random.choice([False, True])

            if self.timer <= 0:
                if self.dop_angle > 0:
                    self.dop_angle -= 0.5
                elif self.dop_angle < 0:
                    self.dop_angle += 0.5

            self.angle = math.degrees(math.atan2(self.pramoyg.center[0] - mp[0], self.pramoyg.center[1] - mp[1]))

            if self.timer > 0:
                self.timer -= 1
                if self.add == False:
                    self.dop_angle += 1
                else:
                    self.dop_angle -= 1

            self.angle += self.dop_angle
            self.dop_x = math.cos(math.radians(self.angle + 90)) * 5
            self.present[0] += self.dop_x

            if self.road_timer >= 6:
                self.road.presents.append(
                    [[self.pramoyg.center[0] - math.cos(math.radians(self.angle - 90)) * 30 + math.cos(
                        math.radians(self.angle)) * 9,
                      self.pramoyg.center[1] + math.sin(math.radians(self.angle - 90)) * 30],
                     [self.pramoyg.center[0] - math.cos(math.radians(self.angle - 90)) * 30 - math.cos(
                         math.radians(self.angle)) * 9,
                      self.pramoyg.center[1] + math.sin(math.radians(self.angle - 90)) * 30]])

                self.road_timer = 0
            else:
                self.road_timer += 1

            self.road.draw(present)
            changed_image = pygame.transform.rotate(pygame.transform.scale(self.image, (64, 64)), self.angle)
            self.pramoyg = changed_image.get_rect()
            self.pramoyg.topleft = self.present

            present.blit(changed_image, self.present)


class rain():

    def __init__(self):
        pass
