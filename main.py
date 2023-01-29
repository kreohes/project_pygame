import pygame, sys

from scripts.button import Button
import os

pygame.init()

WIDTH, HEIGHT = size = 700, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
pygame.mixer.music.load("data/Menu.mp3")
pygame.mixer.music.play(-1)

BG = pygame.image.load("data/fon1.png")


def get_font(size):
    return pygame.font.Font("data/font.ttf", size)


def play():
    import scripts.gameplay


def main_menu():
    while True:
        screen.blit(BG, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("MENU", True, "#FFFFFF")
        menu_rect = menu_text.get_rect(center=(350, 100))
        play_button = Button(image=pygame.image.load("data/Play Rect.png"), pos=(350, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", appearing_color="White")
        options_button = Button(image=pygame.image.load("data/Options Rect.png"), pos=(350, 400),
                                text_input=F"SCORE 0", font=get_font(75), base_color="#d7fcd4",
                                appearing_color="White")
        quit_button = Button(image=pygame.image.load("data/Quit Rect.png"), pos=(350, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", appearing_color="White")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
