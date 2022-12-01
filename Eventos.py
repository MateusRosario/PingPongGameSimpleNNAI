import pygame
import sys

class Eventos:
    def __init__(self):
        self.key_pressed = []
        self.need_objects = False

    def get_eventos(self):
        for event in pygame.event.get(pygame.KEYDOWN):
            self.key_pressed.append(event.key)

        for event in pygame.event.get(pygame.KEYUP):
            self.key_pressed.remove(event.key)

        if len(pygame.event.get(pygame.QUIT)) != 0:
            sys.exit()

    def get_eventos_list(self):
        self.get_eventos()
        return self.key_pressed